from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("uix/components/kv/confirm_content.kv")


class ConfirmContent(MDBoxLayout):

    image = StringProperty()
    text = StringProperty()
    subtext = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
