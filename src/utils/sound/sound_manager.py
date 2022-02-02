from utils.dp.observer import Observer, Subject
from utils.sound.sound_player import SoundPlayer
from utils.translation.internationalization import i18n


class SoundManager(dict, Observer):

    def __init__(self):
        super().__init__()
        print(i18n._("MAMMT"))

    def get_sound(self, path, loop=False, volume=1):
        if path not in self:
            sp = SoundPlayer(path, loop, volume)
            self[path] = sp
        else:
            sp = self[path]
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