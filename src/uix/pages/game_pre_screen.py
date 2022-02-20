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
        self.round_time = str(self.app.status.getv("game.round_time"))
        self.num_players = str(self.app.status.getv("game.num_players"))
        self.num_jumps = str(self.app.status.getv("game.num_jumps"))
        self.game_level = self.app.status.getv("game.level")
        self.current_round = str(self.app.status.getv("game.current_round"))
        self.curr_player = self.app.status.getv("game.current_player")
        self.points = str(self.app.status.getv(f"game.rounds.r{str(int(self.current_round)-1)}.p{str(self.curr_player)}.points", default_value="0"))
        self.current_player = f"Team {str(self.curr_player + 1)}"
        self.image = f"assets/images/pregame/your_turn_{str(self.curr_player)}.png"
        self.title = self.app.i18n._("PREGAME_TEAM_TURN", team=self.current_player)
        self.ids.play_button.md_bg_color = PLAYERS_COLORS[self.curr_player]

    def to_game(self):
        if self.curr_player == 0:
            self.app.ads.request_interstitial()
            self.app.ads.show_interstitial()
        self.manager.go_to_screen('game', direction='left')

    def to_home(self):
        self.app.status.setv("game.current_player", 0)
        self.manager.go_to_screen('home', direction='right')

    def on_resume(self):
        if self.curr_player == 0:
            self.app.ads.request_interstitial()