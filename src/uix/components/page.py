from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_file("uix/components/kv/page.kv")

class Page(MDRelativeLayout):
    text = StringProperty()
    avatar = StringProperty()
    story = StringProperty()
    name = StringProperty()
    icon = StringProperty()
    def __init__(self, **kw):
        super().__init__(**kw)
        self.callback = None
