from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class KTabooHome(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        Window.size = (360, 640)

        self.window.add_widget(Image(source="resources/logo.png"))

        self.window.add_widget(Button(
            text="PLAY - Easy",
            size_hint=(1, 0.2),
            bold=True,
            background_color='#0099ff'
        ))
        self.window.add_widget(Button(
            text="PLAY - Medium",
            size_hint=(1, 0.2),
            bold=True,
            background_color='#0099ff'
        ))
        self.window.add_widget(Button(
            text="PLAY - Hard",
            size_hint=(1, 0.2),
            bold=True,
            background_color='#0099ff'
        ))

        return self.window
