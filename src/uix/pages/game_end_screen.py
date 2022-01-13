from kivy.properties import StringProperty
from kivy.uix.modalview import ModalView
from kivymd.uix.screen import MDScreen

from logic.score import compute_points, best_player, update_score_history
from logic.trophies_checker import check_trophies
from uix.components.custom_modal import CustomModal
from kivy.app import App


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
    
    def on_pre_enter(self, *args):
        G = {'r0': {'p0': {'points': 0, 'actions': []}, 'p1': {'points': 6, 'actions': ['right', 'right', 'right', 'right', 'right', 'right']}}, 'r1': {'p0': {'points': 4, 'actions': ['jump', 'jump', 'jump', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']}, 'p1': {'points': 21, 'actions': ['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']}}}
        game_rounds = self.app.status.getv("game.rounds", default_value=G)

        self.round_time = str(self.app.status.getv("game.round_time", default_value=25))
        self.num_players = str(self.app.status.getv("game.num_players", default_value=2))
        self.num_jumps = str(self.app.status.getv("game.num_jumps", default_value=5))
        self.game_level = self.app.status.getv("game.level", default_value="easy")
        
        players_points = compute_points(game_rounds)
        best_player_index, score = best_player(players_points)
        self.points = str(score)
        self.winner = f"Team {best_player_index}"
        self.score_history = update_score_history(self.game_level, game_rounds, players_points)

    def on_enter(self, *args):
        new_trophies = check_trophies(self.score_history)
        self.trophies_list = new_trophies.values()
        for trophy in self.trophies_list:
            e = CustomModal()
            e._size_hint = (0.6, 0.3)
            e.text = trophy.name
            e.subtext = trophy.description
            e.image = trophy.image
            e.elevation = 0
            e.md_bg_color = (255/255, 241/255, 115/255, 1)
            #self.ids.trophy_carousel.add_widget(e)
        #animations.pop_up(self.ids.trophy_carousel)
        view = ModalView(size_hint=(0.7, 0.4),
                         auto_dismiss=True,
                         background_color=[0,0,0,0])
        view.add_widget(CustomModal(image="../assets/images/trophies/trophy_5points.png",
                                    text="asdasdsadsa", subtext="asdsadas",
                                    bg_color=(255 / 255, 241 / 255, 115 / 255, 1)))
        view.open()

    def back_home(self, inst=None):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

