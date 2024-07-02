from User import User


class EmailFromFormat:

    def __init__(self, user: User):
        self.Name = user.get_name()
        self.Patronymic = user.get_patronymic()
        self.Surname = user.get_surname()

    def get_email(self, email_format: str) -> str:
        list_email_format = "".join(list(map(lambda x: self.parser(x), email_format.split("?"))))
        return list_email_format

    def parser(self, once_format: str) -> str:
        if len(once_format) == 0:
            return ""
        print(once_format)
        try:
            type_format, len_format = map(str, once_format.split("|"))
        except ValueError:
            return once_format
        len_format = int(len_format)
        if type_format == "Surname":
            return self.Surname[:len_format]
        elif type_format == "surname":
            return self.Surname[:len_format].lower()
        elif type_format == "Name":
            return self.Name[:len_format]
        elif type_format == "name":
            return self.Name[:len_format].lower()
        elif type_format == "Patronymic":
            return self.Patronymic[:len_format]
        elif type_format == "patronymic":
            return self.Patronymic[:len_format].lower()
        else:
            raise ValueError("Wrong Format")
