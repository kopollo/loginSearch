import argparse
import os
from pathlib import Path

import click

from src.data_extracter import find_emails, get_document_text
from src.docx_file_downloader import DocxFileDownloader
from src.email_format_searcher import EmailFormatSearch
from src.format_name_to_email import FormatNameToEmail
from src.models import User, Email


def get_upload_path(url: str = "rosneft"):
    BASE_DIR = Path(__file__).resolve().parent
    upload_path = os.path.join(BASE_DIR, f"upload\\{url}")
    return upload_path


def get_save_path(save_path: str):
    BASE_DIR = Path(__file__).resolve().parent
    p = os.path.join(BASE_DIR, save_path)
    return p


def add_paragraph_with_finded_email(save_path, emails: list):
    with open(save_path, 'a') as f:
        print("Finded emails:", file=f)
        print("----------------", file=f)
        for email in emails:
            print(email, file=f)
        print("", file=f)


def add_paragraph_with_email_formats(save_path, email_formats: list[Email]):
    with open(save_path, 'a') as f:
        print("email formats:", file=f)
        print("----------------", file=f)
        for email in email_formats:
            print(email.pretty(), file=f)
        print("", file=f)


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
    for file in files:
        path = os.path.join(upload_path, file)
        emails += find_emails(path)
    add_paragraph_with_finded_email(save_path, emails)

    # 4. Find all email formats
    for email in emails:
        email_format = EmailFormatSearch(email).get_email_format()
        email_formats.append(email_format)

    add_paragraph_with_email_formats(save_path, email_formats)

    # 5. Try user
    for email_format in email_formats:
        user = User("Андрей", "Самойленко", "Сергеевич")
        fm = FormatNameToEmail.format_name_to_email(user.transliterate(), email_format)
        print(fm)
        pass


main()
