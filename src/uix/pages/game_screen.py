import datetime
from functools import partial
import json
import re
import time
from random import randint
from types import SimpleNamespace
from kivy.core.audio import SoundLoader

from kivy.clock import Clock
from kivy.logger import Logger
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from src.app_status import AppStatus
from src.utils.sound_player import SoundPlayer

from uix.components.element_card import ElementCard



class GameScreen(MDScreen):

    COLORS = [(1, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (0, 0, 1, 1)]

    def __init__(self, **kw):
        self.sound = None
        super().__init__(**kw)
    
    def on_pre_enter(self, *args):
        self.round_time = AppStatus.get("game.round_time", default_value=25)
        self.num_players = AppStatus.get("game.num_players", default_value=2)
        self.num_jumps = AppStatus.get("game.num_jumps", default_value=5)
        self.game_level = AppStatus.get("game.level", default_value="easy")
        self.current_round = AppStatus.get("game.current_round", default_value=0)
        self.current_player = AppStatus.get("game.current_player", default_value=0)
        self.background_music = SoundPlayer('../assets/sounds/ukulele.mp3', True, 0.2)
        self.right_notification = SoundPlayer('../assets/sounds/right-notification.wav')
        self.wrong_notification = SoundPlayer('../assets/sounds/wrong-notification.wav')
        self.jump_notification = SoundPlayer('../assets/sounds/jump-notification.wav')
        self.load_game()
        self.play_round()
        self.background_music.play()
    
    def load_game(self):
        with open(f"../assets/resources/game_levels/{self.game_level}.json") as game_file:
            self.elements = json.load(game_file) + [{"word": "", "forbidden": []}]  # add another empty for graphic reasons
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
        self.ids.timer.seconds = self.round_time
        self.ids.timer.start()
 
    def wrong_answer(self):
        self.wrong_notification.play()
        self.ids.player_points.text = str(int(self.ids.player_points.text) - 1)
        self.next_card()
        
    def right_answer(self):
        self.right_notification.play()
        self.ids.player_points.text = str(int(self.ids.player_points.text) + 1)
        self.next_card()
        
    def jump_request(self):
        if int(self.ids.remaining_jumps.text) > 0:
            self.jump_notification.play()
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
        AppStatus.set(f"game.rounds.{self.current_round}.{self.current_player}", int(self.ids.player_points.text))
        AppStatus.set("game.current_player", self.current_player + 1)
        if self.current_player == self.num_players - 1:
            AppStatus.set("game.current_player", 0)
            AppStatus.set("game.current_round", self.current_round + 1)
            if self.current_round == 1:
                if self.sound:
                    self.sound.stop()
                self.manager.transition.direction = 'right'
                self.manager.current = 'game_end'
            else:
                self.manager.transition.direction = 'right'
                self.manager.current = 'game_pre'
        else:
            self.manager.transition.direction = 'right'
            self.manager.current = 'game_pre'

    def on_pre_leave(self, *args):
        self.background_music.stop()
        
    # def calculate_round_point(self):
    #     num_player = len(self.item.info_game['num'])
    #     points = {'num': num_player}
    #     a_datetime = datetime.datetime.now().date()
    #     formatted_datetime = a_datetime.isoformat()
    #     json_datetime = json.dumps(formatted_datetime)
    #     for i in range(0, len(self.game_card.points_game)):
    #         points.__setitem__(self.item.info_game['num'][i], str(self.game_card.points_game[self.item.info_game['num'][i]]))
    #     return {'day': json_datetime, 'level': self.level_game, 'players': [points]}

