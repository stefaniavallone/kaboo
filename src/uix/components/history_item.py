from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import ILeftBodyTouch, IRightBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.label import MDIcon, MDLabel

Builder.load_file("uix/components/kv/history_item.kv")


class HistoryItem(TwoLineAvatarIconListItem, RecycleKVIDsDataViewBehavior,
                  MDBoxLayout):
    winner = StringProperty()
    date = StringProperty()
    image = StringProperty()
    score = StringProperty()


class LeftImage(ILeftBodyTouch, MDIcon):
    '''Custom left container.'''


class RightLabel(IRightBodyTouch, MDLabel):
    '''Custom right container.'''


