import json
from threading import Thread
from time import sleep
from kivy.app import App
from src.uix.components.game_history_content import GameHistoryContent

from uix.base_components.kmodal_view import KModalView
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty
from logic.game import PLAYERS_COLORS
from logic.score import best_player
from kivy.properties import BooleanProperty


class Item(OneLineAvatarListItem):
    name = StringProperty()
    divider = None


class HistoryScreen(MDScreen):
    show_details_dialog = None
    refreshing = BooleanProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.histories = []
    
    def on_pre_enter(self,  *args):
        Thread(target=self._refresh_data).start()

    def _refresh_data(self):
        self.refreshing = True
        sleep(2)
        with open("assets/resources/points.json") as histories_file:
            self.histories = json.load(histories_file)

        table_data = list()
        for history in self.histories:
            winner_index, score = best_player(history['players_points'])
            color = PLAYERS_COLORS[winner_index]
            table_data.append({'date': str(history['date']),
                               'image': f'assets/images/levels/{history["level"]}.png',
                               'players': str(len(history['players_points'])),
                               'winner': 'Team ' + str(winner_index + 1),
                               'score': str(score),
                               'players_points': history['players_points'],
                               'details': self.show_details,
                               'text_color': color
                               })
        self.ids.table_floor.data = table_data[::-1]
        self.refreshing = False

    def show_details(self, players_points, players, date):
        list_items = dict()
        for i in range(int(players)):
            list_items[f'Team {i + 1}'] = players_points[f'p{i}']
        details = GameHistoryContent(text=self.app.i18n._("HISTORY_DETAIL_TITLE", date=date)) #f'History of {date}')
        details.add_item(list_items)
        self.show_details_dialog = KModalView(size_hint=(0.7, 0.6),
                                              auto_dismiss=True,
                                              background_color=[0, 0, 0, 0],
                                              content=details)
        self.show_details_dialog.open()

    def to_home(self):
        self.manager.go_to_screen('home', direction='right')
