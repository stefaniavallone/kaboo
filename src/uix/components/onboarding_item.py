from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("uix/components/kv/onboarding_item.kv")

class OnboardingItem(BoxLayout):
    num_choise = ""
    num_jump = ""
    num_round = ""

    def button_state(self, group, text):
        if group == 'num':
            self.num_choise = text
            print(self.num_choise)
        elif group == 'jump':
            self.num_jump = text
            print(self.num_jump)
        else:
            self.num_round = text
            print(self.num_round)