import inspect
import os
import pkgutil
from importlib import import_module
from pathlib import Path

from kivy.uix.screenmanager import ScreenManager


def import_and_create_routes(package_path):
    pages = dict()
    for f in folder_walker(package_path):
        for (_, name, _) in pkgutil.iter_modules([Path(f)]):
            imported_module = import_module("." + name,
                                            package='.'.join(f.split('/')))

            for i in dir(imported_module):
                attribute = getattr(imported_module, i)

                if inspect.isclass(attribute) and \
                        not issubclass(attribute, ScreenManager) and \
                        not inspect.isabstract(attribute):
                    pages[name] = {
                        "import": f"from {os.path.join(f, name)} import {attribute}",
                        "object": attribute,
                        "kv": ""
                    }
                    # setattr(sys.modules[__name__], name, attribute)
    return pages


def folder_walker(package_path):
    folders = [os.path.join(package_path, o) for o in os.listdir(package_path)
               if os.path.isdir(os.path.join(package_path, o))]
    folders = [package_path] + [f.replace("\\", "/") for f in folders]
    return folders
