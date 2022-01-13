from kivymd.uix.screen import MDScreen
from kivy.app import App


class GameSettingsNumJumpsScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        
    def set_num_jumps(self, value):
        self.app.status.setv("game.num_jumps", int(value))
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_settings_round_time'