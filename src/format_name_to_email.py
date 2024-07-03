from src.models import User, Email


class FormatNameToEmail:
    @staticmethod
    def format_name_to_email(user: User, email_format: Email):
        supposed_names = []
        l = [user.first_name, user.last_name, user.last_name]
        name = ""
        for s in email_format.control_structures:
            ...

    def get_logins(self):
        pass

