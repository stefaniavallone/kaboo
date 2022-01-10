import datetime

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("uix/components/kv/onboarding_item.kv")


class OnboardingItem(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.callback = None