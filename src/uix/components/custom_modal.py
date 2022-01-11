from kivy.lang import Builder
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
        pass