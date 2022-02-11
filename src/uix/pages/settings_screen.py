from kivy.graphics import RoundedRectangle, Color
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.app import App

from uix.base_components.kmodal_view import KModalView
from uix.components.text_terms_policy import TextTermsPolicy
from uix.components.title_and_text_content import TitleAndTextContent


class SettingsScreen(MDScreen):
    term_policy_dialog = None
    how_to_play_dialog = None
    theme_dark_on = False

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()

    def on_pre_enter(self, *args):
        sounds_on = self.app.status.getv("game.sound", default_value=True)
        self.ids.sound_switch.active = sounds_on

    def toggle_sounds(self):
        self.app.status.setv("game.sound", self.ids.sound_switch.active)

    def toggle_dark_theme(self, app):
        self.theme_dark_on = not self.theme_dark_on
        app.theme_cls.theme_style = "Dark" if self.theme_dark_on else "Light"
    
    def open_how_to_play_dialog(self, title, text):
        self.how_to_play_dialog = KModalView(size_hint=(0.8, 0.6), auto_dismiss=True,
                                             content=TitleAndTextContent(title=title, text=text))
        self.how_to_play_dialog.open()

    def open_terms_and_policy_dialog(self):
        if not self.term_policy_dialog:
            self.term_policy_dialog = KModalView(
                                 size_hint=(0.8, 0.8), auto_dismiss=True,
                                 background_color=[0, 0, 0, 0], content=
                                 TextTermsPolicy())
        self.term_policy_dialog.open()

    def to_home(self):
        self.manager.go_to_screen('home', direction='right')

    def set_lang(self, lang, inst):
        self.app.status.setv("app.lang", lang)
        for button in self.ids.languages_container.children:
            if button == inst:
                with button.canvas.before:
                    Color(0.5, 0.5, 1, 1)
                    RoundedRectangle(
                        pos=(button.pos[0] - dp(5), button.pos[1] - dp(5)),
                        size=(button.size[0] + dp(10), button.size[1] + dp(10)),
                        radius=[dp(24), dp(24), dp(24), dp(24)])
            else:
                button.canvas.before.clear()



