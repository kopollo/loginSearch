class User:

    def __init__(self, name: str, patronymic: str, surname: str, email: str = ''):
        self.Name = name
        self.Patronymic = patronymic
        self.Surname = surname
        self.Email = email

    def get_name(self) -> str:
        return self.Name

    def get_patronymic(self) -> str:
        return self.Patronymic

    def get_surname(self) -> str:
        return self.Surname

    def get_email(self) -> str:
        return self.Email

    # TODO Processing of incorrect user data
