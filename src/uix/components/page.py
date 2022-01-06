from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_file("uix/components/kv/page.kv")

class Page(MDRelativeLayout):
    text = StringProperty()
    avatar = StringProperty()
    story = StringProperty()
    name = StringProperty()
    to_home = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.callback = None

    # def on_parent(self, *args):
    #     if not self.avatar:
    #         self.remove_widget(self.ids.avatar)