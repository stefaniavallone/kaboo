from kivy.core.text import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

from uix.pages.root import Root


def initialize_app(app):
    Window.soft_input_mode = "below_target"
    app.title = "KTaboo"

    app.theme_cls.primary_palette = "Amber"
    app.theme_cls.primary_hue = "500"

    app.theme_cls.accent_palette = "Amber"
    app.theme_cls.accent_hue = "500"

    app.theme_cls.theme_style = "Dark"


class BaseApp(MDApp):
    def __init__(self, **kwargs):
        super(BaseApp, self).__init__(**kwargs)
        initialize_app(self)

    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen
