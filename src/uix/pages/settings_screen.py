from kivymd.uix.screen import MDScreen
from app_status import AppStatus

class SettingsScreen(MDScreen):

    sounds_on = True
    theme_dark_on = False

    def toggle_sounds(self):
        self.sounds_on = not self.sounds_on
        AppStatus.set("game.sound", self.sounds_on)

    def toggle_dark_theme(self, app):
        self.theme_dark_on = not self.theme_dark_on
        app.theme_cls.theme_style = "Dark" if self.theme_dark_on else "Light"


    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
