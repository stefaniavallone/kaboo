from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_file("uix/components/kv/page.kv")


class Page(MDRelativeLayout):
    text = StringProperty()
    name = StringProperty()
    icon = StringProperty()

    label_bg_color = ColorProperty()
    label_text_color = ColorProperty()
    card_bg_color = ColorProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.callback = None
