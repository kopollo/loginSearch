from dataclasses import dataclass


@dataclass
class Email:
    control_structures: list[str]
    domain: str = ""


@dataclass
class User:
    first_name: str
    second_name: str
    last_name: str
