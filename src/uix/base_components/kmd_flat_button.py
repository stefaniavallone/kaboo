from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.button import MDFlatButton

Builder.load_file("uix/base_components/kv/kmd_flat_button.kv")


class KMDFlatButton(MDFlatButton):
    width = NumericProperty(100)
    height = NumericProperty(100)
