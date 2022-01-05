import datetime

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
Builder.load_file("uix/components/kv/onboarding_item.kv")


class OnboardingItem(BoxLayout):
    info_game = {}
    colors_players = [[1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1]]
    view_play_button = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.callback = None

    def button_state(self, group, text):
        if group == 'round':
            date_time = datetime.datetime.strptime(text, "%M:%S")
            a_timedelta = date_time - datetime.datetime(1900, 1, 1)
            seconds = a_timedelta.total_seconds()
            self.info_game.__setitem__(group, seconds)
        elif group == 'num':
            players = []
            colors = []
            for i in range(1,int(text)+1):
                players.append("player" + str(i))
                colors.append(self.colors_players[i-1])
            self.info_game.__setitem__(group, players)
            self.info_game.__setitem__("color_player", colors)
        else:
            self.info_game.__setitem__(group, text)
