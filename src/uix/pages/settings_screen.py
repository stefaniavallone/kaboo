from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class TextTermsPolicy(BoxLayout):
    pass


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
        self.how_to_play_dialog = MDDialog(
            title=title,
            type="custom",
            text=text,
            radius=[20, 7, 20, 7]
        )
        self.how_to_play_dialog.open()

    def open_terms_and_policy_dialog(self):
        if not self.term_policy_dialog:
            self.term_policy_dialog = MDDialog(
                title="Terms & Policy:",
                type="custom",
                content_cls=TextTermsPolicy(),
                radius=[20, 7, 20, 7]
            )

        self.term_policy_dialog.open()

    def to_home(self):
        self.manager.go_to_screen('home', direction='right')

    def set_lang(self, lang):
        print("set", lang)
        self.app.status.setv("app.lang", lang)
        #self.canvas.before.clear()
        #with self.canvas.before:
        #    Color(0.5, 1, 0.5, 1)
        #    RoundedRectangle(pos=(self.pos[0] - dp(5), self.pos[1] - dp(5)),
        #                     size=(self.size[0] - dp(5), self.pos[1] - dp(5)),
        #                     radius=[dp(24), dp(24), dp(24), dp(24)])


