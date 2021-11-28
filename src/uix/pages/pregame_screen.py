from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.metrics import dp
from kivy.properties import NumericProperty, BooleanProperty, StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from uix.components.onboarding_item import OnboardingItem

class PreGameScreen(MDScreen,ThemableBehavior, BoxLayout, EventDispatcher):
    circles_size = NumericProperty(dp(20))
    play_button = BooleanProperty(True)
    min_move = NumericProperty(0.05)
    anim_type = StringProperty("out_quad")
    anim_move_duration = NumericProperty(0.2)
    bottom_bar_radius = ListProperty([dp(20), dp(20), 0, 0])
    show_bottom_bar = BooleanProperty(True)
    bottom_bar_color = ListProperty(None)
    circles_color = ListProperty(None)

    def __init__(self, **kwargs):
        super(PreGameScreen, self).__init__(**kwargs)
        self.register_event_type("on_finish")
        Clock.schedule_once(lambda x: self._update())

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, OnboardingItem):
            self.ids.carousel.add_widget(widget)
        else:
            super().add_widget(widget, index=index, canvas=canvas)

    def _on_finish_dispatch(self):
        self.dispatch("on_finish")

    def on_finish(self, *args):
        self.on_size()
        self._update()

    def reset(self):
        return self.ids.carousel.reset()

    def on_size(self, *args):
        self.ids.carousel.size = self.size

    def _update(self):
        self.ids.ghost_circle.size = [self.circles_size, self.circles_size]
