from kivymd.uix.dialog import MDDialog
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

    def show_details(self):
        game_stats_dialog = MDDialog(
            title="HOW TO PLAY",
            type="simple",
            text = "Date: ",
            items="",
            radius=[20, 7, 20, 7]
        )
        game_stats_dialog.open()
    
    def how_to_play(self, title, text):
        how_to_play_dialog = MDDialog(
            title=title,
            type="custom",
            text = text,
            radius=[20, 7, 20, 7]
        )
        how_to_play_dialog.open()


    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
