from kivy.lang import Builder
from kivymd.uix.card import MDCard

Builder.load_file("uix/base_components/kv/kmd_card.kv")


class KMDCard(MDCard):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
