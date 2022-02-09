import gettext
from kivy.event import Observable

from utils.dp.observer import Observer


class I18n(Observer, Observable):
    module = "base"
    default_language = "en"
    observers = []

    def __init__(self):
        super().__init__()
        self.base_dir = "assets/locales"
        self.language = self.default_language
        self.switch_lang(self.language)

    def switch_lang(self, lang):
        # get the right locales directory, and instanciate a gettext
        self.language = lang
        locales = gettext.translation(self.module, localedir=self.base_dir,
                                      languages=[lang])
        self.ugettext = locales.gettext
        # update all the kv rules attached to this text
        for func, largs, kwargs in self.observers:
            func(largs, None, None)

    def _(self, text, *args, **kwargs):
        translated_text = self.ugettext(text)
        for k, v in kwargs.items():
            translated_text = translated_text.replace(f"[{k}]", str(v))
        return translated_text

    def fbind(self, name, func, args, **kwargs):
        if name == "_":
            self.observers.append((func, args, kwargs))
        else:
            return super().fbind(name, func, *args, **kwargs)

    def funbind(self, name, func, args, **kwargs):
        if name == "_":
            key = (func, args, kwargs)
            if key in self.observers:
                self.observers.remove(key)
        else:
            return super().funbind(name, func, *args, **kwargs)

    def update(self, property_name, previous_state, new_state) -> None:
        if property_name == "app.lang" and previous_state != new_state:
            self.switch_lang(new_state)



i18n = I18n()


if __name__ == "__main__":
    i18n = I18n()

    print(i18n._("TEXT_WITH_PARAMS", team="Team 1", points="3"))
    i18n.switch_lang("it")
    print(i18n._("TEXT_WITH_PARAMS", team="Team 1", points="3"))