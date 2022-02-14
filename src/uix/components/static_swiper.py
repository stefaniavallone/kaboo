from kivymd.uix.swiper import MDSwiper


class StaticSwiper(MDSwiper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        return False
    
    def next(self):
        current_index = self.get_current_index()
        print("CURRENT_INDEX", current_index)
        if current_index < len(self.get_items()) - 1: 
            self.set_current(self.get_current_index() + 1)
            print("CARDS", self.get_items())
            #self.children[0].clear_widgets(self.children[0].children[:-2])