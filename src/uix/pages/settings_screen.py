from kivy.properties import BooleanProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App


class SettingsScreen(MDScreen):
    sounds_on = True
    theme_dark_on = False

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.sounds_on = self.app.status.getv("game.sound", default_value=True)

    def on_pre_enter(self, *args):
        self.sounds_on = self.app.status.getv("game.sound", default_value=True)

    def toggle_sounds(self):
        self.sounds_on = not self.sounds_on
        self.app.status.setv("game.sound", self.sounds_on)

    def toggle_dark_theme(self, app):
        self.theme_dark_on = not self.theme_dark_on
        app.theme_cls.theme_style = "Dark" if self.theme_dark_on else "Light"

    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
