from kivy.properties import get_color_from_hex, ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp

class HistoryScreen(MDScreen):
    container = ObjectProperty(None)
    def on_enter(self):
        self.load_data()

    def load_data(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            background_color_header=get_color_from_hex("#65275d"),
            background_color_cell=get_color_from_hex("#451938"),
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("[color=#52251B]Column 2[/color]", dp(30)),
                ("Column 3", dp(30)),
                ("[size=24][color=#C042B8]Column 4[/color][/size]", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data=[
                (
                    f"{i + 1}",
                    "[color=#297B50]1[/color]",
                    "[color=#C552A1]2[/color]",
                    "[color=#6C9331]3[/color]",
                    "4",
                    "5",
                )
                for i in range(50)
            ],
        )
        layout.add_widget(data_tables)
        self.container.add_widget(layout)
        return layout


