import cProfile

from kivmob import KivMob
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.app import MDApp
from app_status import AppStatus

from uix.pages.root import Root
from utils.sound.sound_manager import SoundManager
from utils.translation.i18n import i18n


class BaseApp(MDApp):

    def __init__(self, **kwargs):
        super(BaseApp, self).__init__(**kwargs)
        self.initialize_app()
        self.ads = KivMob("ca-app-pub-5506785496629412~2619392502")
        self.ads.new_interstitial("ca-app-pub-5506785496629412/2803225337")
        self.status = AppStatus()
        self.sound_manager = SoundManager()
        self.i18n = i18n
        self.status.attach(self.sound_manager)
        self.status.attach(self.i18n)
        self.status.setv("app.lang", "en")

    def initialize_app(self):
        Window.soft_input_mode = "below_target"
        fonts_path = "assets/fonts/Montserrat/"
        font_name = "Montserrat"
        self.title = "Kaboo"
        self._set_theme()
        self._set_font(fonts_path, font_name)

    def _set_theme(self):
        self.theme_cls.material_style = "M3"

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.success_color = (8/255, 153/255, 17/255, 1)
        self.theme_cls.theme_style = "Light"

    def _set_font(self, fonts_path, font_name):
        fonts = [
            {
                "name": f"{font_name}",
                "fn_regular": fonts_path + f"{font_name}-Regular.ttf",
                "fn_bold": fonts_path + f"{font_name}-Bold.ttf",
            },
            {
                "name": f"{font_name}Light",
                "fn_regular": fonts_path + f"{font_name}-Light.ttf",
            },
            {
                "name": f"{font_name}Medium",
                "fn_regular": fonts_path + f"{font_name}-Medium.ttf",
            },
        ]
        for font in fonts:
            LabelBase.register(**font)
        for name, style in self.theme_cls.font_styles.items():
            if style[0].endswith("Light"):
                style[0] = f"{font_name}Light"
            elif style[0].endswith("Medium"):
                style[0] = f"{font_name}Medium"
            elif style[0] != "Icons":
                style[0] = f"{font_name}"

    def build(self):
        return Root()
