from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty
from kivy.uix.modalview import ModalView

Builder.load_file("uix/base_components/kv/kmodal_view.kv")


class KModalView(ModalView):

    closable = BooleanProperty()

    def __init__(self, closable=True, buttons=[], content=None, **kw):
        super().__init__(**kw)
        self.background_color = [0, 0, 0, 0]
        self.buttons = buttons
        self.closable = closable
        self.content = content
        self._compose()

    def _compose(self):
        if not self.closable:
            self.ids.container.remove_widget(self.ids.close_button)
        if len(self.buttons) == 0:
            self.remove_widget(self.ids.buttons_container)
        elif len(self.buttons) >= 3:
            self.ids.buttons_container.y = -self.height - dp(20)
        for button in self.buttons:
            self.ids.buttons_container.add_widget(button)
        if self.content is not None:
            self.ids.content_container.add_widget(self.content)

    def on_content(self):
        self.ids.content_container.add_widget(self.content)

    def on_buttons(self):
        for button in self.buttons:
            self.ids.buttons_container.add_widget(button)