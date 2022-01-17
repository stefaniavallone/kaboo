from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.app import App
from src.uix.components.modal_scroll import ModalScroll
from kivy.uix.modalview import ModalView
from kivymd.uix.list import OneLineAvatarIconListItem

class SettingsScreen(MDScreen):
    term_policy_dialog = None
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

    def show_details(self):
        game_stats_dialog = MDDialog(
            title="HOW TO PLAY",
            type="simple",
            text = "Date: ",
            items="",
            size_hint= (0.7 , 1), 
            radius=[20, 7, 20, 7]
        )
        game_stats_dialog.open()
    
    def how_to_play(self, title, text):
        how_to_play_dialog = MDDialog(
            title=title,
            type="custom",
            text = text,
            size_hint= (0.7 , 1), 
            radius=[20, 7, 20, 7]
        )
        how_to_play_dialog.open()

    def infomations(self):
        if not self.term_policy_dialog:
            license = dict()
            license['0']= 'Freepik.com'
            dialog = ModalScroll(text= 'Term and Policy')
            dialog.add_item(license, OneLineAvatarIconListItem)
            self.term_policy_dialog = ModalView(size_hint=(0.7, 0.4),
                                                auto_dismiss=True,
                                                background_color=[0, 0, 0, 0])
            self.term_policy_dialog.add_widget(dialog)
        self.term_policy_dialog.open()

    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
