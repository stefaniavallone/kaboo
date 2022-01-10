import json


from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen


class TrophiesScreen(MDScreen):
    def on_pre_enter(self):
        with open("../assets/resources/trophies.json") as trophies_file:
            trophies = json.load(trophies_file)
        self.ids.list_trophies.data = [
            {'name': trophy['name'],
             'description': trophy['description'],
             'obtained': trophy['obtained']}
            for trophy in trophies]
            
    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'