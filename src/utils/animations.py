from kivy.animation import Animation


class Animations:
    @staticmethod
    def pop_up(widget, *args):
        widget_size_hint = widget.size_hint.copy()
        widget.size_hint = (0, 0)
        widget.opacity = 0
        animate = Animation(
            size_hint=widget_size_hint,
            opacity=1,
            duration=0.3)
        animate.start(widget)

