from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

from uix.components.sw_card import SWCard

Builder.load_file("uix/components/kv/game_card_container.kv")


class GameCardContainer(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def reset_cards(self):
        self.ids.swiper.clear_widgets()

    def add_card(self, word, forbidden):
        gc = SWCard(text=word, forbidden="\n".join(forbidden))
        self.ids.swiper.add_widget(gc)

        #game_cards = self.ids.swiper.children
        #if len(game_cards) > 3:
        #    child = self.ids.swiper.children[0]
        #    self.ids.swiper.remove_widget(child)

    def next_card(self):
        self.ids.swiper.load_next()
