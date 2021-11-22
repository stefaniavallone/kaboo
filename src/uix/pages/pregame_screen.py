
from kivy.factory import Factory
from kivy.uix.carousel import Carousel
from kivymd.uix.screen import MDScreen


class PreGameScreen(MDScreen):
    def on_enter(self):
        self.create_carousel()

    def create_carousel(self):

        for i in range(2):
            image = Factory.Label(text=str(i))
            self.ids.carousel.add_widget(image)




