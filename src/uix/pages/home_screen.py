import webbrowser

from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.app import App


class HomeScreen(MDScreen):
    HOME = True
    rate_us_dialog = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()

    def on_enter(self, *args):
        Clock.schedule_once(self.load_music)

    def load_music(self, *args):
        self.app_background_music = self.app.sound_manager.get_sound(
            "assets/sounds/cute.ogg", loop=True, volume=0.2)
        self.app_background_music.play(restart=False)

    def show_rate_us_dialog(self):
        if not self.rate_us_dialog:
            self.rate_us_dialog = MDDialog(
                text = self.app.i18n._("DIALOG_RATEUS"),  # "If you like this application, please give us five stars on Play Store!",
                radius=[20, 7, 20, 7],
                buttons=[
                    MDFlatButton(
                        text="Rate us",
                        theme_text_color="Custom",
                        on_release=self.go_to_play_store
                    ),
                ]
            )
        self.rate_us_dialog.open()

    def go_to_play_store(self, inst):
        webbrowser.open("market://details?id=org.kames.kaboo")
        self.rate_us_dialog.dismiss()

    def set_game_level(self, text):
        self.app.status.setv("game.level", text)
        self.manager.go_to_screen('game_settings_num_players')

