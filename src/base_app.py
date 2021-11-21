from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

from uix.pages.root import Root


def initialize_app(app):
    Window.soft_input_mode = "below_target"
    app.title = "KTaboo"

    app.theme_cls.primary_palette = "Blue"
    app.theme_cls.primary_hue = "500"

    app.theme_cls.accent_palette = "Amber"
    app.theme_cls.accent_hue = "500"

    app.theme_cls.theme_style = "Light"


class BaseApp(MDApp):
    def __init__(self, **kwargs):
        super(BaseApp, self).__init__(**kwargs)
        initialize_app(self)

    def build(self):
        return Root()