import argparse
import os
from pathlib import Path

import click

from src.data_extracter import find_emails, get_document_text
from src.docx_file_downloader import DocxFileDownloader
from src.email_format_searcher import EmailFormatSearch
from src.format_name_to_email import FormatNameToEmail
from src.models import User, Email
from src.formatter import Formatter


def get_upload_path(url: str = "rosneft"):
    BASE_DIR = Path(__file__).resolve().parent
    upload_path = os.path.join(BASE_DIR, f"upload\\{url}")
    return upload_path


def get_save_path(save_path: str):
    BASE_DIR = Path(__file__).resolve().parent
    p = os.path.join(BASE_DIR, save_path)
    return p


@click.command()
@click.argument('domain')
@click.option(
    '--save_path', '-sp',
    help='path where you want to save result',
)
def main(domain, save_path):
    # 1. Input data
    upload_path = get_upload_path("test")
    # save_path = get_save_path(save_path)
    print(save_path)
    # 2. find and download emails
    # file_links = DocxFileDownloader("rosneft").get()

    # 3. find all emails in .docx
    emails = []
    email_formats = []
    files = os.listdir(upload_path)
    formatter = Formatter(save_path)
    for file in files:
        path = os.path.join(upload_path, file)
        emails += find_emails(path)
    formatter.add_paragraph_with_finded_email(emails)

    # 4. Find all email formats
    for email in emails:
        email_format = EmailFormatSearch(email).get_email_format()
        email_formats.append(email_format)
    # 5. Find all users from metadata
    users = [
        User("Андрей", "Самойленко", "Сергеевич"),
        User("Владислав", "Иванов", "ivanovich")
    ]
    formatter.add_paragraph_with_email_formats(email_formats)

    formatter.add_paragraph_with_users(users)
    # 6. Suppose all user logins
    for user in users:
        for email_format in email_formats:
            fm = FormatNameToEmail.format_name_to_email(user.transliterate(), email_format)
            formatter.add_paragraph_with_user_logins(user, email_format, fm)


main()
