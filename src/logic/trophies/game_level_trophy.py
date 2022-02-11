from logic.trophies.abstract_trophy import AbstractTrophy


class GameLevelTrophy(AbstractTrophy):

    def __init__(self, name, description, image, level, level_count):
        super().__init__(name, description, image)
        self.level = level
        self.level_count = level_count

    def check(self, games):
        level_games_sum = len([g for g in games if g["level"] == self.level])
        if level_games_sum > self.level_count:
            return True
        return False
