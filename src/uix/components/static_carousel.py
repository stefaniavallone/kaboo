from kivymd.uix.carousel import MDCarousel


class StaticCarousel(MDCarousel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        return False
