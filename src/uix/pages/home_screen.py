import webbrowser

from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.app import App

from uix.base_components.kmd_fill_round_flat_button import \
    KMDFillRoundFlatButton
from uix.base_components.kmodal_view import KModalView
from uix.components.title_and_text_content import TitleAndTextContent


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
            self.rate_us_dialog = \
                KModalView(size_hint=(0.8, 0.3), auto_dismiss=True,
                           content=TitleAndTextContent(title=self.app.i18n._(
                                                           "RATEUS_DIALOG_TITLE"),
                                                       text=self.app.i18n._(
                                                           "RATEUS_DIALOG_DESC")),
                           buttons=[
                               KMDFillRoundFlatButton(
                                   text=self.app.i18n._(
                                       "RATEUS_BUTTON"),
                                   # "Rate us",
                                   radius=[dp(10), dp(10), dp(10), dp(10)],
                                   md_bg_color=(0, 0.2, 0.9, 1),
                                   on_release=self.go_to_play_store
                               ),
                           ])

        self.rate_us_dialog.open()

    def go_to_play_store(self, inst):
        webbrowser.open("market://details?id=org.kames.kaboo")
        self.rate_us_dialog.dismiss()

    def set_game_level(self, text):
        self.app.status.setv("game.level", text)
        self.manager.go_to_screen('game_settings_num_players')
