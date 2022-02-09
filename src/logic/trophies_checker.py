import json

from utils.translation.i18n import i18n


class Trophy:

    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.obtained = False

    def check(self, games):
        raise NotImplementedError()

    def __repr__(self):
        return str(vars(self))


class PointsTrophy(Trophy):

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
            self.obtained = True


class ActionTrophy(Trophy):

    def __init__(self, name, description, image, action_type, action_count):
        super().__init__(name, description, image)
        self.action_type = action_type
        self.action_count = action_count

    def check(self, games):
        actions_sum = 0
        for game in games:
            game_rounds = game["rounds"]
            for r in list(game_rounds.keys()):
                round = game_rounds.get(r)
                for p in list(round.keys()):
                    type_actions = [a for a in round.get(p).get("actions")
                                    if a == self.action_type]
                    actions_sum = actions_sum + len(type_actions)
        if actions_sum > self.action_count:
            self.obtained = True


class GameLevelTrophy(Trophy):

    def __init__(self, name, description, image, level, level_count):
        super().__init__(name, description, image)
        self.level = level
        self.level_count = level_count

    def check(self, games):
        level_games_sum = len([g for g in games if g["level"] == self.level])
        if level_games_sum > self.level_count:
            self.obtained = True




trophies = {
    "5 points": PointsTrophy(name=i18n._("TROPHY_POINTS_TITLE", points=5),  # "5 points",
                             description=i18n._("TROPHY_POINTS_DESC", points=5),  #"You scored 5 points",
                             image="assets/images/trophies/trophy_5points.png",
                             points=5),
    "25 points": PointsTrophy(name="25 points",
                              description="You scored 25 points",
                              image="assets/images/trophies/trophy_25points.png",
                              points=25),
    "50 points": PointsTrophy(name="50 points",
                              description="You scored 50 points",
                              image="assets/images/trophies/trophy_50points.png",
                              points=50),
    "250 points": PointsTrophy(name="250 points",
                               description="You scored 250 points",
                               image="assets/images/trophies/trophy_250points.png",
                               points=250),
    "500 points": PointsTrophy(name="500 points",
                               description="You scored 500 points",
                               image="assets/images/trophies/trophy_500points.png",
                               points=500),
    "5 wrong answers": ActionTrophy(name=i18n._("TROPHY_ANSWERS_TITLE", answers=5), #"5 wrong answers",
                                    description=i18n._("TROPHY_ANSWERS_DESC", answers=5), #"You wrong 5 answers",
                                    image="assets/images/trophies/trophy_5wrongs.png",
                                    action_type="wrong",
                                    action_count=5),
    "25 wrong answers": ActionTrophy(name="25 wrong answers",
                                    description="You wrong 25 answers",
                                    image="assets/images/trophies/trophy_25wrongs.png",
                                    action_type="wrong",
                                    action_count=25),
    "50 wrong answers": ActionTrophy(name="50 wrong answers",
                                     description="You wrong 50 answers",
                                     image="assets/images/trophies/trophy_50wrongs.png",
                                     action_type="wrong",
                                     action_count=50),
    "250 wrong answers": ActionTrophy(name="250 wrong answers",
                                     description="You wrong 250 answers",
                                     image="assets/images/trophies/trophy_250wrongs.png",
                                     action_type="wrong",
                                     action_count=250),
    "500 wrong answers": ActionTrophy(name="500 wrong answers",
                                     description="You wrong 500 answers",
                                     image="assets/images/trophies/trophy_500wrongs.png",
                                     action_type="wrong",
                                     action_count=500),
    "1 game Easy": GameLevelTrophy(name=i18n._("TROPHY_GAME_LEVEL_TITLE", games=1, level="easy"), #"1 game Easy",
                                   description=i18n._("TROPHY_GAME_LEVEL_DESC", games=1, level="easy"),  # "You played 1 game with difficult \"Easy\"",
                                   image="assets/images/trophies/trophy_1easy.png",
                                   level="easy",
                                   level_count=1),
    "1 game Medium": GameLevelTrophy(name="1 game Medium",
                                     description="You played 1 game with difficult \"Medium\"",
                                     image="assets/images/trophies/trophy_1medium.png",
                                     level="medium",
                                     level_count=1),
    "1 game Difficult": GameLevelTrophy(name="1 game Difficult",
                                        description="You played 1 game with difficult \"Difficult\"",
                                        image="assets/images/trophies/trophy_1difficult.png",
                                        level="difficult",
                                        level_count=1),
    "5 games Easy": GameLevelTrophy(name=i18n._("TROPHY_GAMES_LEVEL_TITLE", games=5, level="easy"), #"5 games Easy",
                                    description=i18n._("TROPHY_GAMES_LEVEL_DESC", games=1, level="easy"),  #"You played 5 games with difficult \"Easy\"",
                                    image="assets/images/trophies/trophy_5easy.png",
                                    level="easy",
                                    level_count=5),
    "5 games Medium": GameLevelTrophy(name="1 game Medium",
                                      description="You played 5 games with difficult \"Medium\"",
                                      image="assets/images/trophies/trophy_5medium.png",
                                      level="medium",
                                      level_count=5),
    "5 games Difficult": GameLevelTrophy(name="5 games Difficult",
                                         description="You played 5 games with difficult \"Difficult\"",
                                         image="assets/images/trophies/trophy_5difficult.png",
                                         level="difficult",
                                         level_count=5),
    "25 game Easy": GameLevelTrophy(name="25 game Easy",
                                    description="You played 25 games with difficult \"Easy\"",
                                    image="assets/images/trophies/trophy_25easy.png",
                                    level="easy",
                                    level_count=25),
    "25 game Medium": GameLevelTrophy(name="25 game Medium",
                                      description="You played 25 games with difficult \"Medium\"",
                                      image="assets/images/trophies/trophy_25medium.png",
                                      level="medium",
                                      level_count=25),
    "25 game Difficult": GameLevelTrophy(name="25 game Difficult",
                                         description="You played 25 games with difficult \"Difficult\"",
                                         image="assets/images/trophies/trophy_25difficult.png",
                                         level="difficult",
                                         level_count=25),
}


# checker
def check_trophies(score_history):
    filename = 'assets/resources/trophies.json'
    with open(filename, "r") as file:
        saved_trophies = json.load(file)
    not_obtained_trophies_names = set(
        [t["name"] for t in saved_trophies if not t["obtained"]])
    for name, trophy in trophies.items():
        trophy.check(score_history)
    with open(filename, "w") as file:
        file.write(json.dumps([vars(t) for t in trophies.values()], indent=4))
    obtained_trophies_names = set(
        [t.name for t in trophies.values() if t.obtained])
    new_trophies_names = obtained_trophies_names.intersection(
        not_obtained_trophies_names)
    return {n: t for n, t in trophies.items() if n in new_trophies_names}
