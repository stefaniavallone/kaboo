from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list import ILeftBodyTouch, IRightBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.label import MDIcon, MDLabel

Builder.load_file("uix/components/kv/history_item.kv")


class HistoryItem(TwoLineAvatarIconListItem):
    image = StringProperty()
    score = StringProperty()

class LabelRight(IRightBodyTouch, MDLabel):
    '''Custom right container.'''

class ImageLeft(ILeftBodyTouch, MDIcon):
    '''Custom right container.'''