import json

from random import sample, randint
from string import ascii_lowercase

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen


class TrophiesScreen(MDScreen):
    def on_pre_enter(self):
        with open("../assets/resources/trophies.json") as trophies_file:
            trophies = json.load(trophies_file)
        self.ids.rv.data = [
            {'name.text': trophy['points'],
             'value': trophy['name'],
             'icon': trophy['icon']}
            for trophy in trophies]
            
    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
    # def sort(self):
    #     self.rv.data = sorted(self.rv.data, key=lambda x: x['name.text'])

    # def clear(self):
    #     self.rv.data = []

    # def insert(self, value):
    #     self.rv.data.insert(0, {
    #         'name.text': value or 'default value', 'value': 'unknown'})

    # def update(self, value):
    #     if self.rv.data:
    #         self.rv.data[0]['name.text'] = value or 'default new value'
    #         self.rv.refresh_from_data()

    # def remove(self):
    #     if self.rv.data:
    #         self.rv.data.pop(0)

