from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.label import MDIcon
from kivymd.uix.list import ILeftBodyTouch, IRightBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox


Builder.load_file("uix/components/kv/list_item_checkbox.kv")


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    image = StringProperty()
    obtained = BooleanProperty()


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class ImageLeft(ILeftBodyTouch, MDIcon):
    '''Custom right container.'''