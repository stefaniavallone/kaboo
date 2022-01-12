from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip

Builder.load_file("uix/base_components/kv/kmd_icon_squared_button.kv")


class KMDIconSquaredButton(MDIconButton, MDTooltip):
    pass