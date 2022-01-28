import webbrowser

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
        self.app_background_music = self.app.sound_manager.get_sound("assets/sounds/cute.ogg", loop=True, volume=0.2)

    def on_pre_enter(self, *args):
        self.app_background_music.play(restart=False)

    def show_rate_us_dialog(self):
        if not self.rate_us_dialog:
            self.rate_us_dialog = MDDialog(
                text="If you like this application, please give us five stars on Play Store!",
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
        webbrowser.open("market://details?id=com.amazon.mp3")
        self.rate_us_dialog.dismiss()

    def set_game_level(self, text):
        self.app.status.setv("game.level", text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_settings_num_players'

