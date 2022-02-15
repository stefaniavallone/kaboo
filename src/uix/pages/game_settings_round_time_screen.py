import datetime

from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.properties import ListProperty
from uix.base_components.kmd_fill_round_flat_button import \
    KMDFillRoundFlatButton


class GameSettingsRoundTimeScreen(MDScreen):
    buttons = ListProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.buttons = [
            KMDFillRoundFlatButton(text="0:30",
                                   radius=[dp(10), dp(10), dp(10), dp(10)],
                                   theme_text_color="Custom",
                                   width="100dp",
                                   size_hint=(None, None),
                                   on_release=self.set_round_time),
            KMDFillRoundFlatButton(text="1:00",
                                   radius=[dp(10), dp(10), dp(10), dp(10)],
                                   theme_text_color="Custom",
                                   width="100dp",
                                   size_hint=(None, None),
                                   on_release=self.set_round_time),
            KMDFillRoundFlatButton(text="3:00",
                                   radius=[dp(10), dp(10), dp(10), dp(10)],
                                   theme_text_color="Custom",
                                   width="100dp",
                                   size_hint=(None, None),
                                   on_release=self.set_round_time),
            KMDFillRoundFlatButton(text="5:00",
                                   radius=[dp(10), dp(10), dp(10), dp(10)],
                                   theme_text_color="Custom",
                                   width="100dp",
                                   size_hint=(None, None),
                                   on_release=self.set_round_time)
        ]

    def set_round_time(self, inst):
        m, s = inst.text.split(':')
        seconds = int(
            datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds())
        self.app.status.setv("game.round_time", seconds)
        self.app.status.setv("game.current_round", 0)
        self.manager.go_to_screen('game_pre', direction='left')
