import json

from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from src.app_status import AppStatus

from uix.components.element_card import ElementCard


class GameEndScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
 
    # def end_game(self, entry, subtext):
    #     Clock.unschedule(self.interval_clock)
    #     self.write_on_file(entry)
    #     self.ids.container.clear_widgets()
    #     points = [int(s) for s in subtext.split() if s.isdigit()]

    #     end = ElementCard(
    #         image="../assets/images/the_end.png",
    #         text="Winner is ",
    #         subtext=subtext,
    #         on_release=self.back_home
    #     )
    #     self.ids.end_game.add_widget(end)

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
