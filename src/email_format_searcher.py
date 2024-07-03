from src.models import Email, Commands
import re


class EmailFormatSearch:

    def __init__(self, email: str):
        """
        скрипт, который разделит email по разделителям ".", "_", "-" или заглавная буква. Вот пример
        "a.s.lai@mail.ru" -> ["a", ".", "s", "lai", "@mail.ru"]
        "LaiAS@mail.ru" -> ["Lai", "A", "S", "@mail.ru"]
        """
        self.email = email

    def split_row_email(self):
        delimiters = ['.', '_', '-']
        parts = []
        current_part = ''
        for i, char in enumerate(self.email):
            if char == "@":
                parts.append(current_part)
                parts.append(self.email[i:])
                break
            elif char in delimiters:
                parts.append(current_part)
                parts.append(char)
                current_part = ''
            elif char.isupper():
                if current_part != "":
                    parts.append(current_part)
                current_part = char
            else:
                current_part += char
        return parts

    def get_control_email(self) -> Email:
        """
        Instruction for translate email into format
        ".-_": разделители

        "lower_one": односимвольное строчное поле
        "upper_one": односимвольное заглавное поле

        "lower_many": многосимвольное строчное поле
        "upper_many": многосимвольное заглавное поле
        """
        r = []
        row_email = self.split_row_email()
        domain = row_email[-1]

        lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z']

        upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for s in row_email:
            if s in ".-_":
                r.append(s)
            elif s[0] == "@":
                r.append(s)
            elif s[0] in lower_alphabet:
                if len(s) == 1:
                    r.append(Commands.lower_one)
                else:
                    r.append(Commands.lower_many)
            elif s[0] in upper_alphabet:
                if len(s) == 1:
                    r.append(Commands.upper_one)
                else:
                    r.append(Commands.upper_many)
            else:
                print("XXXXXXXXXXXXXXXXXXXXXXX")
        return Email(r, domain)
