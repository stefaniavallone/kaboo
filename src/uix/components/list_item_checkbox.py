from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox


Builder.load_file("uix/components/kv/list_item_checkbox.kv")


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''