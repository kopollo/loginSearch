# import argparse
# parser = argparse.ArgumentParser(description="Домен")
# parser.add_argument("-n", help="Введите домен компании")
from src.data_extracter import find_emails, get_document_text
from src.email_format_searcher import EmailFormatSearch
tests = ["a.b.brok@ma.ru", "samoylenkoKM@yandex.ru", "a.samolenko@google.com"]

# 1. Input data

# 2. find and download emails

# 3. find all emails in .docx
emails = find_emails("upload/test.docx")
print(emails)
# 4. Find all emails in .docx
for email in emails:
    e = EmailFormatSearch(email)
    print(email, "-->", e.get_control_email())
# 5. output to file

# про вывод - сначала список найденных email ---- список найденных форматов+инструкция ---- возможные почты

# for i in tests:
#     e = EmailFormatSearch(i)
#     print(i, "-->", e.split_row_email(), "-->", e.get_control_email())

