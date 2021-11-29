from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivymd.uix.card import MDCard

Builder.load_file("uix/components/kv/game_card.kv")
class GameCard(MDCard):
    text = StringProperty()
    subtext = StringProperty()
    jump_enabled =  BooleanProperty(True)
    info_round = {"wrong": '0', "jump": '', "ok": '0', "update":False};

    def wrong_answer(self):
        self.info_round['update'] = True
        self.info_round['wrong'] = int(self.info_round['wrong']) + 1
        print(self.info_round['wrong'])

    def ok_answer(self):
        self.info_round['update'] = True
        self.info_round['ok'] = int(self.info_round['ok']) + 1
        print(self.info_round['ok'])

    def jump_answer(self):
        self.info_round['update'] = True
        if int(self.info_round['jump']) > 0:
            self.info_round['jump'] = int(self.info_round['jump']) - 1
        else:
            self.jump_enabled = False
        print(self.info_round['jump'])

    def get_info_round(self):
        return self.info_round

    def set_info_round(self, jump):
        self.info_round['jump'] = jump

    def set_info_update(self):
        self.info_round['update'] = False