from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon
from kivymd.uix.list import ILeftBodyTouch, TwoLineAvatarIconListItem


Builder.load_file("uix/base_components/kv/list_item_with_checkbox.kv")


class ListItemWithCheckbox(TwoLineAvatarIconListItem,
                           RecycleKVIDsDataViewBehavior, MDBoxLayout):
    name = StringProperty()
    description = StringProperty()
    image = StringProperty()
    icon = StringProperty()


class LeftImage(ILeftBodyTouch, MDIcon):
    """Custom left container"""