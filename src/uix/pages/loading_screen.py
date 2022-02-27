from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivy.app import App

import version
from utils.setup.class_loader import import_and_create_screens

screens = import_and_create_screens("uix/pages")


class LoadingScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.version = version.__version__

    def on_enter(self, *args):
        self.ids.progress_bar.start()
        Clock.schedule_once(lambda x: self.load_objects(), 0)

    def update_bar(self, value, index):
        self.ids.progress_bar.value += value
        if index == len(screens) - 1:
            self.manager.go_to_screen("home")

    def _load_screen(self, screen, index, increment):
        self.manager._add_screen(screen)
        self.update_bar(increment, index)

    def load_screen(self, screen, index, increment):
        Clock.schedule_once(lambda x: self._load_screen(screen, index, increment), index*0.2+0.1)

    def load_objects(self, *args):
        increment = round(100/len(screens))
        screens_names = list(screens.keys())
        for i, screens_name in enumerate(screens_names):
            self.load_screen(screens_name, i, increment)




