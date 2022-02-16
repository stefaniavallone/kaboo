from kivmob import TestIds
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.app import App

from logic.game import PLAYERS_COLORS


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
        self.points = str(self.app.status.getv(f"game.rounds.r{str(int(self.current_round)-1)}.p{str(curr_player)}.points", default_value="0"))
        self.current_player = f"Team {str(curr_player + 1)}"
        self.image = f"assets/images/pregame/your_turn_{str(curr_player)}.png"
        self.title = self.app.i18n._("PREGAME_TEAM_TURN", team=self.current_player) # f"It's {self.current_player} turn!"
        self.ids.play_button.md_bg_color = PLAYERS_COLORS[curr_player]

    def to_game(self):
        self.app.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.app.ads.request_interstitial()
        self.app.ads.show_interstitial()
        self.manager.go_to_screen('game', direction='left')

    def to_home(self):
        self.app.status.setv("game.current_player", 0)
        self.manager.go_to_screen('home', direction='right')

    def on_resume(self):
        self.app.ads.request_interstitial()