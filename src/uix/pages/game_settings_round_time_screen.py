from kivymd.uix.screen import MDScreen
from app_status import AppStatus


class GameSettingsRoundTimeScreen(MDScreen):
    
    def set_round_time(self, value):
        AppStatus.set("game.round_time", value)
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_pre'

