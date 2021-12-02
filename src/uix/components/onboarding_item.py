import datetime

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("uix/components/kv/onboarding_item.kv")

class OnboardingItem(BoxLayout):
    info_game = {"num":'0',"jump":'0',"round":'0'}
    view_play_button = False

    def button_state(self, group, text):
        if group == 'round':
            date_time = datetime.datetime.strptime(text, "%M:%S")
            a_timedelta = date_time - datetime.datetime(1900, 1, 1)
            seconds = a_timedelta.total_seconds()
            self.info_game[group] = 20
        else:
            self.info_game[group] = text

    def update_callback(self):
        print("update_callback")

    def get_info_game(self):
        return self.info_game