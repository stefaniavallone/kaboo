from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.card import MDCard

Builder.load_file("uix/components/kv/game_card.kv")
class GameCard(MDCard):
    text = StringProperty()
    subtext = StringProperty()
    jump_enabled =  BooleanProperty(True)
    info_round = {"wrong": 0, "jump": '', "ok": 0, "update": False}
    points_game = {}

    def wrong_answer(self):
        self.info_round['update'] = True
        self.info_round['wrong'] += 1
        print(self.info_round['wrong'])

    def ok_answer(self):
        self.info_round['update'] = True
        self.info_round['ok'] += 1
        print(self.info_round['ok'])

    def jump_answer(self):
        self.info_round['update'] = True
        if int(self.info_round['jump']) > 0:
            self.info_round['jump'] = int(self.info_round['jump']) - 1
        else:
            self.jump_enabled = False
        print(self.info_round['jump'])
        return self.info_round['jump']

    def calculate_points(self, players, info_round):
        value = info_round['ok'] - info_round['wrong'] + int(info_round['jump'])
        try:
            self.point = value + self.points_game[players]
            self.points_game[players] = self.point
            self.points_game.__setitem__(players, self.point)
        except:
            self.points_game.__setitem__(players,value)

        print(self.points_game)
