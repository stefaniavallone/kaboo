from kivy.lang import Builder
from kivymd.uix.button import MDIconButton

Builder.load_file("uix/base_components/kv/kmd_icon_squared_button.kv")


class KMDIconSquaredButton(MDIconButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)