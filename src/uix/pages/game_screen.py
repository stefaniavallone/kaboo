import json
from random import shuffle

from kivy.logger import Logger
from kivy.uix.modalview import ModalView
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from uix.components.custom_modal import CustomModal
from kivy.app import App
from logic.game import PLAYERS_COLORS


class GameScreen(MDScreen):
    confirm_exit_dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()

    def on_pre_enter(self, *args):
        self.round_time = self.app.status.getv("game.round_time", default_value=15)
        self.num_players = self.app.status.getv("game.num_players", default_value=2)
        self.num_jumps = self.app.status.getv("game.num_jumps", default_value=5)
        self.game_level = self.app.status.getv("game.level", default_value="easy")
        self.current_round = self.app.status.getv("game.current_round",
                                            default_value=0)
        self.current_player = self.app.status.getv("game.current_player",
                                             default_value=0)
        self.background_music = self.app.sound_manager.add_sound('../assets/sounds/ukulele.mp3',
                                            True, 0.2)
        self.clock_sound = self.app.sound_manager.add_sound('../assets/sounds/clock-ticking.mp3')
        self.right_notification = self.app.sound_manager.add_sound(
            '../assets/sounds/right-notification.wav')
        self.wrong_notification = self.app.sound_manager.add_sound(
            '../assets/sounds/wrong-notification.wav')
        self.jump_notification = self.app.sound_manager.add_sound(
            '../assets/sounds/jump-notification.wav')
        self.load_game()
        self.play_round()
        self.background_music.play()

    def toggle_sounds(self):
        sounds_on = self.app.status.getv("game.sound", default_value=True)
        self.ids.sound_button.icon = "volume-high" if sounds_on else "volume-off"
        if not sounds_on:
            self.background_music.play(restart=True)  # restart game music when button is pressed
        self.app.status.setv("game.sound", not sounds_on)

    def load_game(self):
        with open(f"../assets/resources/game_levels/{self.game_level}.json") as game_file:
            game_elements = json.load(game_file)
            shuffle(game_elements)
            self.elements = game_elements + [{"word": "",
                                              "forbidden": []}]  # add another empty for graphic reasons
        self.elem_idx = 0
        for element in self.elements[:2]:
            self.ids.card_container.add_card(element["word"],
                                             element["forbidden"])
            self.elem_idx = self.elem_idx + 1

    def play_round(self):
        Logger.debug(
            f"Playing round {self.current_round + 1} for player {self.current_player + 1}")
        self.ids.remaining_jumps.text = str(self.num_jumps)
        self.ids.jump_button.disabled = False
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
                self.manager.transition.direction = 'right'
                self.manager.current = 'game_end'
            else:
                self.manager.transition.direction = 'right'
                self.manager.current = 'game_pre'
        else:
            self.manager.transition.direction = 'right'
            self.manager.current = 'game_pre'

    def on_pre_leave(self, *args):
        if self.confirm_exit_dialog:
            self.confirm_exit_dialog.dismiss()
        self.background_music.stop()
        self.clock_sound.stop()

    def confirm_exit(self):
        self.clock_sound.stop()
        self.ids.timer.stop()
        e = CustomModal(
                image="../assets/images/trophies/trophy_5points.png",
                bg_color=(1, 1, 1, 1),
                text="Are you sure?", 
                subtext="You will lose game progress.",
                closable=False,
                buttons=[
                    MDFillRoundFlatButton(text="Back to Home".upper(),
                                           md_bg_color=(1, 0, 0, 1),
                                          width="100dp", size_hint_x=None,
                                          on_release=self.to_home),
                    MDFillRoundFlatButton(text="Cancel".upper(),
                                           width="100dp", size_hint_x=None,
                                          md_bg_color=(0, 0.2, 0.9, 1),
                                          on_release=self.cancel)
                ]
        )
        if not self.confirm_exit_dialog:
            self.confirm_exit_dialog = ModalView(size_hint=(0.7, 0.4),
                                                 auto_dismiss=True,
                                                 background_color=[0, 0, 0, 0])
            self.confirm_exit_dialog.add_widget(e)
        self.confirm_exit_dialog.open()

    def cancel(self, inst):
        if self.ids.timer.seconds <= 10:
            self.clock_sound.play()
        self.ids.timer.start()
        self.confirm_exit_dialog.dismiss()

    def to_home(self, inst):
        self.background_music.stop()
        self.clock_sound.stop()
        self.ids.timer.stop()
        self.confirm_exit_dialog.dismiss()
        self.go_to_screen('home', direction='right')
