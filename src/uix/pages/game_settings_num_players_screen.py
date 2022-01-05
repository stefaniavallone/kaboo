from kivymd.uix.screen import MDScreen
from app_status import AppStatus


class GameSettingsNumPlayersScreen(MDScreen):
    
    def set_num_players(self, value):
        AppStatus.set("game.num_players", int(value))
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_settings_num_jumps'