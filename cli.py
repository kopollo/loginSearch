# import argparse
# parser = argparse.ArgumentParser(description="Домен")
# parser.add_argument("-n", help="Введите домен компании")
from src.data_extracter import find_emails, get_document_text
from src.docx_file_downloader import DocxFileDownloader
from src.email_format_searcher import EmailFormatSearch
from src.format_name_to_email import FormatNameToEmail
from src.models import User

# 1. Input data

# 2. find and download emails
# file_links = DocxFileDownloader("rosneft").get()

# 3. find all emails in .docx
emails = find_emails("upload/test.docx")
print(emails)

# 4. Find all emails in .docx
for email in emails:
    email_format = EmailFormatSearch(email).get_email_format()
    print(email, "-->", )
    user = User("andrey", "samoilenko", "polutech")
    fm = FormatNameToEmail.format_name_to_email(user, email_format)
# 5. output to file


# про вывод - сначала список найденных email ---- список найденных форматов+инструкция ---- возможные почты

# for i in tests:
#     e = EmailFormatSearch(i)
#     print(i, "-->", e.split_row_email(), "-->", e.get_control_email())
