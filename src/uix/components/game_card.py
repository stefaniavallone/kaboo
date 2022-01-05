from kivy.lang import Builder
from kivymd.uix.swiper import MDSwiperItem

Builder.load_file("uix/components/kv/game_card.kv")


class GameCard(MDSwiperItem):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


