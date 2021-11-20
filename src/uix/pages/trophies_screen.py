import json

from kivymd.uix.list import OneLineAvatarIconListItem, ImageLeftWidget
from kivymd.uix.screen import MDScreen


class TrophiesScreen(MDScreen):
    trophies_list = None
    def on_enter(self):
        self.load()

    def load(self):
        with open("./src/utils/trophies.json") as trophies_file:
            self.trophies = json.load(trophies_file)
        for trophy in self.trophies:
            print(trophy['points'])
            if not self.trophies_list:
                self.trophies_list = OneLineAvatarIconListItem(
                    text=trophy['points'],
                )
                self.ids.scroll.add_widget(self.trophies_list)



