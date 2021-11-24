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

    def _add_circles(self):
        self.total_circles = len(self.slides) - 1

        if self.parent.circles_color:
            circle_color = self.parent.circles_color
        else:
            circle_color = self.theme_cls.primary_color

        for _ in range(self.total_circles + 1):
            self.parent.ids.circles_box.add_widget(
                ItemCircles(
                    width=self.parent.circles_size, _circles_color=circle_color
                )
            )

        self._current_circle = self.total_circles
        Clock.schedule_once(lambda x: self._set_current_circle(animation=False))

    def on_size(self, *args):
        Clock.schedule_once(lambda x: self._set_current_circle(animation=False))
        return super().on_size(*args)

    def reset(self):
        self._current_circle = self.total_circles
        self._set_current_circle()
        self.load_slide(self.slides[0])

    def _set_current_circle(self, mode=None, animation=True):
        if mode == "next":
            if self._current_circle > 0:
                self._current_circle -= 1
            else:
                self.parent._on_finish_dispatch()

        elif mode == "previous":
            if self._current_circle < self.total_circles:
                self._current_circle += 1
        if animation:
            width = self.parent.ids.ghost_circle.width
            anim = Animation(
                pos=self.parent.ids.circles_box.children[
                    self._current_circle
                ].pos,
                t=self.anim_type,
                duration=self.anim_move_duration,
            )
            anim.start(self.parent.ids.ghost_circle)
        else:
            self.parent.ids.ghost_circle.pos = (
                self.parent.ids.circles_box.children[self._current_circle].pos
            )

    def on_touch_up(self, touch):
        if abs(self._offset) > self.width * self.min_move:

            if self._offset > 0:  # previous screen
                self._set_current_circle("previous")

            elif self._offset < 0:  # next screen
                self._set_current_circle("next")

        return super().on_touch_up(touch)

    def _on_resize(self, *args):
        Clock.schedule_once(lambda x: self._set_current_circle(animation=False))