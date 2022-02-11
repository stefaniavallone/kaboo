from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.properties import ListProperty
from uix.base_components.kmd_fill_round_flat_button import KMDFillRoundFlatButton


class GameSettingsNumJumpsScreen(MDScreen):
    buttons = ListProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.buttons= [
            KMDFillRoundFlatButton(text="0",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_jumps)),
            KMDFillRoundFlatButton(text="3",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_jumps)),
            KMDFillRoundFlatButton(text="5",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_jumps)),
            KMDFillRoundFlatButton(text="10",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_jumps))
        ]

        
    def set_num_jumps(self, inst):
        self.app.status.setv("game.num_jumps", int(inst.text))
        self.manager.go_to_screen('game_settings_round_time', direction='left')