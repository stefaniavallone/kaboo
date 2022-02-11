from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.properties import ListProperty
from uix.base_components.kmd_fill_round_flat_button import KMDFillRoundFlatButton


class GameSettingsNumPlayersScreen(MDScreen):
    buttons = ListProperty()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.buttons= [
            KMDFillRoundFlatButton(text="2",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_players)),
            KMDFillRoundFlatButton(text="3",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_players)),
            KMDFillRoundFlatButton(text="4",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_players)),
            KMDFillRoundFlatButton(text="5",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_num_players))
        ]

    def set_num_players(self, inst):
        self.app.status.setv("game.num_players", int(inst.text))
        self.manager.go_to_screen('game_settings_num_jumps', direction='left')