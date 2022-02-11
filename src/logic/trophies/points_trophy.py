from logic.trophies.abstract_trophy import AbstractTrophy


class PointsTrophy(AbstractTrophy):

    def __init__(self, name, description, image, points):
        super().__init__(name, description, image)
        self.points = points

    def check(self, games):
        points_sum = 0
        for game in games:
            game_rounds = game["rounds"]
            for r in list(game_rounds.keys()):
                round = game_rounds.get(r)
                for p in list(round.keys()):
                    points_sum = points_sum + round.get(p).get("points")
        if points_sum > self.points:
            return True
        return False