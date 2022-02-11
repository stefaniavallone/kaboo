from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.screen import MDScreen

from logic.game import PLAYERS_COLORS
from logic.score import compute_points, best_player, update_score_history, \
    get_score_history
from logic.trophies.trophies_checker import check_trophies, \
    compute_trophies_diff
from kivy.app import App

from uix.base_components.kmd_icon_button import KMDIconButton
from uix.base_components.kmodal_view import KModalView
from uix.components.trophy_content import TrophyContent


class GameEndScreen(MDScreen):
    round_time = StringProperty()
    num_players = StringProperty()
    num_jumps = StringProperty()
    game_level = StringProperty()
    winner = StringProperty()
    points = StringProperty()
    trophy_dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.applause_sound = self.app.sound_manager.get_sound(
            'assets/sounds/applause.wav')

    def on_pre_enter(self, *args):
        G = {'r0': {'p0': {'points': 0, 'actions': []}, 'p1': {'points': 6, 'actions': ['right', 'right', 'right', 'right', 'right', 'right']}}, 'r1': {'p0': {'points': 34, 'actions': ['jump', 'jump', 'jump', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']}, 'p1': {'points': 21, 'actions': ['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']}}}
        game_rounds = self.app.status.getv("game.rounds", default_value=G)

        self.round_time = str(self.app.status.getv("game.round_time", default_value=25))
        self.num_players = str(self.app.status.getv("game.num_players", default_value=2))
        self.num_jumps = str(self.app.status.getv("game.num_jumps", default_value=5))
        self.game_level = self.app.status.getv("game.level", default_value="easy")

        players_points = compute_points(game_rounds)
        best_player_index, score = best_player(players_points)
        self.ids.winner_card.md_bg_color = PLAYERS_COLORS[best_player_index]
        self.points = str(score)
        self.winner = self.app.i18n._("GAMEEND_TEAM_WINNER", team=f"Team {best_player_index + 1}").upper()  # f"Team {best_player_index} wins!"
        old_trophies = check_trophies(get_score_history())
        self.score_history = update_score_history(self.game_level, game_rounds, players_points)
        new_trophies = check_trophies(self.score_history)
        self.trophies_diff = compute_trophies_diff(old_trophies, new_trophies)
        self.applause_sound.play()

    def on_enter(self, *args):
        self.ids.confetti_rain.start()
        if len(self.trophies_diff) > 0:
            trophies_carousel = MDCarousel()
            buttons = []
            for name, trophy in self.trophies_diff.items():
                trophies_carousel.add_widget(TrophyContent(image=trophy["image"],
                                                           text=trophy["name"],
                                                           subtext=trophy["description"]))
            if len(self.trophies_diff) > 1:
                buttons = [
                    KMDIconButton(icon="chevron-left",
                                        _radius=dp(24),
                                        md_bg_color=[0.6, 0.6, 0.6, 1],
                                        on_release=lambda x: trophies_carousel.load_previous()),
                    KMDIconButton(icon="chevron-right",
                                               _radius=dp(24),
                                               md_bg_color=[0.6, 0.6, 0.6, 1],
                                               on_release=lambda x: trophies_carousel.load_next()),
                             ]
            self.trophies_won_view = KModalView(size_hint=(0.7, 0.4),
                          auto_dismiss=False, content=trophies_carousel,
                          buttons=buttons)
            self.trophies_won_view.open()

    def to_home(self, inst=None):
        self.manager.go_to_screen('home', direction='right')

    def on_pre_leave(self, *args):
        self.applause_sound.stop()

    def on_leave(self, *args):
        self.ids.confetti_rain.stop()