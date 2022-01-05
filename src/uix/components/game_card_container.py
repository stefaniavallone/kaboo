from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from uix.components.sw_card import SWCard

Builder.load_file("uix/components/kv/game_card_container.kv")


class GameCardContainer(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_card(self, word, forbidden):
        gc = SWCard()
        gc.ids.word.text = word
        gc.ids.forbidden.text = "\n".join(forbidden)
        self.ids.swiper.add_widget(gc)
        

