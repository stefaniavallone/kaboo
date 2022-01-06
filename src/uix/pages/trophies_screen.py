import json

from kivymd.uix.screen import MDScreen
from app_status import AppStatus

from uix.components.list_item_checkbox import ListItemWithCheckbox


class TrophiesScreen(MDScreen):
    trophies_list = None

    def on_pre_enter(self):
        with open("../assets/resources/trophies.json") as trophies_file:
            trophies = json.load(trophies_file)
        AppStatus.set("trophy.trophies", trophies)

    def on_enter(self, *args): 
        trophies = AppStatus.get("trophy.trophies", default_value=dict())
        for trophy in trophies:
                self.trophies_list = ListItemWithCheckbox(text=trophy['points'],
                                     secondary_text=trophy['name'],
                                     icon=trophy['icon'])

                self.ids.trophies_list.add_widget(self.trophies_list)

    
    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

