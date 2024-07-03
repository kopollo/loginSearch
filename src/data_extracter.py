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


def find_emails(file_path) -> list[str]:
    text = get_document_text(file_path)
    email_pattern = re.compile(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    return list(set(re.findall(email_pattern, text)))


