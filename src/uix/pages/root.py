from kivy import Logger
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from utils.setup.class_loader import import_and_create_screens


Builder.load_file("uix/pages/kv/root.kv")


screens = import_and_create_screens("uix/pages")


class Root(ScreenManager):
    """
    The Root (or Assembler) of the App.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self._add_screen("loading")
        Window.bind(on_keyboard=self.keyboard)
        self.exit_pressed_once = False

    def _add_screen(self, screen_name):
        if screen_name not in self.screen_names:
            screen_details = screens[screen_name]
            Builder.load_file(screen_details["kv"])  # You must import kv before
            exec(screen_details["import"])  # executing imports
            screen_object = screen_details[
                "object"]()  # eval(screen_details["object"])  # calling it
            screen_object.name = screen_name  # giving the name of the screen
            self.add_widget(
                screen_object
            )  # finally adding it to the screen manager
            Logger.debug(f"Added Screen: {screen_name}")

    def go_to_screen(self, screen_name, direction="left"):
        self._add_screen(screen_name)
        self.transition.direction = direction
        self.current = screen_name

    def reset_state(self, *args):
        self.exit_pressed_once = False

    def keyboard(self, window, key, *args):
        if key == 27 and self.current != "home":
            return True  # key event consumed by app
        else:
            if self.exit_pressed_once:
                return False  # key event passed to Android
            else:
                self.exit_pressed_once = True
                toast(self.app.i18n._("EXIT_MESSAGE"))
                Clock.schedule_once(self.reset_state, 5)
                return True  # key event consumed by app

