import json
import time
from random import randint

from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from uix.components.game_card import GameCard
from uix.components.onboarding_item import OnboardingItem

class GameScreen(MDScreen):
    game_card = None
    text = StringProperty()
    subtext = StringProperty()

    def on_enter(self, *args):
        self.inizialize()
        self.load_game()
        #Clock.schedule_interval(self.Callback_Clock, 1)

    def inizialize(self):
        self.level_game = "easy"
        self.item = OnboardingItem()
        self.seconds = self.item.get_info_game()['round']
        self.wrong_answer_point = 0
        self.ok_answer_point = 0
        self.level_game = "easy"

    def load_game(self):
        if self.level_game == 'easy':
            self.easy_game()
        elif self.level_game == 'medium':
            self.medium_game()
        else:
            self.hard_game()

    def Callback_Clock(self, df):
        self.seconds = int(self.seconds) - 1
        self.ids.info.clear_widgets()
        if self.seconds == 0:
            Clock.stop_clock()
            self.pause_game()
        else:
            self.ids.info.add_widget(MDLabel(text=str(self.game_card.get_info_round()['jump']), font_style="H4", halign="left"))
            self.ids.info.add_widget(MDLabel(text=time.strftime("%M:%S", time.gmtime(self.seconds)), font_style="H4", halign="center"))
            self.ids.info.add_widget(MDLabel(text=str(self.game_card.get_info_round()['ok']), font_style="H4", halign="right"))

    def easy_game(self):
        with open("../assets/resources/easy_game.json") as game_file:
            words = json.load(game_file)
        if not self.game_card:
            i = randint(1, 10)
            Clock.schedule_interval(self.Callback_Clock, 1)
            self.game_card = GameCard(
                text=words[i]["word"],
                subtext=words[i]["forbidden"][0] + '\n' + words[i]["forbidden"][1] + '\n' + words[i]["forbidden"][2] + '\n' + words[i]["forbidden"][3] + '\n' + words[i]["forbidden"][4]
            )
            self.game_card.set_info_round(self.item.get_info_game()['jump'])
            self.ids.container.add_widget(self.game_card)

    def medium_game(self):
        pass

    def hard_game(self):
        pass

    def pause_game(self):
        self.game_card = GameCard(
            text='PROVA',
            subtext='PIPPO'
        )
        self.ids.container.clear_widgets()
        self.ids.container.add_widget(self.game_card)
        with open('../assets/resources/points.json', 'w') as f:
            f.write("appended text")
