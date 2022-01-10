from kivy.core.window import Window
from kivymd.app import MDApp
from app_status import AppStatus

from uix.pages.root import Root


class BaseApp(MDApp):
    def __init__(self, **kwargs):
        super(BaseApp, self).__init__(**kwargs)
        self.initialize_app()
        self.initialize_status()
    
    def initialize_app(self):
        Window.soft_input_mode = "below_target"
        self.title = "Kaboo"
        
        self.theme_cls.material_style = "M3"
        
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"
        self.font_name = "../assets/fonts/TheNautigal-Bold.ttf"

    def initialize_status(self):
        self.status = AppStatus()

    def build(self):
        from kivy.core.text import LabelBase
        from kivymd.font_definitions import theme_font_styles
        LabelBase.register(
            name="JetBrainsMono",
            fn_regular="../assets/fonts/TheNautigal-Bold.ttf")
        theme_font_styles.append('JetBrainsMono')
        self.theme_cls.font_styles["JetBrainsMono"] = [
            "JetBrainsMono",
            16,
            False,
            0.15,
            ]
        return Root()