from kivy.core.audio import SoundLoader
from kivy.app import App


class SoundPlayer:

    def __init__(self, path, loop=False, volume=1) -> None:
        self.app = App.get_running_app()
        self.sound = SoundLoader.load(path)
        self.sound.loop = loop
        self.sound.volume = volume
        self._prev_volume = volume

    def off(self):
        self.sound.volume = 0

    def on(self):
        self.sound.volume = self._prev_volume

    def play(self, restart=True):
        if restart:
            self.sound.seek(0)
        self.sound.play()

    def pause(self):
        self.stop(restart=False)

    def stop(self, restart=True):
        if restart:
            self.sound.seek(0)
        self.sound.stop()

