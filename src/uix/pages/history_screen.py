import json

from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp


class Item(OneLineAvatarListItem):
    divider = None


class HistoryScreen(MDScreen):
    data_tables = None
    game_stats_dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.data_tables:
            with open("../assets/resources/points.json") as histories_file:
                self.histories = json.load(histories_file)

    def on_enter(self):
        self.load_data()

    def load_data(self):
        if not self.data_tables:
            self.data_tables = MDDataTable(
                use_pagination=False if len(self.histories) < 10 else True,
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                size_hint=(0.9, 0.6),
                rows_num=10,
                pagination_menu_pos="center",
                background_color=[1, 0, 0, .5],
                column_data=[
                    ("[color=#C042B8]N°[/color]", dp(5)),
                    ("[color=#C042B8]Day[/color]", dp(20)),
                    ("[color=#C042B8]Level[/color]", dp(15)),
                    ("[color=#C042B8]Players[/color]", dp(15))
                ],
                row_data=[
                    (
                        history['id'],
                        "[color=#297B50]" + history['day'] + "[/color]",
                        "[color=#6C9331]" + history['level'] + "[/color]",
                        "[color=#C552A1]" + str(history['players'][0]['num']) + "[/color]",
                    )
                    for history in self.histories
                ],
            )

            self.data_tables.bind(on_row_press=self.on_row_press)
            self.ids.container.add_widget(self.data_tables)

    def on_row_press(self, instance_table, instance_cell_row):
        index = instance_table.row_data[int(instance_cell_row.index/4)][0] - 1
        players = self.histories[index]["players"][0]

        items = [Item(text=f"Player {i+1}: [color=#C042B8]{players[f'player{i+1}']} points[/color]") for i in range(players["num"])]
        self.game_stats_dialog = MDDialog(
            title="Players Point",
            type="simple",
            items=items
        )
        self.game_stats_dialog.open()
