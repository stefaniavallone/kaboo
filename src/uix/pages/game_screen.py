import datetime
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
    current_player = ""
    num_round = 0
    jump = 0

    def on_enter(self, *args):
        self.inizialize()
        self.load_game()

    def inizialize(self):
        self.level_game = self.manager.element
        self.item = OnboardingItem()
        self.current_player = self.item.info_game['num'][0]
        self.seconds = self.item.info_game['round']
        self.jump = self.item.info_game['jump']
        Clock.schedule_interval(self.callback_clock, 1)

    def load_game(self):
        if self.level_game == 'Easy':
            self.easy_game()
        elif self.level_game == 'Medium':
            self.medium_game()
        else:
            self.hard_game()

    def callback_clock(self, df):
        self.seconds = int(self.seconds) - 1
        self.ids.info.clear_widgets()
        value = self.game_card.info_round
        self.jump = self.game_card.info_round['jump']
        if self.seconds == 0:

            self.seconds = self.item.info_game['round']
            self.game_card.calculate_points(self.current_player, value)
            value['jump'] = self.item.info_game['jump']
            value['ok'] = 0
            value['wrong'] = 0
            self.num_round += 1
            self.current_player = self.item.info_game['num'][self.num_round%len(self.item.info_game['num'])]
            if self.num_round == 3 * len(self.item.info_game['num']):
                self.end_game()
        else:
            if value['update']:
                value['update'] = False
                self.load_game()
        self.ids.info.add_widget(MDLabel(text=str(value['jump']), font_style="H4", halign="left"))
        self.ids.info.add_widget(MDLabel(text=time.strftime("%M:%S", time.gmtime(self.seconds)), font_style="H4", halign="center"))
        self.ids.info.add_widget(MDLabel(text=str(value['ok']), font_style="H4", halign="right"))


    def easy_game(self):
        with open("../assets/resources/easy_game.json") as game_file:
            words = json.load(game_file)
        self.card_game(words)

    def medium_game(self):
        with open("../assets/resources/easy_game.json") as game_file:
            words = json.load(game_file)
        self.card_game(words)

    def hard_game(self):
        with open("../assets/resources/easy_game.json") as game_file:
            words = json.load(game_file)
        self.card_game(words)

    def card_game(self, words):
        index = randint(1, 10)
        self.ids.container.clear_widgets()
        color = self.item.info_game['color_player'][self.num_round%len(self.item.info_game['num'])]
        print(color)
        self.game_card = GameCard(
            text=words[index]["word"],
            subtext=words[index]["forbidden"][0] + '\n' + words[index]["forbidden"][1] + '\n' + words[index]["forbidden"][
                2] + '\n' + words[index]["forbidden"][3] + '\n' + words[index]["forbidden"][4],
            md_bg_color=color
        )
        self.game_card.info_round['jump'] = self.jump
        self.ids.container.add_widget(self.game_card)


    def end_game(self):

        num_player = len(self.item.info_game['num'])
        points = {'num': num_player}
        a_datetime = datetime.datetime.now().date()
        formatted_datetime = a_datetime.isoformat()
        json_datetime = json.dumps(formatted_datetime)
        subtext = ""
        for i in range(0, num_player):
            points.__setitem__(self.item.info_game['num'][i], str(self.game_card.points_game[self.item.info_game['num'][i]]))
            subtext += self.item.info_game['num'][i] + ': ' + str(self.game_card.points_game[self.item.info_game['num'][i]]) + '\n'
        entry = {'day': json_datetime, 'level': self.level_game, 'players': [points]}
        self.write_on_file(entry)
        self.ids.container.clear_widgets()
        self.end_game = GameCard(
            text='THE END',
            subtext=subtext,
            md_bg_color= [1, 0, 0, 1]
        )
        self.ids.end_game.add_widget(self.end_game)


    def write_on_file(self,entry):
        filename = '../assets/resources/points.json'
        with open(filename, "r+") as file:
            data = json.load(file)
            try:
                if data[len(data)-1]['id'] > 0:
                    entry.__setitem__('id',data[len(data)-1]['id']+1)
            except:
                entry.__setitem__('id', 1)
            data.append(entry)
            file.seek(0)
            json.dump(data, file)

