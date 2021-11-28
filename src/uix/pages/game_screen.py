import json
from random import randint

from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from uix.components.game_card import GameCard


class GameScreen(MDScreen):
    level_game = "easy"
    time = ""
    game_card = None
    count = 00
    hours = 0
    text = StringProperty()
    subtext = StringProperty()
    wrong_answer_point = 0
    ok_answer_point = 0
    jump_answer_point = 5
    def on_enter(self, *args):
        self.load_game()
        Clock.schedule_interval(self.Callback_Clock, 1)

    def load_game(self):
        if self.level_game == 'easy':
            self.easy_game()
        elif self.level_game == 'medium':
            self.medium_game()
        else:
            self.wrong_answer()

    def Callback_Clock(self, df):
        self.count = self.count + 1
        print(self.count)
        if self.hours == 3 and self.count == 60:
            self.ids.time.clear_widgets()
            self.pause_game()
        if self.count == 60:
            self.hours = self.hours + 1
            self.count = 00
        self.ids.time.clear_widgets()
        self.ids.time.add_widget(MDLabel(text=str(self.hours) + ":" + str(self.count), font_style="H4", halign= "center" ))

    def easy_game(self):
        with open("../assets/resources/easy_game.json") as game_file:
            words = json.load(game_file)

        if not self.game_card:
            i = randint(1, 10)
            print(words[i]["word"])
            print(words[i]["forbidden"])
            self.game_card = GameCard(
                text=words[i]["word"],
                subtext=words[i]["forbidden"][0] + '\n' + words[i]["forbidden"][1] + '\n' + words[i]["forbidden"][2] + '\n' + words[i]["forbidden"][3] + '\n' + words[i]["forbidden"][4],
                wrong_answer_action=self.wrong_answer(),
                ok_answer_action=self.ok_answer(),
                jump_answer_action=self.jump_answer()
            )
            self.ids.info.clear_widgets()
            self.ids.info.add_widget(MDLabel(text=str(self.jump_answer_point), font_style="H4", halign= "left"),MDLabel(text=str(self.ok_answer_point), font_style="H4", halign= "center") )
            self.ids.container.add_widget(self.game_card)


    def medium_game(self):
        pass

    def wrong_answer(self):
        print("wrong_answer_action")

    def pause_game(self):
        print("pause_game")

    def wrong_answer(self):
        self.wrong_answer_point += 1
        return self.wrong_answer_point

    def ok_answer(self):
        self.ok_answer_point += 1
        return self.ok_answer_point

    def jump_answer(self):
        if self.jump_answer_point < 5:
            self.jump_answer_point += 1
        return self.jump_answer_point