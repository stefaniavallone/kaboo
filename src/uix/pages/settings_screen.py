from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.factory import Factory


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
            text="Date: ",
            items="",
            size_hint=(0.7, 1),
            radius=[20, 7, 20, 7]
        )
        game_stats_dialog.open()
    
    def how_to_play(self, title, text):
        how_to_play_dialog = MDDialog(
            title=title,
            type="custom",
            text=text,
            radius=[20, 7, 20, 7]
        )
        how_to_play_dialog.open()

    def informations(self):
        dialog = Factory.KDialog()
        dialog.ids.label_dialog.text ='\n[b][color=ff3333]SOUNDS[/color][/b]\n\n\
• Game Background music "ukulele.mp3" from "www.bensound.com" (Royalty Free Music)\n\n\
• Game ticking clock sound clock-ticking.mp3" from "www.fesliyanstudios.com" (Royalty Free Music)\n\n\
• Game sound "jump-notification.wav" from "www.tunetank.com" (Royalty Free Music)\n\n\
• Game sound "right-notification.wav" from "www.tunetank.com" (Royalty Free Music)\n\n\
• Game sound "wrong-notification.wav" from "www.tunetank.com" (Royalty Free Music)\n\n\
• Game sound "10 second applause" of Mike Koenig from "www.SoundBible.com" (Royalty Free Music)\n\n\n\
[b][color=ff3333]IMAGES[/color][/b]\n\n\
• It\'s you turn image from "https://www.freepik.com/vectors/people" People vector created by freepik - www.freepik.com\n\n\
• "Winner" image from "https://it.freepik.com/vettori/affari" Affari vettore creata da jcomp - it.freepik.com\n\n\
• "Trophies" icons and images from "https://www.flaticon.com/free-icons/trophy" title="trophy icons". Trophy icons created by Aficons studio - Flaticon\n\n\
• "Background" image from "https://www.freepik.com/vectors/background" Background vector created by starline - www.freepik.com\n\n\
• "Home Background" image from "https://www.freepik.com/photos/background" Background photo created by freepik - www.freepik.com\n\n\
• "Go home - Sad bear" icon from "https://www.flaticon.com/free-icons/sad" title="sad icons". Sad icons created by Smashicons - Flaticon</a>'
        dialog.open()

    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
