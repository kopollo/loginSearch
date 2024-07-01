import requests
from bs4 import BeautifulSoup

query = "filetype:docx inurl:cat"
num_results = 15

# url = f"https://www.google.com/search?q={query}&num={num_results}"
url = f"https://www.google.com/search?q={query}&num={num_results}"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# print(response.content)
links = []
print(response.content)
# for result in soup.select("a"):
#     print(href)
#     href = result.get("href")
#     if href.startswith("/url?"):
#         pass
# #         link = href.replace("/url?q=", "").split("&")[0]
# #         links.append(link)
# #
# # print(links)
links = []
for result in soup.select("a"):
    href = result.get("href")
    if href.startswith("/url?q="):
        link = href.replace("/url?q=", "").split("&")[0]
        if link.endswith(".doc") or link.endswith(".docx"):
            links.append(link)
for link in links:
    print(link)
