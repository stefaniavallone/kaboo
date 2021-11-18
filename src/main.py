import json
import traceback

from kivy.factory import Factory

__version__ = "0.0.1"

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
