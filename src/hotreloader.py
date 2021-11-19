import os

from base_app import initialize_app, BaseApp
from utils.env import setup_env
from kaki.app import App as HotReloaderApp

from kivymd.app import MDApp

from src.uix.pages.root import Root


KV_FOLDER = os.path.join(os.getcwd(), "src", "uix", "pages", "kv")


class LiveApp(MDApp, HotReloaderApp):
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    KV_FILES = [os.path.join(KV_FOLDER, i) for i in os.listdir(KV_FOLDER)]

    # Class to watch from *.py files
    # You need to register the *.py files in libs/uix/baseclass/*.py
    CLASSES = {'Root': 'src.uix.pages.root', 'HomeScreen': 'src.uix.pages.home_screen'}

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        ("./src", {"recursive": True}),
    ]

    def __init__(self, **kwargs):
        super(LiveApp, self).__init__(**kwargs)
        initialize_app(self)

    def build_app(self):
        return Root()


if __name__ == "__main__":
    setup_env()
    LiveApp().run()
