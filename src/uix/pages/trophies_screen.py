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
        #Clock.schedule_once(self._load_data)
        if not self.refreshing:
            return
        Thread(target=self._refresh_data).start()

    def _refresh_data(self):
        self.refreshing = True
        sleep(2)
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
        #self.view = ModalView(size_hint=(0.7, 0.4),
        #                 auto_dismiss=True,
        #                 background_color=[0,0,0,0])
        #self.view.add_widget(CustomModal(image=image,
        #                            text=name, subtext=description,
        #                            on_close=self.cancel,
        #                            bg_color=(255 / 255, 241 / 255, 115 / 255, 1)))
        #self.view.open()
        self.kmodal = KModalView(size_hint=(0.7, 0.4), auto_dismiss=True,
                                 background_color=[0, 0, 0, 0], content=
                                 TrophyContent(image=image,
                                    text=name, subtext=description))
        self.kmodal.open()

    def to_home(self):
        self.manager.go_to_screen('home', direction='right')

