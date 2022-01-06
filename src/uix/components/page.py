from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_file("uix/components/kv/page.kv")

class Page(MDRelativeLayout):
    avatar = StringProperty()
    story = StringProperty()
    name = StringProperty()

    # def on_parent(self, *args):
    #     if not self.avatar:
    #         self.remove_widget(self.ids.avatar)