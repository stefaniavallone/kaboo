import json
from random import shuffle

from kivmob import TestIds
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen

from uix.base_components.kmd_fill_round_flat_button import \
    KMDFillRoundFlatButton
from uix.components.confirm_content import ConfirmContent
from kivy.app import App
from logic.game import PLAYERS_COLORS
from uix.base_components.kmodal_view import KModalView


class GameScreen(MDScreen):
    confirm_exit_dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()

    def on_resume(self):
        self.app.ads.request_interstitial()

    def on_pre_enter(self, *args):
        self.app.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.app.ads.request_interstitial()
        self.app.ads.show_interstitial()
        self.round_time = self.app.status.getv("game.round_time",
                                               default_value=15)
        self.num_players = self.app.status.getv("game.num_players",
                                                default_value=2)
        self.num_jumps = self.app.status.getv("game.num_jumps", default_value=5)
        self.game_level = self.app.status.getv("game.level",
                                               default_value="easy")
        self.current_round = self.app.status.getv("game.current_round",
                                                  default_value=0)
        self.current_player = self.app.status.getv("game.current_player",
                                                   default_value=0)

        sounds_on = self.app.status.getv("game.sound", default_value=True)
        self._set_sound_icon(sounds_on)

        Clock.schedule_once(self.load_music)
        self.load_game()
        self.play_round()

    def on_enter(self, *args):
        pass

    def load_music(self, *args):
        self.app_background_music = self.app.sound_manager.get_sound(
            "assets/sounds/cute.ogg")
        self.game_background_music = self.app.sound_manager.get_sound(
            'assets/sounds/ukulele.ogg',
            True, 0.2)
        self.clock_sound = self.app.sound_manager.get_sound(
            'assets/sounds/clock-ticking.ogg')
        self.right_notification = self.app.sound_manager.get_sound(
            'assets/sounds/right-notification.wav')
        self.wrong_notification = self.app.sound_manager.get_sound(
            'assets/sounds/wrong-notification.wav')
        self.jump_notification = self.app.sound_manager.get_sound(
            'assets/sounds/jump-notification.wav')
        self.app_background_music.stop()
        self.game_background_music.play()

    def _set_sound_icon(self, sounds_on):
        self.ids.sound_button.icon = "assets/images/icons/volume-off.png" \
            if sounds_on else "assets/images/icons/volume-high.png"

    def toggle_sounds(self):
        sounds_on = self.app.status.getv("game.sound", default_value=True)
        self._set_sound_icon(not sounds_on)
        self.app.status.setv("game.sound", not sounds_on)

    def load_game(self, *args):
        self.elements = []
        locale = self.app.status.getv("app.lang")
        with open(
                f"assets/resources/game_levels/{locale}/{self.game_level}.json") as game_file:
            game_elements = json.load(game_file)
            shuffle(game_elements)
            self.elements = game_elements
            Logger.info(f"Loading Game - {len(self.elements)} Elements: {self.elements}")
        self.elem_idx = 0
        for element in self.elements[:2]:
            self.ids.card_container.add_card(element["word"],
                                             element["forbidden"])
            self.elem_idx = self.elem_idx + 1

    def play_round(self, *args):
        Logger.debug(
            f"Playing round {self.current_round + 1} for player {self.current_player + 1}")
        self.ids.remaining_jumps.text = str(self.num_jumps)
        self.ids.jump_button.disabled = True if self.num_jumps == 0 else False
        self.ids.container.md_bg_color = PLAYERS_COLORS[self.current_player]
        self.ids.player_points.text = "0"
        self.actions = []
        self.ids.timer.seconds = self.round_time
        self.ids.timer.start()

    def wrong_answer(self):
        self.wrong_notification.play()
        self.actions.append("wrong")
        self.ids.player_points.text = str(int(self.ids.player_points.text) - 1)
        self.next_card()

    def right_answer(self):
        self.right_notification.play()
        self.actions.append("right")
        self.ids.player_points.text = str(int(self.ids.player_points.text) + 1)
        self.next_card()

    def jump_request(self):
        if int(self.ids.remaining_jumps.text) > 0:
            self.jump_notification.play()
            self.actions.append("jump")
            value = int(self.ids.remaining_jumps.text)
            self.ids.remaining_jumps.text = str(value - 1)
            if value - 1 == 0:
                self.ids.jump_button.disabled = True
            self.next_card()

    def next_card(self):
        if self.elem_idx < len(self.elements):
            self.ids.card_container.ids.swiper.next()
            self.ids.card_container.add_card(
                self.elements[self.elem_idx]["word"],
                self.elements[self.elem_idx]["forbidden"])
            self.elem_idx = self.elem_idx + 1
        else:
            self.ids.card_container.ids.swiper.next()

    def finish_round(self):
        self.app.status.setv(
            f"game.rounds.r{self.current_round}.p{self.current_player}.points",
            int(self.ids.player_points.text))
        self.app.status.setv(
            f"game.rounds.r{self.current_round}.p{self.current_player}.actions",
            self.actions)
        self.app.status.setv("game.current_player", self.current_player + 1)
        if self.current_player == self.num_players - 1:
            self.app.status.setv("game.current_player", 0)
            self.app.status.setv("game.current_round", self.current_round + 1)
            if self.current_round == 1:
                self.manager.go_to_screen('game_end', direction='right')
            else:
                self.manager.go_to_screen('game_pre', direction='right')
        else:
            self.manager.go_to_screen('game_pre', direction='right')

    def on_pre_leave(self, *args):
        if self.confirm_exit_dialog:
            self.confirm_exit_dialog.dismiss()
        self.game_background_music.stop()
        self.clock_sound.stop()

    def confirm_exit(self):
        self.clock_sound.stop()
        self.ids.timer.stop()
        self.confirm_exit_dialog = \
            KModalView(size_hint=(0.7, 0.4),
                       auto_dismiss=False,
                       closable=False,
                       background_color=[0, 0, 0, 0],
                       content=ConfirmContent(image="assets/images/go_home.png",
                           text=self.app.i18n._("DIALOG_BACK_HOME_TITLE"),
                           subtext=self.app.i18n._("DIALOG_BACK_HOME_DESC")),
                       buttons=[
                           KMDFillRoundFlatButton(text=self.app.i18n._(
                               "GAME_CANCEL_BUTTON").upper(),
                                                  radius=[dp(10), dp(10),
                                                          dp(10), dp(10)],
                                                  width="100dp",
                                                  size_hint_x=None,
                                                  md_bg_color=(
                                                  0, 0.2, 0.9, 1),
                                                  on_release=self.cancel),
                           KMDFillRoundFlatButton(text=self.app.i18n._(
                               "GAME_BACK_HOME_BUTTON").upper(),
                                                  md_bg_color=(1, 0, 0, 1),
                                                  radius=[dp(10), dp(10),
                                                          dp(10), dp(10)],
                                                  width="100dp",
                                                  size_hint_x=None,
                                                  on_release=self.to_home),
                       ])
        self.confirm_exit_dialog.open()

    def cancel(self, inst):
        self.ids.timer.start()
        self.confirm_exit_dialog.dismiss()

    def to_home(self, inst):
        self.game_background_music.stop()
        self.clock_sound.stop()
        self.ids.timer.stop()
        self.confirm_exit_dialog.dismiss()
        self.app.status.setv("game.current_player", 0)
        self.manager.go_to_screen('home', direction='right')
