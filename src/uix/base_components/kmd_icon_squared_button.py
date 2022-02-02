from kivy.lang import Builder
from kivymd.uix.button import MDIconButton

Builder.load_file("uix/base_components/kv/kmd_icon_squared_button.kv")


class KMDIconSquaredButton(MDIconButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_disabled(self, instance, value):
        self.md_bg_color = (self.md_bg_color[0] * 0.5,
                            self.md_bg_color[1] * 0.5,
                            self.md_bg_color[2] * 0.5,
                            self.md_bg_color[3])