from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.card import MDCard

Builder.load_file("uix/components/kv/game_card.kv")
class GameCard(MDCard):
    text = StringProperty()
    subtext = StringProperty()
    wrong_answer_action = ObjectProperty()
    ok_answer_action = ObjectProperty()
    jump_answer_action = ObjectProperty()
