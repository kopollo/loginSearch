import argparse
import os
from pathlib import Path

import click
import requests

from src.data_extracter import find_emails, get_document_text
from src.DocsGoogleSearcher import DocsGoogleSearcher
from src.email_format_searcher import EmailFormatSearch
from src.format_name_to_email import FormatNameToEmail
from src.models import User, Email
from src.formatter import Formatter
from src.file_downloader import DocxFileDownloader, save_docs


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
    upload_path = get_upload_path(domain)
    # save_path = get_save_path(save_path)
    print(save_path)

    # 2. find and download emails
    # python cli.py rosneft -sp text2.txt

    # links = ["https://tender.rosneft.ru/files/sales/tt84692-28_06_2024_0.docx",
    #          "https://zrnao.ru/assets/files/Uved/2022/Rosneft.docx"]
    links = ['https://rosneft-azs.ru/upload/site1/document_event/000/062/460/Spisok_AZS_Moskva.docx', 'https://tender.rosneft.ru/files/sales/tt71088-26_11_2021_1.docx', 'https://tender.rosneft.ru/files/sales/tt79619-20_07_2023_1.docx', 'https://rosneft-azs.ru/upload/site1/document_event/000/156/827/Pravila_Aktsii_Piknik.docx', 'https://tender.rosneft.ru/files/sales/tt67104-15_01_2021_1.docx', 'https://zrnao.ru/assets/files/Uved/2022/Rosneft.docx', 'https://tender.rosneft.ru/files/refining/tt59522-19_08_2019_0.docx', 'https://tender.rosneft.ru/files/sales/tt64782-21_07_2020_1.docx', 'https://www.tektorg.ru/documents/rosneft/importozameshchenie/%D0%9F%D0%B5%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%86%D0%B8%D0%B8%20%D0%9C%D0%B8%D0%BD%D0%BF%D1%80%D0%BE%D0%BC%D1%82%D0%BE%D1%80%D0%B3.docx', 'https://www.temryuk.ru/administratsiya/obshchslush/files/protocol-slushaniy-rosneft-27.01.2022.docx', 'https://severgazbank.ru/upload/iblock/d6e/tj0jcn3p2lu6gtlj27mdg52pi9w38tpj/O-korporativnom-deystvii-Godovoe-obshchee-sobranie-aktsionerov-emitenta-PAO-NK-Rosneft-ot-28.05.2024.docx', 'https://tender.rosneft.ru/files/sales/tt78149-04_05_2023_2.docx', 'https://tender.rosneft.ru/files/sales/tt77241-20_02_2023_1.docx', 'https://tender.rosneft.ru/files/sales/tt76148-28_12_2022_1.docx', 'https://tender.rosneft.ru/files/sales/tt68730-11_06_2021_1.docx', 'https://tender.rosneft.ru/files/sales/tt84692-28_06_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt74812-08_09_2022_1.docx', 'https://tender.rosneft.ru/files/sales/tt62469-06_02_2020_0.docx', 'https://tender.rosneft.ru/files/sales/tt79397-25_07_2023_1.docx', 'https://tender.rosneft.ru/files/sales/tt77900-05_04_2023_1.docx', 'https://tender.rosneft.ru/files/sales/tt65793-05_10_2020_1.docx', 'https://tender.rosneft.ru/files/sales/tt83486-14_03_2024_5.docx', 'https://tender.rosneft.ru/files/sales/tt84810-25_06_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt82402-22_12_2023_5.docx', 'https://tender.rosneft.ru/files/sales/tt83877-18_04_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt84501-27_05_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt61620-27_01_2020_1.docx', 'https://tender.rosneft.ru/files/sales/tt68849-21_07_2021_1.docx', 'https://tender.rosneft.ru/files/sales/tt84802-25_06_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt83225-01_03_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt84484-27_05_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt84491-27_05_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt85290-24_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt84485-27_05_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt83878-18_04_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt85134-01_08_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt85292-24_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt85289-24_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt68494-25_05_2021_1.docx', 'https://tender.rosneft.ru/files/sales/tt78182-19_05_2023_1.docx', 'https://tender.rosneft.ru/files/sales/tt76436-16_12_2022_0.docx', 'https://tender.rosneft.ru/files/sales/tt84804-25_06_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt84488-27_05_2024_1.docx', 'https://tender.rosneft.ru/files/sales/tt85295-24_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt77248-28_02_2023_5.docx', 'https://tender.rosneft.ru/files/sales/tt85291-24_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt85314-25_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt85294-24_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt85293-24_07_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt84133-26_04_2024_5.docx', 'https://tender.rosneft.ru/files/sales/tt68353-17_05_2021_0.docx', 'https://tender.rosneft.ru/files/sales/tt85135-01_08_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt85133-01_08_2024_0.docx', 'https://tender.rosneft.ru/files/sales/tt75602-21_10_2022_2.docx', 'https://tender.rosneft.ru/files/sales/tt85131-01_08_2024_0.docx',]
    # links = links[:10]
    # print(links)
    save_docs(upload_path, links)
    # TODO - написать ограничитель на Commands до 3 штук

    # searcher = DocsGoogleSearcher()
    # docs, code = searcher.get_file_urls("rosneft", "docx")
    # print(docs, code)

    # searcher = DocxFileDownloader("rosneft", "docx")
    # searcher.save_docs()
    # print(searcher.get())

    # save_docs(docs)
    # for link in docs:
    #     print(link)
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
