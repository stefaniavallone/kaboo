import datetime
from kivymd.uix.screen import MDScreen
from kivy.app import App
from src.uix.base_components.kmd_fill_round_flat_button import KMDFillRoundFlatButton
from kivy.properties import ListProperty

class GameSettingsRoundTimeScreen(MDScreen):
    buttons = ListProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.buttons= [
            KMDFillRoundFlatButton(text="0:20",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_round_time)),
            KMDFillRoundFlatButton(text="1:00",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_round_time)),
            KMDFillRoundFlatButton(text="3:00",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_round_time)),
            KMDFillRoundFlatButton(text="5:00",
                                    radius=[10, 10, 10, 10],
                                    theme_text_color= "Custom",
                                    width="100dp", 
                                    size_hint=(None, None),
                                    on_release=(self.set_round_time))
        ]


    def set_round_time(self, inst):
        m, s = inst.text.split(':')
        seconds = int(datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds())
        self.app.status.setv("game.round_time", seconds)
        self.manager.go_to_screen('game_pre', direction='left')

