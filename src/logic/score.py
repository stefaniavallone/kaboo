import json
from datetime import datetime

POINTS_FILENAME = 'assets/resources/points.json'


def compute_points(game_rounds):
    player_points = dict()
    for r in list(game_rounds.keys()):
        round = game_rounds.get(r)
        for p in list(round.keys()):
            player_points[p] = player_points.get(p, 0) + round.get(p)["points"]
    return player_points


def best_player(player_points):
    key = max(player_points, key=player_points.get)
    return int(key[1]), player_points[key]


def get_score_history():
    with open(POINTS_FILENAME, "r") as file:
        data = json.load(file)
    return data


def update_score_history(level, game_rounds, players_points):
    data = get_score_history()
    game = {
        "level": level,
        "date": str(datetime.utcnow().date()),
        "rounds": json.loads(
            json.dumps(game_rounds, default=lambda s: vars(s))),
        "players_points": players_points
    }
    data.append(game)
    with open(POINTS_FILENAME, "w") as file:
        file.write(json.dumps(data, indent=4))
    return data
