from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDSwitch


class SettingsScreen(MDScreen):
    switch_sound = None
    switch_notify = None
    def on_enter(self):
        self.settings()

    def settings(self):
        if not self.switch_sound:
            self.switch_sound = MDSwitch(
                active=True,
            )
            self.switch_notify = MDSwitch(
                active=False
            )
        self.ids.sound.add_widget(self.switch_sound)
        self.ids.sound.add_widget(self.switch_notify)


