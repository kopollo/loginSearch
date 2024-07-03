# import argparse
# from src.data_extracter import DataExtractor
# from src.email_format_searcher import EmailFormatSearch
# from src.format_name_to_email import EmailFromFormat
# parser = argparse.ArgumentParser(description="Домен")
# parser.add_argument("-n", help="Введите домен компании")
# args = parser.parse_args()
# # print(args.n)
# import docx
# # dt = DataExtractor("testdoc.docx")
# # dt.save_docs()
#
#
# EmailFormatSearch
from src.data_extracter import find_emails, get_document_text
from src.email_format_searcher import EmailFormatSearch
tests = ["a.b.brok@ma.ru", "samoylenkoKM@yandex.ru", "a.samolenko@google.com"]

for i in tests:
    e = EmailFormatSearch(i)
    print(i, "-->", e.split_row_email(), "-->", e.get_control_email())
# print(find_emails(get_document_text("src/testdoc.docx")))

# print(r)

