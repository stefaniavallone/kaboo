import json
from random import shuffle

from kivy.logger import Logger
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from app_status import AppStatus
from utils.sound_player import SoundPlayer


class GameScreen(MDScreen):

    COLORS = [(1, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (0, 0, 1, 1)]
    confirm_exit_dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def on_pre_enter(self, *args):
        self.round_time = AppStatus.get("game.round_time", default_value=15)
        self.num_players = AppStatus.get("game.num_players", default_value=2)
        self.num_jumps = AppStatus.get("game.num_jumps", default_value=5)
        self.game_level = AppStatus.get("game.level", default_value="easy")
        self.current_round = AppStatus.get("game.current_round", default_value=0)
        self.current_player = AppStatus.get("game.current_player", default_value=0)
        self.background_music = SoundPlayer('../assets/sounds/ukulele.mp3', True, 0.2)
        self.clock_sound = SoundPlayer('../assets/sounds/clock-ticking.mp3')
        self.right_notification = SoundPlayer('../assets/sounds/right-notification.wav')
        self.wrong_notification = SoundPlayer('../assets/sounds/wrong-notification.wav')
        self.jump_notification = SoundPlayer('../assets/sounds/jump-notification.wav')
        self.load_game()
        self.play_round()
        self.background_music.play()
    
    def load_game(self):
        with open(f"../assets/resources/game_levels/{self.game_level}.json") as game_file:
            game_elements = json.load(game_file)
            shuffle(game_elements)
            self.elements = game_elements + [{"word": "", "forbidden": []}]  # add another empty for graphic reasons
        self.elem_idx = 0
        for element in self.elements[:2]:
            self.ids.card_container.add_card(element["word"], element["forbidden"])
            self.elem_idx = self.elem_idx + 1

    def play_round(self):
        Logger.debug(f"Playing round {self.current_round+1} for player {self.current_player+1}")
        self.ids.remaining_jumps.text = str(self.num_jumps)
        self.ids.jump_button.disabled = False
        self.ids.container.md_bg_color = self.COLORS[self.current_player]
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
            self.ids.card_container.add_card(self.elements[self.elem_idx]["word"], 
                                             self.elements[self.elem_idx]["forbidden"])
            self.elem_idx = self.elem_idx + 1
        else:
            self.ids.card_container.ids.swiper.next()
    
    def finish_round(self):
        self.background_music.stop()
        self.clock_sound.stop()
        AppStatus.set(f"game.rounds.r{self.current_round}.p{self.current_player}.points", int(self.ids.player_points.text))
        AppStatus.set(f"game.rounds.r{self.current_round}.p{self.current_player}.actions", self.actions)
        AppStatus.set("game.current_player", self.current_player + 1)
        if self.current_player == self.num_players - 1:
            AppStatus.set("game.current_player", 0)
            AppStatus.set("game.current_round", self.current_round + 1)
            if self.current_round == 1:
                self.manager.transition.direction = 'right'
                self.manager.current = 'game_end'
            else:
                self.manager.transition.direction = 'right'
                self.manager.current = 'game_pre'
        else:
            self.manager.transition.direction = 'right'
            self.manager.current = 'game_pre'

    def confirm_exit(self):

        if not self.confirm_exit_dialog:
            content = MDFlatButton(text="aaaa", md_bg_color=(1,0,0,1),
                                   on_release=self.to_home)
            self.confirm_exit_dialog = MDDialog(
                type="custom",
                radius=[20, 7, 20, 7],
                auto_dismiss=False,
                size_hint=(.7, .6),
                content_cls=content
            )
        self.confirm_exit_dialog.open()

    def to_home(self, inst):
        self.background_music.stop()
        self.clock_sound.stop()
        self.ids.timer.stop()
        self.confirm_exit_dialog.dismiss()
        self.go_to_screen('home', direction='right')
 
    

