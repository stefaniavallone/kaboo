import json

from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen


class TrophiesScreen(MDScreen):
    trophies_list = None

    def on_enter(self):
        self.load_trophies()

    def load(self):
        with open("../assets/resources/trophies.json") as trophies_file:
            trophies = json.load(trophies_file)
        for trophy in trophies:
            self.root.ids.container.add_widget(
                OneLineAvatarIconListItem(text=trophy['points'])
            )



