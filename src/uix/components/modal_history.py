from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_file("uix/components/kv/modal_history.kv")


class Item(OneLineAvatarListItem):
            divider = None


class ModalHistory(MDRelativeLayout):

    text_date = StringProperty()
    subtext_date = StringProperty()
    text_player = StringProperty()
    subtext_player = StringProperty()
        # text_jump = StringProperty()
    # subtext_jump = StringProperty()
    # text_wrong = StringProperty()
    # subtext_wrong = StringProperty()
    # text_winner = StringProperty()
    # subtext_winner = StringProperty()