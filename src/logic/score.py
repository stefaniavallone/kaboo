import json
from datetime import datetime


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
    filename = 'assets/resources/points.json'
    with open(filename, "r") as file:
        data = json.load(file)
        game = {
            "level": level,
            "date": str(datetime.utcnow().date()),
            "rounds": json.loads(json.dumps(game_rounds, default=lambda s: vars(s))),
            "players_points": players_points
        }
        data.append(game)
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))
    return data
