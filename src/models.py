from dataclasses import dataclass
from enum import Enum


@dataclass
class Email:
    control_structures: list[str]
    domain: str = ""


@dataclass
class User:
    first_name: str
    second_name: str
    last_name: str


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
