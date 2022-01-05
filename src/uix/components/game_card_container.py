from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from src.uix.components.game_card import GameCard

Builder.load_file("uix/components/kv/game_card_container.kv")


class GameCardContainer(BoxLayout):

    def add_card(self, word, forbidden):
        gc = GameCard()
        gc.ids.word = word
        gc.ids.forbidden = forbidden
        self.ids.swiper.add_widget(gc)
        

