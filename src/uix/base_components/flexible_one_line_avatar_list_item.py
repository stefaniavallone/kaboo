from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import OptionProperty, StringProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.list import OneLineAvatarListItem, MDList

Builder.load_file("uix/base_components/kv/flexible_one_line_avatar_list_item.kv")
MDList
OneLineAvatarListItem
class FlexibleOneLineAvatarListItem(ThemableBehavior, RectangularRippleBehavior,
                                    ButtonBehavior,
                                    BoxLayout):
    text = StringProperty()
    icon = StringProperty()
    radius = ListProperty([dp(0), dp(0), dp(0), dp(0)])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"


