from kivymd.uix.screen import MDScreen

from logic.score import get_score_history
from logic.trophies.trophies_checker import check_trophies
from uix.base_components.kmodal_view import KModalView
from uix.components.trophy_content import TrophyContent


class TrophiesScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self):
        score_history = get_score_history()
        checked_trophies = check_trophies(score_history)

        list_trophies = list()
        for name, trophy in checked_trophies.items():
            list_trophies.append({
                'name': trophy["name"],
                'description': trophy["description"],
                'image': trophy["image"],
                'icon': "checkbox-multiple-marked-circle" if trophy["obtained"] else "",
                'details': self.show_details})
        self.ids.list_trophies.data = list_trophies

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

