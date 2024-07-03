import os
from bs4 import BeautifulSoup

import requests


class DocxFileDownloader:
    def __init__(self, inurl):
        self.inurl = inurl
        self.num_results = 5
        self.links = self._find_docs()
        # print(self.links)

    def _find_docs(self):
        query = f"filetype:docx inurl:{self.inurl}"
        print(query)
        url = f"https://www.google.com/search?q={query}&num={self.num_results}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
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
            address = f"upload/{self.inurl}/{i}.docx"
            directory = f"upload/{self.inurl}/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            print(address)
            with open(address, "wb") as f:
                f.write(response.content)
