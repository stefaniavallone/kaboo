from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivy.app import App

import version
from utils.setup.class_loader import import_and_create_screens




class LoadingScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        self.version = version.__version__
        screens = import_and_create_screens("uix/pages")
        sounds = [
            ('assets/sounds/cute.ogg', True, 1),
            ('assets/sounds/ukulele.ogg', True, 0.2),
            ('assets/sounds/clock-ticking.ogg', False, 1),
            ('assets/sounds/right-notification.ogg', False, 1),
            ('assets/sounds/wrong-notification.ogg', False, 1),
            ('assets/sounds/jump-notification.ogg', False, 1),
            ('assets/sounds/applause.ogg', False, 1),
        ]
        screens_names = list(screens.keys())
        self.objects = screens_names + sounds

    def on_enter(self, *args):
        self.ids.progress_bar.start()
        Clock.schedule_once(lambda x: self.load_objects(), 0)

    def load_objects(self, *args):
        increment = round(100/len(self.objects))
        for i, obj in enumerate(self.objects):
            self.load_object(i, increment, obj)

    def load_object(self, index, increment, obj):
        Clock.schedule_once(lambda x: self._load_obj(index, increment, obj), index*0.2+0.1)

    def _load_obj(self, index, increment, obj):
        if isinstance(obj, str):
            self.manager.add_screen(obj)
        else:
            self.app.sound_manager.load_sound(*obj)
        self.update_bar(increment)
        if index == len(self.objects) - 1:
            self.manager.go_to_screen("home")

    def update_bar(self, value):
        self.ids.progress_bar.value += value






