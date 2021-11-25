import json
from random import randint

from kivymd.uix.screen import MDScreen

from uix.components.element_card import ElementCard


class GameScreen(MDScreen):
    level_game = "easy"
    time = ""
    game_card = None

    def on_enter(self, *args):
        self.load_game()

    def load_game(self):
        if self.level_game == 'easy':
            self.easy_game()
        elif self.level_game == 'medium':
            self.medium_game()
        else:
            self.hard_game()


    def easy_game(self):
        with open("../assets/resources/easy_game.json") as game_file:
            words = json.load(game_file)
        if not self.game_card:
            i = randint(1, 10)
            print(words[i]["word"])
            print(words[i]["forbidden"])

            self.game_card = ElementCard(
                size_hint=(0.80, 0.8),
                pos_hint={"center_x": 0.5, "center_y": 0.60},
                text=words[i]["word"],
                subtext=words[i]["forbidden"][0] + '\n' + words[i]["forbidden"][1] + '\n' + words[i]["forbidden"][2] + '\n' + words[i]["forbidden"][3] + '\n' + words[i]["forbidden"][4]
            )
            self.ids.container.add_widget(self.game_card)


    def medium_game(self):
        pass

    def hard_game(self):
        pass
