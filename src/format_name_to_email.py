from src.models import User, Email


class FormatNameToEmail:

    def format_name_to_email(user: User, email_format: Email):
        """
        Instruction for translate email into format
        ".-_": разделители

        "a": односимвольное строчное поле
        "ak": односимвольное заглавное поле

        "s": многосимвольное строчное поле
        "sk": односимвольное заглавное поле
        "d": domain
        """
        supposed_names = []
        l = [user.first_name, user.last_name, user.last_name]
        name = ""
        # for s in email_format.control_structures:
        #     if s == "a":
        #         name += l[0]
        #     if s == "ak":
        #         name += l[0].upper()
        #

    def get_logins(self):
        pass

