# import argparse
# parser = argparse.ArgumentParser(description="Домен")
# parser.add_argument("-n", help="Введите домен компании")
import os
from pathlib import Path

from src.data_extracter import find_emails, get_document_text
from src.docx_file_downloader import DocxFileDownloader
from src.email_format_searcher import EmailFormatSearch
from src.format_name_to_email import FormatNameToEmail
from src.models import User


def get_upload_path(url: str = "rosneft"):
    BASE_DIR = Path(__file__).resolve().parent
    upload_path = os.path.join(BASE_DIR, f"upload\\{url}")
    return upload_path


# 1. Input data

upload_path = get_upload_path("test")
# print(upload_path)
# 2. find and download emails
# file_links = DocxFileDownloader("rosneft").get()

# 3. find all emails in .docx
emails = []
files = os.listdir(upload_path)
for file in files:
    path = os.path.join(upload_path, file)
    emails += find_emails(path)

# print(emails)
# # 4. Find all email formats
for email in emails:
    email_format = EmailFormatSearch(email).get_email_format()
    # print(email, "-->", email_format.pretty())
    user = User("Андрей", "Самойленко", "Сергеевич")
    fm = FormatNameToEmail.format_name_to_email(user.transliterate(), email_format)
    print(fm)
    # print(fm)

# # 6. Find supposed logins

# # 5. output to file

# # про вывод - сначала список найденных email ---- список найденных форматов+инструкция ---- возможные почты
