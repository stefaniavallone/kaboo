from kivy.app import App
from kivy.factory import Factory
from kivy.uix.carousel import Carousel


class Logo(App):
    def build(self):

        carousel = Carousel(direction='right', loop=True)
        for i in range(2):
            image = Factory.Label(text=str(i))
            carousel.add_widget(image)

        return carousel


if __name__ == '__main__':
    Logo().run()