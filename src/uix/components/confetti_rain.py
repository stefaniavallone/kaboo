from random import randint

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock, NumericProperty, ListProperty
from kivy.uix.floatlayout import FloatLayout


Builder.load_file("uix/components/kv/confetti_rain.kv")


class ConfettiItem(FloatLayout):
    color = ListProperty()

    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        Clock.schedule_once(self._update)

    def _update(self, *args):
        (Animation(opacity=1, d=randint(*self.parent.time_before_fade))).start(
            self)


class ConfettiRain(FloatLayout):
    size_range = ListProperty([dp(2), dp(5)])
    time_range = ListProperty([3, 5])
    speed = ListProperty([3, 6])
    time_before_fade = ListProperty([1, 3])
    number = NumericProperty(250)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            Clock.schedule_once(self._update)

    def stop(self):
        self.running = False

    def add_item(self, count):
        print("ADD_ITEMMMMMMM")
        for x in range(count):
            color = [randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1]
            item = ConfettiItem(
                size=[
                    randint(*self.size_range),
                    randint(*self.size_range)
                ],
                pos=[
                    randint(0, int(self.width)),
                    randint(int(self.height * 0.9), int(self.height))
                ],
                color=color
            )
            self.add_widget(item)
            self.start_anim(item)
        return None

    def _update(self, *args):
        self.add_item(self.number)

    def start_anim(self, item):
        target_pos = [randint(0, self.width), 0]
        final_time = randint(*self.time_range)

        speed = randint(*self.time_range)
        anim = Animation(pos=target_pos, d=speed)
        anim.start(item)

        # remove
        Clock.schedule_once(lambda x: self.remove_widget(item), final_time)

        # add new
        if self.running:
            Clock.schedule_once(lambda x: self.add_item(1), final_time)

        fade_time = final_time - randint(*self.time_before_fade)
        Clock.schedule_once(lambda x: self._fade_out(item, fade_time),
                            final_time - fade_time)

    def _fade_out(self, item, time):
        anim = Animation(opacity=0, d=time)
        anim.start(item)