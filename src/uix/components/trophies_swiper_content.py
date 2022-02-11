from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("uix/components/kv/trophies_swiper_content.kv")


class TrophiesSwiperContent(MDBoxLayout):

    image = StringProperty()
    text = StringProperty()
    subtext = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
