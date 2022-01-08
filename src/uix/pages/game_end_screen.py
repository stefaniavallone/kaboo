import json

from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from src.app_status import AppStatus
from datetime import datetime
from uix.components.element_card import ElementCard


def compute_points(game_rounds):
    player_points = dict()
    for r in list(game_rounds.__dict__):
        round = getattr(game_rounds, r)
        for p in list(round.__dict__):
            player_points[p] = player_points.get(p, 0) + getattr(round, p).points
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
    # with open(filename, "w") as file:
    #     file.write(data)
    return data
    

class GameEndScreen(MDScreen):
    round_time = StringProperty()
    num_players = StringProperty()
    num_jumps = StringProperty()
    game_level = StringProperty()
    winner = StringProperty()
    points = StringProperty()
    
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def on_pre_enter(self, *args):
        game_rounds = AppStatus.get("game.rounds")
    
        self.round_time = str(AppStatus.get("game.round_time", default_value="25"))
        self.num_players = str(AppStatus.get("game.num_players", default_value=2))
        self.num_jumps = str(AppStatus.get("game.num_jumps", default_value="5"))
        self.game_level = AppStatus.get("game.level", default_value="easy")
        
        players_points = compute_points(game_rounds)
        best_player_index, score = best_player(players_points)
        self.points = str(score)
        self.winner = f"Team {best_player_index}"
        
        score_history = update_score_history(level, game_rounds, players_points)
        self.check_trophies(score_history)
        
        
    def check_trophies(self):
        pass
        #with open(filename, "r+") as file:
        #     data = json.load(file)

    def back_home(self, inst):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

  
    
    # def write_on_file(self,entry):
    #     filename = '../assets/resources/points.json'
    #     with open(filename, "r+") as file:
    #         data = json.load(file)
    #         try:
    #             if data[len(data)-1]['id'] > 0:
    #                 entry.__setitem__('id', data[len(data)-1]['id'] + 1)
    #         except:
    #             entry.__setitem__('id', 1)
    #         data.append(entry)
    #         file.seek(0)
    #         json.dump(data, file)

    # def check_trophies(self, value):
    #     print([x for x in self.trophies if x["points"] == value])
