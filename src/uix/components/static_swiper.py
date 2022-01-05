from kivymd.uix.swiper import MDSwiper


class StaticSwiper(MDSwiper):

    def on_touch_down(self, touch):
        return False
    
    def next(self):
        current_index = self.get_current_index()
        if current_index < len(self.get_items()) - 1: 
            self.set_current(self.get_current_index() + 1)