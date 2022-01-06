import json

from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from src.app_status import AppStatus

from uix.components.element_card import ElementCard


class GameEndScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def on_pre_enter(self, *args):
        # compute points
        # save results
        pass

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
