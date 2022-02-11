from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineListItem

Builder.load_file("uix/components/kv/game_history_content.kv")


class GameHistoryContent(MDBoxLayout):

    text = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)

    def add_item(self, elements):
        for key, value in elements.items():
            self.ids.item_list.add_widget(
                TwoLineListItem(text=f'{key}', secondary_text=str(value))
            )
