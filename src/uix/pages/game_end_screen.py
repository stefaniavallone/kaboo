import json

from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from src.app_status import AppStatus

from uix.components.element_card import ElementCard


class GameEndScreen(MDScreen):
    round_time = StringProperty()
    num_players = StringProperty()
    num_jumps = StringProperty()
    game_level = StringProperty()
    current_round = StringProperty()
    current_player = StringProperty()
    points = StringProperty()
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def on_pre_enter(self, *args):
        self.round_time = str(AppStatus.get("game.round_time", default_value="25"))
        self.num_players = str(AppStatus.get("game.num_players", default_value="2"))
        self.num_jumps = str(AppStatus.get("game.num_jumps", default_value="5"))
        self.game_level = AppStatus.get("game.level", default_value="easy")
        self.current_round = str(AppStatus.get("game.current_round", default_value="0"))
        self.current_player = str(AppStatus.get("game.current_player", default_value="Players1"))
        self.points = str(AppStatus.get(f"game.rounds.{self.current_round}.{self.current_player}", default_value="0"))

    def back_home(self, inst):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

    # def write_on_file(self,entry):
    #     filename = '../assets/resources/points.json'
    #     with open(filename, "r+") as file:
    #         data = json.load(file)
    #         try:
    #             if data[len(data)-1]['id'] > 0:
    #                 entry.__setitem__('id', data[len(data)-1]['id'] + 1)
    #         except:
    #             entry.__setitem__('id', 1)
    #         data.append(entry)
    #         file.seek(0)
    #         json.dump(data, file)

    # def check_trophies(self, value):
    #     print([x for x in self.trophies if x["points"] == value])
