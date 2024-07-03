# # import docx
# # import re
# #
# #
# # class DataExtractor:
# #     def __init__(self, file_path):
# #         self.document = docx.Document(file_path)
# #
# #         return self.find_names(metadata_text)
# #
# #     def get_document_text(self) -> str:
# #         document_text = ''
# #         for paragraph in self.document.paragraphs:
# #             document_text += paragraph.text + '\n'
# #
# #         return document_text
# #
# #     def get_metadata_text(self) -> str:
# #         metadata_text = ''
# #         core_properties = self.document.core_properties
# #
# #         # Converge all metadata properties into a single string
# #         attributes = dir(core_properties)
# #         for attribute in attributes:
# #             if attribute.startswith('_'):
# #                 continue
# #
# #     def extract_emails(self, file_path: str) -> list[str]:
# #         document_text = self.get_document_text()
# #         return self.find_emails(document_text)
# #
# #
# #     def extract_names(self, file_path: str) -> list[str]:
# #         metadata_text = self.get_metadata_text()
# #             property = getattr(core_properties, attribute)
# #             if property is None or len(str(property)) == 0:
# #                 continue
# #
# #             metadata_text += str(property) + ' '
# #
# #         return metadata_text
# #     # Finds all [unique] email occurrences in a text
# #     def find_emails(self, text: str) -> list[str]:
# #         email_pattern = re.compile(r'[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# #         return list(set(re.findall(email_pattern, text)))
# #
# #     # Finds all [unique] name occurrences in a text
# #     def find_names(self, text: str) -> list[str]:
# #         # TODO: Instead of pattern-based search implement concurrence finder (Name DB or smth.)
# #         name_pattern = re.compile(r'\b[A-Z][a-z]*\b')
# #         return list(set(re.findall(name_pattern, text)))
#
#
# import re
#
# import docx2txt
#
#
# def extract_text_from_docx(filename):
#     text = docx2txt.process(filename)
#     print(text)
#     return text
#
#
# def find_emails(text: str) -> list[str]:
#     email_pattern = re.compile(r'[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#     return list(set(re.findall(email_pattern, text)))
#
#
# print(find_emails(extract_text_from_docx("testdoc.docx")))

import re
import zipfile


def get_document_text(file_path):
    with zipfile.ZipFile(file_path, 'r') as docx:
        full_text = []
        for file_info in docx.infolist():
            if not file_info.filename.endswith('.xml'):
                continue
            with docx.open(file_info.filename) as xml_file:
                xml_content = xml_file.read().decode('utf-8')
                full_text.append(xml_content)
        full_text = '\n'.join(full_text)
        return full_text


def find_emails(text: str) -> list[str]:
    email_pattern = re.compile(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    return list(set(re.findall(email_pattern, text)))

