from kivymd.uix.screen import MDScreen
from app_status import AppStatus


class GameSettingsNumJumpsScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        
    def set_num_jumps(self, value):
        AppStatus.setv("game.num_jumps", int(value))
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_settings_round_time'