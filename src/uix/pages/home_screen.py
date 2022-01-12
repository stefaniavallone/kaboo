import json
import webbrowser
from kivy.core.text import Label

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from app_status import AppStatus


class HomeScreen(MDScreen):
    HOME = True
    rate_us_dialog = None
    
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
        AppStatus.setv("game.level", text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_settings_num_players'

