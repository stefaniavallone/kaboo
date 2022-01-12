from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.swiper import MDSwiperItem

Builder.load_file("uix/components/kv/sw_card.kv")


class SWCard(MDSwiperItem):

    text = StringProperty()
    forbidden = StringProperty()

    def __init__(self, text, forbidden, **kwargs):
        super().__init__(**kwargs)
        self.text = text.upper()
        self.forbidden = forbidden.upper()
