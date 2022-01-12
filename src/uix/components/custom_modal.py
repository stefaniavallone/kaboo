from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock, BooleanProperty
from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_file("uix/components/kv/custom_modal.kv")


class CustomModal(MDRelativeLayout):

    closable = BooleanProperty()

    def __init__(self, closable=True, buttons=[], **kw):
        super().__init__(**kw)
        self.closable = closable
        self.buttons = buttons
        Clock.schedule_once(self._late_init)

    def _late_init(self, inst):
        if not self.closable:
            self.remove_widget(self.ids.close_button)
        if len(self.buttons) == 0:
            self.remove_widget(self.ids.buttons_container)
        elif len(self.buttons) >= 3:
            self.ids.buttons_container.y = -self.height - dp(20)
        for button in self.buttons:
            self.ids.buttons_container.add_widget(button)
