import datetime
import json
import time
from datetime import date
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
    current_player = ""

    def on_enter(self, *args):
        self.inizialize()
        self.load_game()

    def inizialize(self):
        self.current_player = 'Player1'
        self.level_game = self.manager.element
        self.item = OnboardingItem()
        self.seconds = self.item.get_info_game()['round']

    def load_game(self):
        if self.level_game == 'Easy':
            self.easy_game()
        elif self.level_game == 'Medium':
            self.medium_game()
        else:
            self.hard_game()

    def Callback_Clock(self, df):
        self.seconds = int(self.seconds) - 1
        self.ids.info.clear_widgets()
        if self.seconds == 0:
            Clock.stop_clock()
            self.end_game()
        else:
            self.ids.info.add_widget(MDLabel(text=str(self.game_card.get_info_round()['jump']), font_style="H4", halign="left"))
            self.ids.info.add_widget(MDLabel(text=time.strftime("%M:%S", time.gmtime(self.seconds)), font_style="H4", halign="center"))
            self.ids.info.add_widget(MDLabel(text=str(self.game_card.get_info_round()['ok']), font_style="H4", halign="right"))

    def easy_game(self):
        with open("../assets/resources/easy_game.json") as game_file:
            words = json.load(game_file)
        index = randint(1, 10)
        self.card_game(words, index)
        while self.game_card.get_info_update() and self.seconds>0:
            index = randint(1, 10)
            self.card_game(words, index)


    def medium_game(self):
        pass

    def hard_game(self):
        pass

    def card_game(self, words, index):
        Clock.schedule_interval(self.Callback_Clock, 1)
        self.game_card = GameCard(
            text=words[index]["word"],
            subtext=words[index]["forbidden"][0] + '\n' + words[index]["forbidden"][1] + '\n' + words[index]["forbidden"][
                2] + '\n' + words[index]["forbidden"][3] + '\n' + words[index]["forbidden"][4]
        )
        self.game_card.set_info_round(self.item.get_info_game()['jump'])
        self.ids.container.add_widget(self.game_card)


    def end_game(self):
        filename = '../assets/resources/points.json'
        num_player = int(self.item.get_info_game()['num'])
        points = {'num': num_player}
        a_datetime = datetime.datetime.now().date()
        formatted_datetime = a_datetime.isoformat()
        json_datetime = json.dumps(formatted_datetime)
        for i in range(0, num_player):
            values = self.game_card.info_round['ok'] - self.game_card.info_round['wrong']
            points.update({'point' + str(i): values})
            print(points)
        entry = {'index': 1, 'day': json_datetime, 'level': self.level_game, 'players': [points]}

        with open(filename, "r+") as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file)

