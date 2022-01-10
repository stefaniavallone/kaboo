from types import SimpleNamespace
from typing import Any

from kivy.app import App
from kivy.logger import Logger


class AppStatus(SimpleNamespace):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.game_started = False
            
    @staticmethod
    def set(name, value):
        app = App.get_running_app()
        name_parts = list(name.split("."))
        obj = app.status
        for name_part in name_parts[:-1]:
            sn = getattr(obj, name_part, SimpleNamespace())
            setattr(obj, name_part, sn)
            obj = sn
        setattr(sn, name_parts[-1], value)
        Logger.debug(f"Saved value in app.status: {AppStatus.get(name_parts[0])}")

    @staticmethod
    def get(name, default_value=None):
        app = App.get_running_app()
        name_parts = list(name.split("."))
        obj = app.status
        for name_part in name_parts:
            value = getattr(obj, name_part, default_value)
            obj = value
        return value

    def __repr__(self) -> str:
        return self.__dict__

