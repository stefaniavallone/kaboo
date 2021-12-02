from kivy.core.window import Animation, Window
from kivy.uix.carousel import Carousel
from kivymd.theming import ThemableBehavior

from uix.components.item_circle import ItemCircles
from kivy.clock import Clock

class Carousel(ThemableBehavior, Carousel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda x: self._add_circles())
        Window.bind(on_resize=self._on_resize)


