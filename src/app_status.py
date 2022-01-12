from types import SimpleNamespace
from typing import Any

from kivy.app import App
from kivy.logger import Logger


class DotDict(dict):
    """
    a dictionary that supports dot notation as well as dictionary access notation-
    usage: d = DotDict() or d = DotDict({'val1':'first'})
    set attributes: d.val2 = 'second' or d['val2'] = 'second'
    get attributes: d.val2 or d['val2']
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct=dict()):
        super().__init__()
        for key, value in dct.items():
            if hasattr(value, '__getitem__'):
                value = DotDict(value)
            self[key] = value


class AppStatus(dict):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
            
    @staticmethod
    def setv(name, value):
        app = App.get_running_app()
        name_parts = list(name.split("."))
        obj = app.status
        for name_part in name_parts[:-1]:
            sn = obj.get(name_part, dict())
            obj[name_part] = sn
            obj = sn
        sn[name_parts[-1]] = value
        Logger.debug(f"Saved value in app.status: {AppStatus.getv(name_parts[0])}")

    @staticmethod
    def getv(name, default_value=None):
        app = App.get_running_app()
        name_parts = list(name.split("."))
        obj = app.status
        for name_part in name_parts:
            value = obj.get(name_part, default_value)
            if not isinstance(value, dict):
                break
            obj = value
        return value

