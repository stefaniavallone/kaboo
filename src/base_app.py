from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from app_status import AppStatus

from uix.pages.root import Root


class BaseApp(MDApp):
    def __init__(self, **kwargs):
        super(BaseApp, self).__init__(**kwargs)
        self.initialize_app()
        self.initialize_status()
    
    def initialize_app(app):
        Window.soft_input_mode = "below_target"
        app.title = "KTaboo"
        
        app.theme_cls.material_style = "M3"
        
        app.theme_cls.primary_palette = "Blue"
        app.theme_cls.primary_hue = "500"

        app.theme_cls.accent_palette = "Amber"
        app.theme_cls.accent_hue = "500"

        app.theme_cls.theme_style = "Light"

    def initialize_status(self):
        self.status = AppStatus()
    
    def go_to_screen(self, screen, direction="left"):
        self.manager.transition.direction = direction
        self.manager.current = screen

    def build(self):
        return Root()