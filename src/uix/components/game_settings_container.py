from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Clock
from kivy.properties import  ListProperty


Builder.load_file("uix/components/kv/game_settings_container.kv")


class GameSettingsContainer(BoxLayout):
    buttons = ListProperty()

    def __init__(self, buttons=[], **kwargs):
        super().__init__(**kwargs)
        self.buttons = buttons
        Clock.schedule_once(self._late_init)
    
    def _late_init(self, inst):
        for button in self.buttons:
            self.ids.buttons_container.add_widget(button)

    
