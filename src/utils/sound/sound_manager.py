from kivy import Logger

from utils.dp.observer import Observer
from utils.sound.sound_player import SoundPlayer


class SoundManager(dict, Observer):

    def __init__(self):
        super().__init__()

    def get_sound(self, path, loop=False, volume=1):
        if path not in self:
            self.load_sound(path, loop, volume)
        else:
            return self[path]

    def load_sound(self, path, loop=False, volume=1):
        self[path] = self._load(path, loop, volume)

    def _load(self, path, loop, volume):
        Logger.debug(f"Sound {path} loading started.")
        sp = SoundPlayer(path, loop, volume)
        Logger.debug(f"Sound {path} loaded.")
        return sp

    def remove_sound(self, path):
        sp = self[path]
        sp.stop()
        del self[path]

    def off_all(self):
        for name in self.keys():
            sp = self.get_sound(name)
            sp.off()

    def on_all(self):
        for name in self.keys():
            sp = self.get_sound(name)
            sp.on()

    def update(self, property_name, previous_state, new_state) -> None:
        if property_name == "game.sound" and previous_state != new_state:
            if not new_state:
                self.off_all()
            else:
                self.on_all()