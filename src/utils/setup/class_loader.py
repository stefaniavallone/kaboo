import inspect
import os
import pkgutil
from importlib import import_module
from pathlib import Path

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen


## Utils
def folder_walker(package_path):
    folders = [os.path.join(package_path, o) for o in os.listdir(package_path)
               if os.path.isdir(os.path.join(package_path, o))]
    folders = [package_path] + [f.replace("\\", "/") for f in folders]
    return folders


def move_element(odict, thekey, newpos):
    ndict = dict()
    ndict[thekey] = odict.pop(thekey)
    i = 0
    for key in odict.keys():
        if i >= newpos:
            ndict[key] = odict[key]
        i += 1
    return ndict


def import_and_create_screens(package_path):
    package_path = package_path.replace("\\", "/")
    screens = dict()
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
                    import_path = file_path.replace("/", ".")
                    import_file = f"from {import_path} import {class_name}"
                    kv_file = f"{os.path.join(f, 'kv', name)}.kv".replace("\\", "/")
                    module_name = file_path.split("/")[-1].split("_screen")[0]
                    screens[module_name] = {
                        "import": import_file,
                        "object": attribute,
                        "kv": kv_file,
                        "class_name": class_name,
                        "path": file_path
                    }
    return screens


def get_screens_map(screens):
    screens_map = dict()
    for screen in screens.values():
        screens_map[screen["class_name"]] = screen["path"].replace("/", ".")
    return screens_map
        





