from typing import Any
from utils.dp.observer import ConcreteSubject


class AppStatus(dict, ConcreteSubject):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def setv(self, name, value):
        name_parts = list(name.split("."))
        obj = self
        for name_part in name_parts[:-1]:
            sn = obj.get(name_part, dict())
            obj[name_part] = sn
            obj = sn
        previous_state = sn.get(name_parts[-1])
        sn[name_parts[-1]] = value
        self.notify(name, previous_state, value)

    def getv(self, name, default_value=None):
        name_parts = list(name.split("."))
        obj = self
        for name_part in name_parts:
            value = obj.get(name_part, default_value)
            if not isinstance(value, dict):
                break
            obj = value
        return value

