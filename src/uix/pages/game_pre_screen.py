from kivymd.uix.screen import MDScreen
from src.app_status import AppStatus
from kivy.properties import StringProperty

class GamePreScreen(MDScreen):
    round_time = StringProperty()
    num_players = StringProperty()
    num_jumps = StringProperty()
    game_level = StringProperty()
    current_round = StringProperty()
    current_player = StringProperty()
    points = StringProperty()
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def on_pre_enter(self, *args):
        self.round_time = str(AppStatus.get("game.round_time", default_value="25"))
        self.num_players = str(AppStatus.get("game.num_players", default_value="2"))
        self.num_jumps = str(AppStatus.get("game.num_jumps", default_value="5"))
        self.game_level = AppStatus.get("game.level", default_value="easy")
        self.current_round = str(AppStatus.get("game.current_round", default_value="0"))
        self.current_player = "Players" + str(AppStatus.get("game.current_player", default_value="1"))
        self.points = str(AppStatus.get(f"game.rounds.{self.current_round}.{self.current_player}", default_value="0"))
    
    def to_game(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'

    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
    
    def reset(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'game_settings_num_players'