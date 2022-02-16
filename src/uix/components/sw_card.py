from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("uix/components/kv/sw_card.kv")


class SWCard(MDBoxLayout):

    text = StringProperty()
    forbidden = StringProperty()

    def __init__(self, text, forbidden, **kwargs):
        super().__init__(**kwargs)
        self.text = text.upper()
        self.forbidden = forbidden.upper()
