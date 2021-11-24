from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivymd.theming import ThemableBehavior


class ItemCircles(ThemableBehavior, Widget):
    _circles_color = ListProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
