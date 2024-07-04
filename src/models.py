from dataclasses import dataclass
from enum import Enum


@dataclass
class Email:
    control_structures: list[str]
    domain: str = ""

    def pretty(self):
        res = ""
        for s in self.control_structures:
            if s in Commands:
                res += "<" + s.value + ">"
                # pass
            else:
                res += s
        return res


def transliteration(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|I|I|K|L|M|N|O|P|R|S|T|U|F|Kh|Tc|Ch|Sh|Shch||Y||E|Iu|Ia'.split(
        '|')
    return text.translate({ord(k): v for k, v in zip(cyrillic, latin)})


@dataclass
class User:
    first_name: str
    second_name: str
    last_name: str

    def transliterate(self):
        return User(transliteration(self.first_name),
                    transliteration(self.second_name),
                    transliteration(self.last_name))


class Commands(Enum):
    lower_one = "lower_one"
    upper_one = "upper_one"
    lower_many = "lower_many"
    upper_many = "upper_many"

    """
    ".-_": разделители

    "lower_one": односимвольное строчное поле
    "upper_one": односимвольное заглавное поле

    "lower_many": многосимвольное строчное поле
    "upper_many": многосимвольное заглавное поле
    """
