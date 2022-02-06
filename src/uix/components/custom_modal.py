from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock, BooleanProperty, StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_file("uix/components/kv/custom_modal.kv")


class CustomModal(MDRelativeLayout):

    closable = BooleanProperty()
    image = StringProperty()
    text = StringProperty()
    subtext = StringProperty()

    def __init__(self, image, text, subtext, bg_color, on_close=None, buttons=[], **kw):
        super().__init__(**kw)
        self.image = image
        self.text = text
        self.subtext = subtext
        self.on_close = on_close
        self.buttons = buttons
        Clock.schedule_once(self._late_init)
        self.register_event_type('on_close')

    def _late_init(self, inst):
        if self.on_close is None:
            self.remove_widget(self.ids.close_button)
        if len(self.buttons) == 0:
            self.remove_widget(self.ids.buttons_container)
        elif len(self.buttons) >= 3:
            self.ids.buttons_container.y = -self.height - dp(20)
        for button in self.buttons:
            self.ids.buttons_container.add_widget(button)
