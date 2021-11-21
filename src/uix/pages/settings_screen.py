from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDSwitch


class SettingsScreen(MDScreen):

    sounds_on = False
    notifications_on = False
    theme_dark_on = False

    def toggle_sounds(self):
        self.sounds_on = not self.sounds_on

    def toggle_notifications(self):
        self.sounds_on = not self.notifications_on

    def toggle_dark_theme(self, app):
        self.theme_dark_on = not self.theme_dark_on
        app.theme_cls.theme_style = "Dark" if self.theme_dark_on else "Light"
    # switch_sound = None
    # switch_notify = None
    #
    # def on_enter(self):
    #     self.settings()
    #
    # def settings(self):
    #     if not self.switch_sound:
    #         self.switch_sound = MDSwitch(
    #             active=True,
    #         )
    #         self.switch_notify = MDSwitch(
    #             active=False
    #         )
    #     self.ids.sound.add_widget(self.switch_sound)
    #     self.ids.sound.add_widget(self.switch_notify)


