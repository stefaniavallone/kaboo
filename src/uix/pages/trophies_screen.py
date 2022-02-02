import json
from kivymd.uix.screen import MDScreen
from kivy.uix.modalview import ModalView
from uix.components.custom_modal import CustomModal


class TrophiesScreen(MDScreen):

    def on_pre_enter(self):
        with open("assets/resources/trophies.json") as trophies_file:
            self.trophies = json.load(trophies_file)

        list_trophies = list()

        for trophy in self.trophies:
            icon = "close-circle-multiple"
            if trophy['obtained']:
                icon = "checkbox-multiple-marked-circle"
            list_trophies.append({
                'name': trophy['name'],
                'description': trophy['description'],
                'image': trophy['image'],
                'icon': icon,
                'details': self.show_details})
        self.ids.list_trophies.data = list_trophies

    def show_details(self, name, description, image):
        self.view = ModalView(size_hint=(0.7, 0.4),
                         auto_dismiss=True,
                         background_color=[0,0,0,0])
        self.view.add_widget(CustomModal(image=image,
                                    text=name, subtext=description,
                                    on_close=self.cancel,
                                    bg_color=(255 / 255, 241 / 255, 115 / 255, 1)))
        self.view.open()

    def cancel(self, inst):
        self.view.dismiss()

    def to_home(self):
        self.manager.go_to_screen('home', direction='right')

