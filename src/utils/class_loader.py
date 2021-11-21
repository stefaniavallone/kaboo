import inspect
import os
import pkgutil
from importlib import import_module
from pathlib import Path

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen


def folder_walker(package_path):
    folders = [os.path.join(package_path, o) for o in os.listdir(package_path)
               if os.path.isdir(os.path.join(package_path, o))]
    folders = [package_path] + [f.replace("\\", "/") for f in folders]
    return folders


def import_and_create_screens(package_path):
    pages = dict()
    for f in folder_walker(package_path):
        for (_, name, _) in pkgutil.iter_modules([Path(f)]):
            imported_module = import_module("." + name,
                                            package='.'.join(f.split('/')))

            for i in dir(imported_module):
                attribute = getattr(imported_module, i)

                if inspect.isclass(attribute) and \
                        not issubclass(attribute, ScreenManager) and \
                        issubclass(attribute, MDScreen) and \
                        not attribute == MDScreen and \
                        not inspect.isabstract(attribute):

                    class_name = attribute.__name__
                    file_path = os.path.join(f, name).replace("\\", "/")
                    import_file = f"from {file_path} import {class_name}"
                    kv_file = f"{os.path.join(f, 'kv', name)}.kv".replace("\\", "/")
                    pages[class_name] = {
                        "import": import_file,
                        "object": attribute,
                        "kv": kv_file,
                        "path": file_path
                    }
    return pages


def get_screens_package(package_path):
    screens = import_and_create_screens(package_path)
    screens_package = dict()
    for screen_name, screen_details in screens.items():
        screens_package[screen_name] = screen_details["path"].replace("/", ".")
    return screens_package



