from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.gridlayout import MDGridLayout

Builder.load_file("uix/components/kv/game_resume.kv")


class GameResume(MDGridLayout):

    num_players = StringProperty()
    num_jumps = StringProperty()
    round_time = StringProperty()
    game_level = StringProperty()
    points = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        

