from kivymd.uix.screen import MDScreen

class GamePreScreen(MDScreen):
   
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def to_game(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'
