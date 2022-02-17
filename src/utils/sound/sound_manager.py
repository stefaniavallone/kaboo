from concurrent.futures import ThreadPoolExecutor, Future

from kivy import Logger

from utils.dp.observer import Observer
from utils.sound.sound_player import SoundPlayer


class SoundManager(dict, Observer):

    def __init__(self):
        super().__init__()
        self.executor = ThreadPoolExecutor()

    def get_sound(self, path, loop=False, volume=1):
        if path not in self:
            self.load_sound(path, loop, volume)
        if isinstance(self[path], Future):
            return self[path].result()
        else:
            return self[path]

    def load_sound(self, path, loop=False, volume=1):
        self[path] = self.executor.submit(self._load, path, loop, volume)

    def _load(self, path, loop, volume):
        Logger.debug(f"Sound {path} loading started.")
        sp = SoundPlayer(path, loop, volume)
        Logger.debug(f"Sound {path} loaded.")
        self[path] = sp
        return sp

    def remove_sound(self, path):
        sp = self[path]
        sp.stop()
        del self[path]

    def off_all(self):
        for name, sp in self.items():
            sp.off()

    def on_all(self):
        for name, sp in self.items():
            sp.on()

    def update(self, property_name, previous_state, new_state) -> None:
        if property_name == "game.sound" and previous_state != new_state:
            if not new_state:
                self.off_all()
            else:
                self.on_all()