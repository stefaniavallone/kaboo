from logic.trophies.action_trophy import ActionTrophy
from logic.trophies.game_level_trophy import GameLevelTrophy
from logic.trophies.points_trophy import PointsTrophy
from utils.translation.i18n import i18n


trophies = {
    "5 points": PointsTrophy(name="TROPHY_POINTS_TITLE",  # "5 points",
                             description="TROPHY_POINTS_DESC",  # "You scored 5 points",
                             image="assets/images/trophies/trophy_5points.png",
                             points=5),
    "25 points": PointsTrophy(name="TROPHY_POINTS_TITLE",  # "25 points",
                              description="TROPHY_POINTS_DESC",  # "You scored 25 points",
                              image="assets/images/trophies/trophy_25points.png",
                              points=25),
    "50 points": PointsTrophy(name="TROPHY_POINTS_TITLE",  # "50 points",
                              description="TROPHY_POINTS_DESC",  # "You scored 50 points",
                              image="assets/images/trophies/trophy_50points.png",
                              points=50),
    "250 points": PointsTrophy(name="TROPHY_POINTS_TITLE",  # "250 points",
                               description="TROPHY_POINTS_DESC",  # "You scored 250 points",
                               image="assets/images/trophies/trophy_250points.png",
                               points=250),
    "500 points": PointsTrophy(name="TROPHY_POINTS_TITLE",  # "500 points",
                               description="TROPHY_POINTS_DESC",  # "You scored 500 points",
                               image="assets/images/trophies/trophy_500points.png",
                               points=500),
    "5 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",  # "5 wrong answers",
                                    description="TROPHY_ANSWERS_DESC",  # "You wrong 5 answers",
                                    image="assets/images/trophies/trophy_5wrongs.png",
                                    action_type="wrong",
                                    action_count=5),
    "25 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",  # "25 wrong answers",
                                    description="TROPHY_ANSWERS_DESC",  # "You wrong 25 answers",
                                    image="assets/images/trophies/trophy_25wrongs.png",
                                    action_type="wrong",
                                    action_count=25),
    "50 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",  # "50 wrong answers",
                                     description="TROPHY_ANSWERS_DESC",  # "You wrong 50 answers",
                                     image="assets/images/trophies/trophy_50wrongs.png",
                                     action_type="wrong",
                                     action_count=50),
    "250 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",  # "250 wrong answers",
                                     description="TROPHY_ANSWERS_DESC",  # "You wrong 250 answers",
                                     image="assets/images/trophies/trophy_250wrongs.png",
                                     action_type="wrong",
                                     action_count=250),
    "500 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",  # "500 wrong answers",
                                     description="TROPHY_ANSWERS_DESC",  # "You wrong 500 answers",
                                     image="assets/images/trophies/trophy_500wrongs.png",
                                     action_type="wrong",
                                     action_count=500),
    "1 game Easy": GameLevelTrophy(name="TROPHY_GAME_LEVEL_TITLE",  # "1 game Easy",
                                   description="TROPHY_GAME_LEVEL_DESC",  # "You played 1 game with difficult \"Easy\"",
                                   image="assets/images/trophies/trophy_1easy.png",
                                   level="easy",
                                   level_count=1),
    "1 game Medium": GameLevelTrophy(name="TROPHY_GAME_LEVEL_TITLE",  # "1 game Medium",
                                     description="TROPHY_GAME_LEVEL_DESC",  # "You played 1 game with difficult \"Medium\"",
                                     image="assets/images/trophies/trophy_1medium.png",
                                     level="medium",
                                     level_count=1),
    "1 game Difficult": GameLevelTrophy(name="TROPHY_GAME_LEVEL_TITLE",  # "1 game Difficult",
                                        description="TROPHY_GAME_LEVEL_DESC",  # "You played 1 game with difficult \"Difficult\"",
                                        image="assets/images/trophies/trophy_1hard.png",
                                        level="hard",
                                        level_count=1),
    "5 games Easy": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",  # "5 games Easy",
                                    description="TROPHY_GAMES_LEVEL_DESC",  # "You played 5 games with difficult \"Easy\"",
                                    image="assets/images/trophies/trophy_5easy.png",
                                    level="easy",
                                    level_count=5),
    "5 games Medium": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",  # "5 game Medium",
                                      description="TROPHY_GAMES_LEVEL_DESC",  # "You played 5 games with difficult \"Medium\"",
                                      image="assets/images/trophies/trophy_5medium.png",
                                      level="medium",
                                      level_count=5),
    "5 games Difficult": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",  # "5 games Difficult",
                                         description="TROPHY_GAMES_LEVEL_DESC",  # "You played 5 games with difficult \"Difficult\"",
                                         image="assets/images/trophies/trophy_5hard.png",
                                         level="hard",
                                         level_count=5),
    "25 game Easy": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",  # "25 game Easy",
                                    description="TROPHY_GAMES_LEVEL_DESC",  # "You played 25 games with difficult \"Easy\"",
                                    image="assets/images/trophies/trophy_25easy.png",
                                    level="easy",
                                    level_count=25),
    "25 game Medium": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",  # "25 game Medium",
                                      description="TROPHY_GAMES_LEVEL_DESC",  # "You played 25 games with difficult \"Medium\"",
                                      image="assets/images/trophies/trophy_25medium.png",
                                      level="medium",
                                      level_count=25),
    "25 game Difficult": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",  # "25 game Difficult",
                                         description="TROPHY_GAMES_LEVEL_DESC",  # "You played 25 games with difficult \"Difficult\"",
                                         image="assets/images/trophies/trophy_25hard.png",
                                         level="hard",
                                         level_count=25)
}