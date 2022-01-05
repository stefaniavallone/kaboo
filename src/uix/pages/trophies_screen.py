import json

from kivymd.uix.screen import MDScreen

from uix.components.list_item_checkbox import ListItemWithCheckbox


class TrophiesScreen(MDScreen):
    trophies_list = None
    
    def on_enter(self):
        self.load_trophies()

    def load_trophies(self):
        if not self.trophies_list:
            with open("../assets/resources/trophies.json") as trophies_file:
                trophies = json.load(trophies_file)
            for trophy in trophies:
                self.trophies_list = ListItemWithCheckbox(text=trophy['points'],
                                     secondary_text=trophy['name'],
                                     icon=trophy['icon'])

                self.ids.trophies_list.add_widget(self.trophies_list)
