from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp


class HistoryScreen(MDScreen):
    data_tables = None
    def on_enter(self):
        self.load_data()

    def load_data(self):
        if not self.data_tables:
            self.data_tables = MDDataTable(
                #background_color_header=get_color_from_hex("#65275d"),
                #background_color_cell=get_color_from_hex("#451938"),
                use_pagination = True,
                column_data=[
                    ("No.", dp(15)),
                    ("Column 1", dp(15)),
                    ("[color=#52251B]Column 2[/color]", dp(15)),
                    ("Column 3", dp(15))
                ],
                row_data=[
                    (
                        f"{i + 1}",
                        "[color=#297B50]1[/color]",
                        "[color=#C552A1]2[/color]",
                        "[color=#6C9331]3[/color]"
                    )
                    for i in range(50)
                ],
            )
            self.ids.container.add_widget(self.data_tables)


