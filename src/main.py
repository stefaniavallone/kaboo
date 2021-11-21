import json
import logging
import os
import sys
import traceback

from kivy import Logger
from kivy.factory import Factory

__version__ = "0.0.1"

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "utils"))

from base_app import BaseApp
from utils.env import setup_env

"""
Registering factories from factory.json.
"""
# r = Factory.register
#
# with open("factory_registers.json") as fd:
#     custom_widgets = json.load(fd)
#     for module, _classes in custom_widgets.items():
#         for _class in _classes:
#             r(_class, module=module)


if __name__ == "__main__":
    setup_env()

    try:
        BaseApp().run()
    except Exception:
        error = traceback.format_exc()

        with open("ERROR.log", "w") as error_file:
            error_file.write(error)

        print(error)
