from threading import Thread
from time import sleep
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen

from logic.score import get_score_history
from logic.trophies.trophies_checker import check_trophies
from uix.base_components.kmodal_view import KModalView
from uix.components.trophy_content import TrophyContent
from kivy.properties import BooleanProperty


class TrophiesScreen(MDScreen):
    refreshing = BooleanProperty()

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self):
        pass
        #if not self.refreshing:
        #    return
        #Thread(target=self._load_data).start()

    def on_enter(self, *args):
        Clock.schedule_once(self._load_data)

    def _load_data(self, delay=0):
        for i in range(1000000):
            print(i)
        self.refreshing = True
        list_trophies = list()
        score_history = get_score_history()
        checked_trophies = check_trophies(score_history)
        for _, trophy in checked_trophies.items():
            list_trophies.append({
                'name': trophy["name"],
                'description': trophy["description"],
                'image': trophy["image"],
                'icon': "checkbox-multiple-marked-circle" if trophy["obtained"] else "",
                'details': self.show_details})
        self.ids.list_trophies.data = list_trophies
        self.refreshing = False

    def show_details(self, name, description, image):
        self.kmodal = KModalView(size_hint=(0.7, 0.4), auto_dismiss=True,
                                 background_color=[0, 0, 0, 0], content=
                                 TrophyContent(image=image,
                                    text=name, subtext=description))
        self.kmodal.open()

    def to_home(self):
        self.manager.go_to_screen('home', direction='right')

