from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import MDGridLayout

from uix.components.sw_card import SWCard

Builder.load_file("uix/components/kv/game_resume.kv")


class GameResume(MDGridLayout):

    num_players = StringProperty()
    num_jumps = StringProperty()
    round_time = StringProperty()
    game_level = StringProperty()
    points = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(kwargs)
        

