import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class DocsGoogleSearcher:
    SEARCH_URL = "https://www.google.com/search"
    MAX_TRIES = 5

    def get_file_urls(self, company: str, filetype: str) -> (list[str], int):
        """
        Sends GET requests to google.com/search to extract documents associated with given company.

        :param company: name of the company to search associated files for (example: google)
        :param filetype: file extension without dot  (example: docx)
        :return: tuple (list of file urls, GET response status code)
        """

        q = f"inurl:{company} filetype:{filetype}"
        ua = UserAgent()
        page_number = 0
        docx_urls = []
        tries = 1
        while True:
            agent = ua.random
            # print("User agent: ", agent)
            url = self.SEARCH_URL
            response = requests.get(
                url, params={"q": q, "filter": 0, "start": page_number, "num": 100}, headers={"User-agent": agent},
                timeout=10
            )

            # print("URL: ", response.url)
            # print("status code: ", response.status_code)

            if response.status_code == 200:
                bs = BeautifulSoup(response.text, 'html.parser')
                links = bs.find_all('a', href=True)
                links_counter = 0

                for link in links:
                    if "." + filetype in link['href']:
                        docx_urls.append(link['href'])
                        # print(link['href'])
                        links_counter += 1

                # print("links on page: ", links_counter)
                if links_counter == 0:
                    break

                page_number += 100
            else:
                if tries >= self.MAX_TRIES:
                    break
                tries += 1
            break
        # print("start param: ", page_number)
        # print("tries: ", tries)
        return docx_urls, response.status_code


def main():
    searcher = DocsGoogleSearcher()
    docs, code = searcher.get_file_urls("rosneft", "docx")
    print(len(docs))
    print(docs)
    print(code)


if __name__ == '__main__':
    main()
