from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("uix/components/kv/title_and_text_content.kv")


class TitleAndTextContent(MDBoxLayout):

    title = StringProperty('')
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = kwargs.get("title")
        if self.title is None or self.title == '':
            self.remove_widget(self.ids.title)