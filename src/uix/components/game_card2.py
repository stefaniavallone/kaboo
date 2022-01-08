from kivy.lang import Builder
from kivymd.uix.swiper import MDSwiperItem

Builder.load_file("uix/components/kv/game_card2.kv")


class GameCard2(MDSwiperItem):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


