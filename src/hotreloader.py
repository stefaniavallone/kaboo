import os

from base_app import initialize_app
from utils.class_loader import get_screens_package
from utils.env import setup_env
from kaki.app import App as HotReloaderApp

from kivymd.app import MDApp

from uix.pages.root import Root


KV_FOLDER = os.path.join(os.getcwd(), "uix", "pages", "kv")


class LiveApp(MDApp, HotReloaderApp):
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    #KV_FILES = [os.path.join(KV_FOLDER, i) for i in os.listdir(KV_FOLDER)]

    # Class to watch from *.py files
    # You need to register the *.py files in uix/pages/*.py
    CLASSES = get_screens_package("uix/pages")

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def __init__(self, **kwargs):
        super(LiveApp, self).__init__(**kwargs)
        initialize_app(self)

    def build_app(self):
        return Root()


if __name__ == "__main__":
    setup_env()
    LiveApp().run()
