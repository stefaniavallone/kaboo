import json

from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem
from logic.game import PLAYERS_COLORS
from logic.score import best_player

class Item(OneLineAvatarListItem):
    divider = None

class HistoryScreen(MDScreen):
    def on_pre_enter(self, *args):
        with open("../assets/resources/points.json") as histories_file:
            self.histories = json.load(histories_file)

        table_data= list()
        for history in self.histories:
            winner, score = best_player(history['players_points'])
            color = PLAYERS_COLORS[int(winner[1])]
            table_data.append({'date': str(history['date']),
             'image': f'../assets/images/levels/{history["level"]}.png',
             'players': str(len(history['players_points'])),
             'winner': 'Team ' + str(int(winner[1]) + 1),
             'score': str(score),
             'players_points': history['players_points'],
             'details': self.show_details,
             'text_color': color
             })
        self.ids.table_floor.data = table_data

    def show_details(self, players_points, players, date):
        list_items = [Item(text=f" Player {i+1}: [color=#C042B8]{players_points[f'p{i}']} points[/color]") for i in range(int(players))]
        game_stats_dialog = MDDialog(
            title="Players Point",
            type="simple",
            text = "Date: "+ date,
            items=list_items,
            radius=[20, 7, 20, 7]
        )
        game_stats_dialog.open()
    
    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
