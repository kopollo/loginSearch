from src.models import Email, User


class Formatter:
    def __init__(self, save_path: str):
        self.save_path = save_path

    def add_paragraph_with_finded_email(self, emails: list):
        with open(self.save_path, 'w', encoding="utf-8") as f:
            print("Finded emails:", file=f)
            print("----------------", file=f)
            for email in emails:
                print(email, file=f)
            print("----------------", file=f)
            print("", file=f)

    def add_paragraph_with_email_formats(self, email_formats: list[Email]):
        with open(self.save_path, 'a', encoding="utf-8") as f:
            print("email formats:", file=f)
            print("----------------", file=f)
            for email in email_formats:
                print(email.pretty(), file=f)
            print("----------------", file=f)
            print("", file=f)

    def add_paragraph_with_users(self, users: list):
        with open(self.save_path, 'a', encoding="utf-8") as f:
            print("Users:", file=f)
            print("----------------", file=f)
            for user in users:
                print(user, file=f)
            print("----------------", file=f)
            print("", file=f)

    def add_paragraph_with_user_logins(self, user: User, email_format: Email, logins: list):
        with open(self.save_path, 'a', encoding="utf-8") as f:
            print(f"user: {user}", file=f)
            print(f"email format: {email_format.pretty()}", file=f)
            print("----------------", file=f)
            for login in logins:
                print(login, file=f)
            print("----------------", file=f)
            print("", file=f)
