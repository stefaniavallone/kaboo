from kivymd.uix.screen import MDScreen



class SettingsScreen(MDScreen):

    sounds_on = False
    notifications_on = False
    theme_dark_on = True

    def toggle_sounds(self):
        self.sounds_on = not self.sounds_on

    def toggle_notifications(self):
        self.sounds_on = not self.notifications_on

    def toggle_dark_theme(self, app):
        self.theme_dark_on = not self.theme_dark_on
        app.theme_cls.theme_style = "Dark" if self.theme_dark_on else "Light"



