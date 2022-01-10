import json

from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from src.app_status import AppStatus
from datetime import datetime
from uix.components.element_card import ElementCard
from utils.animations import Animations
from utils.trophies_checker import trophies


def compute_points(game_rounds):
    player_points = dict()
    for r in list(game_rounds.keys()):
        round = game_rounds.get(r)
        for p in list(round.keys()):
            player_points[p] = player_points.get(p, 0) + round.get(p)["points"]
    return player_points


def best_player(player_points):
    index = max(player_points, key=player_points.get)
    return index, player_points[index]


def update_score_history(level, game_rounds, players_points):
    filename = '../assets/resources/points.json'
    with open(filename, "r") as file:
        data = json.load(file)
        game = {
            "level": level,
            "date": str(datetime.utcnow().date()),
            "rounds": json.loads(json.dumps(game_rounds, default=lambda s: vars(s))),
            "players_points": players_points
        }
        data.append(game)
    #with open(filename, "w") as file:
    #    file.write(json.dumps(data, indent=4))
    return data


def check_trophies(score_history):
    filename = '../assets/resources/trophies.json'
    with open(filename, "r") as file:
        saved_trophies = json.load(file)
    not_obtained_trophies_names = set([t["name"] for t in saved_trophies if not t["obtained"]])
    for name, trophy in trophies.items():
        trophy.check(score_history)
    with open(filename, "w") as file:
        file.write(json.dumps([vars(t) for t in trophies.values()], indent=4))
    obtained_trophies_names = set([t.name for t in trophies.values() if t.obtained])
    new_trophies_names = obtained_trophies_names.intersection(not_obtained_trophies_names)
    return { n: t for n, t in trophies.items() if n in new_trophies_names }


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
    
    def on_pre_enter(self, *args):
        G = {'r0': {'p0': {'points': 0, 'actions': []}, 'p1': {'points': 6, 'actions': ['right', 'right', 'right', 'right', 'right', 'right']}}, 'r1': {'p0': {'points': 4, 'actions': ['jump', 'jump', 'jump', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'wrong', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']}, 'p1': {'points': 21, 'actions': ['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']}}}
        game_rounds = AppStatus.get("game.rounds", default_value=G)

        self.round_time = str(AppStatus.get("game.round_time", default_value=25))
        self.num_players = str(AppStatus.get("game.num_players", default_value=2))
        self.num_jumps = str(AppStatus.get("game.num_jumps", default_value=5))
        self.game_level = AppStatus.get("game.level", default_value="easy")
        
        players_points = compute_points(game_rounds)
        best_player_index, score = best_player(players_points)
        self.points = str(score)
        self.winner = f"Team {best_player_index}"
        self.score_history = update_score_history(self.game_level, game_rounds, players_points)

    def on_enter(self, *args):
        new_trophies = check_trophies(self.score_history)
        self.trophies_list = new_trophies.values()
        for trophy in self.trophies_list:
            e = ElementCard()
            e.text = trophy.name
            e.subtext = trophy.description
            e.image = trophy.image
            e.elevation=0
            e.md_bg_color = (255/255, 241/255, 115/255, 1)
            self.ids.trophy_carousel.add_widget(e)
        Animations.pop_up(self.ids.trophy_carousel)
        # layout.add_widget(trophy_carousel)
        # if not self.trophy_dialog:
        #     self.trophy_dialog = MDDialog(
        #         type="custom",
        #         radius=[20, 7, 20, 7],
        #         size_hint=(None, None),
        #         width=self.width * 0.8,
        #         height=self.height * 0.6,
        #         content_cls=layout
        #     )
        # self.trophy_dialog.open()
        # self.counter = 0
        # if len(self.trophies_list) > 0:
        #     self.make_dialog(self.trophies_list[self.counter])

    # def make_dialog(self, trophy):
    #
    #     if self.trophy_dialog:
    #         self.trophy_dialog.dismiss()
    #         self.counter = self.counter + 1
    #     if self.counter < len(self.trophies_list) - 1:
    #         if not self.trophy_dialog:
    #             self.trophy_dialog = MDDialog(
    #                 text=trophy.name,
    #                 radius=[20, 7, 20, 7],
    #                 size_hint=(.7, .6),
    #                 buttons=[
    #                     MDFlatButton(text="ok", on_release=lambda inst: self.make_dialog(self.make_dialog(self.trophies_list[self.counter])))
    #                 ]
    #             )
    #         else:
    #             self.trophy_dialog.text=trophy.name
    #
    #         self.trophy_dialog.open()

    def back_home(self, inst=None):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

