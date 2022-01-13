import datetime
from kivymd.uix.screen import MDScreen
from kivy.app import App


class GameSettingsRoundTimeScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()

    def set_round_time(self, value):
        m, s = value.split(':')
        seconds = int(datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds())
        self.app.status.setv("game.round_time", seconds)
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_pre'

