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
        self.last_seconds = kwargs.get("last_seconds", 10)
        if self.last_seconds > self.seconds:
            self.last_seconds = self.seconds
        self.register_event_type('on_finish')
        self.register_event_type('on_last_seconds')
    
    def update(self, dt):
        self.seconds = self.seconds - self.interval
        if self.seconds <= self.last_seconds:
            self.dispatch('on_last_seconds')
            self.last_seconds = -1  # to avoid the dispatching of a new event
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

    def on_last_seconds(self):
        pass