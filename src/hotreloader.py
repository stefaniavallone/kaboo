import os

from base_app import BaseApp
from utils.setup.class_loader import import_and_create_screens, get_screens_map
from utils.setup.env import setup_env
from kaki.app import App as HotReloaderApp

from uix.pages.root import Root


KV_FOLDER = os.path.join(os.getcwd(), "uix", "pages", "kv")


class LiveApp(BaseApp, HotReloaderApp):
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    KV_FILES = [os.path.join(KV_FOLDER, i) for i in os.listdir(KV_FOLDER)]

    # Class to watch from *.py files
    # You need to register the *.py files in uix/pages/*.py
    CLASSES = get_screens_map(import_and_create_screens("uix/pages"))

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def __init__(self, **kwargs):
        super(LiveApp, self).__init__(**kwargs)

    def build_app(self):
        return Root()


if __name__ == "__main__":
    setup_env()
    LiveApp().run()
