from kivy import Logger
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from utils.kiva.class_loader import import_and_create_screens


Builder.load_file("uix/pages/kv/root.kv")


class Root(ScreenManager):
    """
    The Root (or Assembler) of the App.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.add_screens)
        Window.bind(on_keyboard=self.keyboard)

    def add_screens(self, interval=0.1):
        """
        If you need to use more screens in your app,
        Create your screen files like below:
            1. Create screen_file.py in libs/uix/pages/
            2. Create screen_file.kv in libs/uix/kv/
            3. Add the screen details in screens.json like below:
                {
                    ...,
                    "screen_name": {
                        "import": "from libs.uix.pages.screen_py_file import ScreenObject",
                        "kv": "libs/uix/kv/screen_kv_file.kv",
                        "object": "ScreenObject()"
                    }
                }
                Note: In .JSON you must not use:
                        * Unneeded Commas
                        * Comments
        """

        screens = import_and_create_screens("uix/pages")

        for screen_name in screens.keys():
            screen_details = screens[screen_name]
            Builder.load_file(screen_details["kv"])  # You must import kv before
            exec(screen_details["import"])  # executing imports
            screen_object = screen_details["object"]() #eval(screen_details["object"])  # calling it

            screen_object.name = screen_name  # giving the name of the screen
            self.add_widget(
                screen_object
            )  # finally adding it to the screen manager
            Logger.debug(f"Added Screen: {screen_name}")

    def keyboard(self, window, key, *args):
        if key == 27 and self.current != "home":
            self.current = "home"
            return True  # key event consumed by app
        else:
            return False  # key event passed to Android