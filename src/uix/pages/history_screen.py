import json

from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

class HistoryScreen(MDScreen):

    def on_pre_enter(self, *args):
        with open("../assets/resources/points.json") as histories_file:
            histories = json.load(histories_file)

        table_data = []
        table_data.append({'text':'Day','size_hint_y':None,'height':30,'color':'#C042B8'})
        table_data.append({'text':'Level','size_hint_y':None,'height':30,'color':'#C042B8'})
        # table_data.append({'text':'Players','size_hint_y':None,'height':30,'color':'#C042B8'})
        self.columns = len(table_data)
        column_titles = ['day', 'level']

        for history in histories:
            for y in column_titles:
                table_data.append({'text':history[y],'size_hint_y':None,'height':20,'bcolor':(.06,.25,.50,1)})

        self.ids.table_floor_layout.cols = self.columns #define value of cols to the value of self.columns
        self.ids.table_floor.data = table_data

    # def build(self):
    #     if not self.data_tables:
    #         self.data_tables = MDDataTable(
    #             use_pagination=False if len(self.histories) < 10 else True,
    #             pos_hint={'center_x': 0.5, 'center_y': 0.5},
    #             rows_num=10,
    #             pagination_menu_pos="center",
    #             # background_color=[1, 0, 0, .5],
    #             opacity=1,
    #             column_data=[
    #                 ("[color=#C042B8]N°[/color]", dp(5)),
    #                 ("[color=#C042B8]Day[/color]", dp(20)),
    #                 ("[color=#C042B8]Level[/color]", dp(15)),
    #                 ("[color=#C042B8]Players[/color]", dp(15))
    #             ],
    #             row_data=[
    #                 (
    #                     history['id'],
    #                     "[color=#297B50]" + history['day'] + "[/color]",
    #                     "[color=#6C9331]" + history['level'] + "[/color]",
    #                     "[color=#C552A1]" + str(history['players'][0]['num']) + "[/color]",
    #                 )
    #                 for history in self.histories
    #             ],
    #         )

            # self.data_tables.bind(on_row_press=self.on_row_press)
            # self.ids.container.add_widget(self.data_tables)

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
    
    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
