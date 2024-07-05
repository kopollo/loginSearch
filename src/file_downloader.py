import os
from bs4 import BeautifulSoup

import requests
from fake_useragent import UserAgent


class DocxFileDownloader:
    def __init__(self, company: str, filetype: str):
        # self.inurl = inurl
        self.num_results = 5
        self.company = company
        self.query = f"filetype:{filetype} inurl:{company}"
        self.links = self._find_docs()

    def _find_docs(self):
        url = f"https://www.google.com/search?q={self.query}&num={self.num_results}"
        ua = UserAgent()
        agent = ua.random
        headers = {"User-agent": agent}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        print(self.query, response.status_code)

        for result in soup.select("a"):
            href = result.get("href")
            if href.startswith("/url?q="):
                link = href.replace("/url?q=", "").split("&")[0]
                print(link)
                if link.endswith(".doc") or link.endswith(".docx"):
                    links.append(link)
        return links

    def save_docs(self):
        for i, link in enumerate(self.links):
            response = requests.get(link)
            address = f"upload/{self.company}/{i}.docx"
            directory = f"upload/{self.company}/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            # print(address)
            self.links.append(address)
            with open(address, "wb") as f:
                f.write(response.content)

    def get(self):
        return self.links


def save_docs(upload_path, links):

    ua = UserAgent()
    for i, link in enumerate(links):
        agent = ua.random
        headers = {"User-agent": agent}
        try:
            response = requests.get(link, headers=headers)
            if response.status_code != 200:
                continue
            # print(response.status_code)
            address = f"{upload_path}/{i}.docx"
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)
            # print(address)
            # self.links.append(address)
            with open(address, "wb") as f:
                f.write(response.content)
        except Exception:
            pass