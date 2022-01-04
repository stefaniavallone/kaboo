import datetime
import json
import re
import time
from random import randint

from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton

from uix.components.element_card import ElementCard
from uix.components.game_card import GameCard
from uix.components.onboarding_item import OnboardingItem


class GameScreen(MDScreen):
    game_card = None
    text = StringProperty()
    subtext = StringProperty()
    current_player = ""
    num_round = 0
    jump = 0
    interval_clock = None
    trophies = ""

    def on_enter(self, *args):
        self.interval_clock = Clock.schedule_interval(self.start_game, 1)
        self.inizialize()
        self.load_game()

    def inizialize(self):
        self.level_game = self.manager.element
        self.item = OnboardingItem()
        self.current_player = self.item.info_game['num'][0]
        self.seconds = self.item.info_game['round']
        self.jump = self.item.info_game['jump']
        with open("../assets/resources/trophies.json") as trophies_file:
            trophies = json.load(trophies_file)


    def load_game(self):
        if self.level_game == 'Easy':
            self.easy_game()
        elif self.level_game == 'Medium':
            self.medium_game()
        else:
            self.hard_game()

    def start_game(self, df):
        self.seconds = int(self.seconds) - 1
        self.ids.info.clear_widgets()
        value = self.game_card.info_round
        self.jump = self.game_card.info_round['jump']
        if self.seconds == 0:
            self.game_card.calculate_points(self.current_player, value)
            Clock.schedule_once(self.stop_clock, 0)
            entry = self.calculate_round_point()
            subtext = ""
            self.num_round += 1
            for i in range(0, len(self.game_card.points_game)):
                subtext += self.item.info_game['num'][i] + ': ' + str(self.game_card.points_game[self.item.info_game['num'][i]]) + '\n'
                self.check_tropheis(self.game_card.points_game[self.item.info_game['num'][i]])
            if self.num_round == 3 * len(self.item.info_game['num']):
                return self.end_game(entry, subtext)
            self.current_player = self.item.info_game['num'][self.num_round % len(self.item.info_game['num'])]
            self.seconds = self.item.info_game['round']
            value['jump'] = self.item.info_game['jump']
            value['ok'] = 0
            value['wrong'] = 0
            self.jump = self.item.info_game['jump']
            restart_game = ElementCard(
                image="../assets/images/start.png",
                text='Finish round ' + str(self.num_round) + ' turn of ' + self.current_player,
                subtext=subtext,
                radius=[20, 7, 20, 7],
                on_release=self.restart
            )
            self.ids.container.clear_widgets()
            self.ids.restart_game.add_widget(restart_game)
        else:
            if value['update']:
                value['update'] = False
                self.load_game()
            self.ids.info.add_widget(MDLabel(text=str(value['jump']), font_style="H4", halign="left"))
            self.ids.info.add_widget(MDLabel(text=time.strftime("%M:%S", time.gmtime(self.seconds)), font_style="H4", halign="center"))
            self.ids.info.add_widget(MDLabel(text=str(value['ok']), font_style="H4", halign="right"))

    def restart(self, inst):
        self.ids.restart_game.clear_widgets()
        self.interval_clock = Clock.schedule_interval(self.start_game, 1)
        self.load_game()

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
        if not self.game_card is None and int(self.game_card.info_round['jump']) < 1:
            print(self.game_card.info_round['jump'])
            self.game_card.__setattr__('text', words[index]["word"]),
            self.game_card.__setattr__('subtext', words[index]["forbidden"][0] + '\n' + words[index]["forbidden"][1] + '\n' + words[index]["forbidden"][
                    2] + '\n' + words[index]["forbidden"][3] + '\n' + words[index]["forbidden"][4]),
            self.game_card.__setattr__('md_bg_color', color),
            self.game_card.__setattr__('close_thick', 'close-thick'),
            self.game_card.__setattr__('check_bold', 'check-bold')

        else:
            self.game_card = GameCard(
                text=words[index]["word"],
                subtext=words[index]["forbidden"][0] + '\n' + words[index]["forbidden"][1] + '\n' +
                        words[index]["forbidden"][2] + '\n' + words[index]["forbidden"][3] + '\n' + words[index]["forbidden"][4],
                md_bg_color=color,
                close_thick="close-thick",
                redo="redo",
                check_bold="check-bold"
            )
        self.game_card.info_round['jump'] = self.jump
        self.ids.container.add_widget(self.game_card)

    def calculate_round_point(self):
        num_player = len(self.item.info_game['num'])
        points = {'num': num_player}
        a_datetime = datetime.datetime.now().date()
        formatted_datetime = a_datetime.isoformat()
        json_datetime = json.dumps(formatted_datetime)
        for i in range(0, len(self.game_card.points_game)):
            points.__setitem__(self.item.info_game['num'][i], str(self.game_card.points_game[self.item.info_game['num'][i]]))
        return {'day': json_datetime, 'level': self.level_game, 'players': [points]}

    def end_game(self, entry, subtext):
        Clock.unschedule(self.interval_clock)
        self.write_on_file(entry)
        self.ids.container.clear_widgets()
        points = [int(s) for s in subtext.split() if s.isdigit()]

        end = ElementCard(
            image="../assets/images/the_end.png",
            text="Winner is ",
            subtext=subtext,
            on_release=self.back_home
        )
        self.ids.end_game.add_widget(end)

    def back_home(self, inst):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

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

    def check_tropheis(self, value):
        print([x for x in self.trophies if x["points"]==value])

    def stop_clock(self, *args):
        self.interval_clock.cancel()