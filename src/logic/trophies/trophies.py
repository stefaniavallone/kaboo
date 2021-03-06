from logic.trophies.action_trophy import ActionTrophy
from logic.trophies.game_level_trophy import GameLevelTrophy
from logic.trophies.points_trophy import PointsTrophy


trophies = {
    "5 points": PointsTrophy(name="TROPHY_POINTS_TITLE",
                             description="TROPHY_POINTS_DESC",
                             image="assets/images/trophies/trophy_5points.png",
                             points=5),
    "25 points": PointsTrophy(name="TROPHY_POINTS_TITLE",
                              description="TROPHY_POINTS_DESC",
                              image="assets/images/trophies/trophy_25points.png",
                              points=25),
    "50 points": PointsTrophy(name="TROPHY_POINTS_TITLE",
                              description="TROPHY_POINTS_DESC",
                              image="assets/images/trophies/trophy_50points.png",
                              points=50),
    "250 points": PointsTrophy(name="TROPHY_POINTS_TITLE",
                               description="TROPHY_POINTS_DESC",
                               image="assets/images/trophies/trophy_250points.png",
                               points=250),
    "500 points": PointsTrophy(name="TROPHY_POINTS_TITLE",
                               description="TROPHY_POINTS_DESC",
                               image="assets/images/trophies/trophy_500points.png",
                               points=500),
    "5 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",
                                    description="TROPHY_ANSWERS_DESC",
                                    image="assets/images/trophies/trophy_5wrongs.png",
                                    action_type="wrong",
                                    action_count=5),
    "25 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",
                                    description="TROPHY_ANSWERS_DESC",
                                    image="assets/images/trophies/trophy_25wrongs.png",
                                    action_type="wrong",
                                    action_count=25),
    "50 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",
                                     description="TROPHY_ANSWERS_DESC",
                                     image="assets/images/trophies/trophy_50wrongs.png",
                                     action_type="wrong",
                                     action_count=50),
    "250 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",
                                     description="TROPHY_ANSWERS_DESC",
                                     image="assets/images/trophies/trophy_250wrongs.png",
                                     action_type="wrong",
                                     action_count=250),
    "500 wrong answers": ActionTrophy(name="TROPHY_ANSWERS_TITLE",
                                     description="TROPHY_ANSWERS_DESC",
                                     image="assets/images/trophies/trophy_500wrongs.png",
                                     action_type="wrong",
                                     action_count=500),
    "1 game Easy": GameLevelTrophy(name="TROPHY_GAME_LEVEL_TITLE",
                                   description="TROPHY_GAME_LEVEL_DESC",
                                   image="assets/images/trophies/trophy_1easy.png",
                                   level="easy",
                                   level_count=1),
    "1 game Medium": GameLevelTrophy(name="TROPHY_GAME_LEVEL_TITLE",
                                     description="TROPHY_GAME_LEVEL_DESC",
                                     image="assets/images/trophies/trophy_1medium.png",
                                     level="medium",
                                     level_count=1),
    "1 game Difficult": GameLevelTrophy(name="TROPHY_GAME_LEVEL_TITLE",
                                        description="TROPHY_GAME_LEVEL_DESC",
                                        image="assets/images/trophies/trophy_1hard.png",
                                        level="hard",
                                        level_count=1),
    "5 games Easy": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",
                                    description="TROPHY_GAMES_LEVEL_DESC",
                                    image="assets/images/trophies/trophy_5easy.png",
                                    level="easy",
                                    level_count=5),
    "5 games Medium": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",
                                      description="TROPHY_GAMES_LEVEL_DESC",
                                      image="assets/images/trophies/trophy_5medium.png",
                                      level="medium",
                                      level_count=5),
    "5 games Difficult": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",
                                         description="TROPHY_GAMES_LEVEL_DESC",
                                         image="assets/images/trophies/trophy_5hard.png",
                                         level="hard",
                                         level_count=5),
    "25 game Easy": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",
                                    description="TROPHY_GAMES_LEVEL_DESC",
                                    image="assets/images/trophies/trophy_25easy.png",
                                    level="easy",
                                    level_count=25),
    "25 game Medium": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",
                                      description="TROPHY_GAMES_LEVEL_DESC",
                                      image="assets/images/trophies/trophy_25medium.png",
                                      level="medium",
                                      level_count=25),
    "25 game Difficult": GameLevelTrophy(name="TROPHY_GAMES_LEVEL_TITLE",
                                         description="TROPHY_GAMES_LEVEL_DESC",
                                         image="assets/images/trophies/trophy_25hard.png",
                                         level="hard",
                                         level_count=25)
}