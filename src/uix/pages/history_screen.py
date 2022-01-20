import json

from src.uix.components.modal_scroll import ModalScroll
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem, TwoLineListItem
from kivy.properties import StringProperty
from logic.game import PLAYERS_COLORS
from logic.score import best_player
from kivy.uix.modalview import ModalView


class Item(OneLineAvatarListItem):
    name = StringProperty()
    divider = None


class HistoryScreen(MDScreen):
    def on_pre_enter(self, *args):
        with open("../assets/resources/points.json") as histories_file:
            self.histories = json.load(histories_file)

        table_data = list()
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
        self.ids.table_floor.data = table_data[::-1]

    def show_details(self, players_points, players, date):
        list_items = dict()
        for i in range(int(players)):
            list_items[f'Team {i+1}'] = players_points[f'p{i}']
        self.dialog = ModalScroll(text=f'History of {date}')
        self.dialog.add_item(list_items, TwoLineListItem)
        
        self.confirm_exit_dialog = ModalView(size_hint=(0.7, 0.5),
                                             auto_dismiss=True,
                                             background_color=[0, 0, 0, 0])
        self.confirm_exit_dialog.add_widget(self.dialog)
        self.confirm_exit_dialog.open()
    
    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
