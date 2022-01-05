from kivy.clock import Clock
from kivymd.uix.label import MDLabel
import time


class Timer(MDLabel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.format = kwargs.get("format", "%H:%M:%S")
        self.seconds = kwargs.get("seconds", 60)
        self.interval = kwargs.get("interval", 0.05)
        self.running = False
        self.register_event_type('on_finish')
    
    def update(self, dt):
        self.seconds = self.seconds - self.interval
        if self.seconds < 0:
            self.seconds = 0
            self.dispatch('on_finish')
            self.stop()
        self.text = time.strftime(self.format, time.gmtime(self.seconds))
    
    def start(self):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update, self.interval)

    def stop(self):
        if self.running:
            self.running = False
            Clock.unschedule(self.update)
    
    def on_finish(self):
        pass