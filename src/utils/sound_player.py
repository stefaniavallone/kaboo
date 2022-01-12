from kivy.core.audio import SoundLoader

from app_status import AppStatus

class SoundPlayer:
    def __init__(self, path, loop=False, volume=1) -> None:
        self.sound = SoundLoader.load(path)
        self.sound.loop = loop
        self.sound.volume = volume

    def play(self, seconds=0):
        setting_sound = AppStatus.getv("game.sound", default_value=True)
        if setting_sound:
            self.sound.seek(seconds)
            self.sound.play()

    def stop(self, restart=True):
        if restart:
            self.sound.seek(0)
        self.sound.stop()