import webbrowser
from kivy.lang import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.properties import ObjectProperty, StringProperty
Builder.load_file("uix/components/kv/modal_scroll.kv")


class ModalScroll(MDRelativeLayout):
    item_list = ObjectProperty()
    text = StringProperty()

    def add_item(self, elements, type):
        for key, value in elements.items():
            if type == OneLineAvatarIconListItem:
                self.ids.item_list.add_widget(
                    type(text=f'{value}'
                    )
                )
            else:
                self.ids.item_list.add_widget(
                    type(text=f'{key}',
                        secondary_text=str(value)
                    )
                )