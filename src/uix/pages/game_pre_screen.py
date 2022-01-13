from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.app import App


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
        self.app = App.get_running_app()
    
    def on_pre_enter(self, *args):
        self.round_time = str(self.app.status.getv("game.round_time", default_value=25))
        self.num_players = str(self.app.status.getv("game.num_players", default_value=2))
        self.num_jumps = str(self.app.status.getv("game.num_jumps", default_value=5))
        self.game_level = self.app.status.getv("game.level", default_value="easy")
        self.current_round = str(self.app.status.getv("game.current_round", default_value=0))
        curr_player = self.app.status.getv("game.current_player", default_value=0)
        self.current_player = f"Team {str(curr_player + 1)}"
        self.points = str(self.app.status.getv(f"game.rounds.{str(self.current_round)}.{str(self.current_player)}", default_value="0"))
        self.image = f"../assets/images/pregame/your_turn_{str(curr_player)}.png"
        self.title = f"It's {self.current_player}'s turn!"

    def to_game(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'

    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
    
    def reset(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'game_settings_num_players'