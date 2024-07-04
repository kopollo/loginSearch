import itertools

from src.models import User, Email, Commands


class FormatNameToEmail:
    @staticmethod
    def format_name_to_email(user: User, email_format: Email):
        supposed_names = []
        # l = [user.first_name, user.last_name, user.last_name]
        for l in itertools.permutations(sorted([user.first_name, user.second_name, user.last_name])):
            l = list(l)
            name = ""
            idx = 0
            for operation in email_format.control_structures:
                if idx >= 3:
                    pass
                if operation in Commands:
                    user_part = l[idx]
                    if operation == Commands.upper_one:
                        user_part = user_part[:1].capitalize()
                    if operation == Commands.upper_many:
                        user_part = user_part.capitalize()
                    if operation == Commands.lower_one:
                        user_part = user_part[:1].lower()
                    if operation == Commands.lower_many:
                        user_part = user_part.lower()

                    name += user_part
                    idx += 1
                else:
                    name += operation
            supposed_names.append(name)
        return supposed_names

    def get_logins(self):
        pass
