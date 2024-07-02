from User import User


class EmailFormatSearch:

    def __init__(self, user: User):
        self.Name = user.get_name()
        self.Patronymic = user.get_patronymic()
        self.Surname = user.get_surname()
        self.Email = user.get_email()
        if len(self.Email) == 0:
            raise ValueError("Empty email")

    '''The function returns the email format. The return value is {.type|(number of characters)}...
      If the type is written with a capital letter, then the e-mail is also written
      with a capital letter. Type - Surname, First Name, Patronymic'''

    def email_format(self) -> str:
        username, hostname = map(str, self.Email.split("@"))
        lower_name = self.Name.lower()
        lower_patronymic = self.Patronymic.lower()
        lower_surname = self.Surname.lower()
        format_string = ""
        splited_username = self.split_username(username)
        for i in splited_username:
            if i in self.Name:
                format_string += f'?Name|{len(i)}'
            elif i in self.Surname:
                format_string += f'?Surname|{len(i)}'
            elif i in self.Patronymic:
                format_string += f'?Patronymic|{len(i)}'
            elif i in lower_name:
                format_string += f'?name|{len(i)}'
            elif i in lower_surname:
                format_string += f'?surname|{len(i)}'
            elif i in lower_patronymic:
                format_string += f'?patronymic|{len(i)}'
            else:
                format_string += "?" + i
        return format_string

    """The method of splitting email by name"""

    @staticmethod
    def split_username(username: str) -> list[str]:
        username_list = list()
        first_iter = 0
        for i in range(len(username)):
            if i == len(username) - 1:
                username_list.append(username[first_iter:i + 1])
                break
            if username[i] in "-_.":
                username_list.append(username[first_iter:i])
                username_list.append(username[i])
                first_iter = i + 1
            if username[i + 1].isupper() and username[i].isalpha() and username[i + 1].isalpha():
                username_list.append(username[first_iter:i + 1])
                first_iter = i + 1

        return username_list
