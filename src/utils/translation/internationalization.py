import gettext

# el = gettext.translation('base', localedir='locales', languages=['el'])
# el.install()

# _ = el.gettext  # Greek

# ngettext = el.ngettext
from enum import Enum


class Internationalize:
    module = "base"
    default_language = "en"

    def __init__(self):
        self.base_dir = "assets/locales"
        self.language = self.default_language
        self.switch_lang(self.language)

    def switch_lang(self, lang):
        # get the right locales directory, and instanciate a gettext
        self.language = lang
        locales = gettext.translation(self.module, localedir=self.base_dir,
                                      languages=[lang])
        self.ugettext = locales.gettext

    def _(self, text):
        return self.ugettext(text)

global i18n
i18n = Internationalize()


def print_some_strings():
    print(i18n._("HOME_LEVEL_EASY"))


if __name__ == "__main__":
    print_some_strings()
    i18n.switch_lang("it")
    print_some_strings()