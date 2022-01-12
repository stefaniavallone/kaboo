import datetime
from kivymd.uix.screen import MDScreen
from app_status import AppStatus


class GameSettingsRoundTimeScreen(MDScreen):
    
    def set_round_time(self, value):
        m, s = value.split(':')
        seconds = int(datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds())
        AppStatus.setv("game.round_time", seconds)
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_pre'

