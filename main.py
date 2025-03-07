import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text
# print(web_text)
soup = BeautifulSoup(web_page, 'html.parser')
h3_tag = soup.select(selector="h3.title")
title_rank = [text.getText() for text in h3_tag][::-1]
# print(title_rank)

for text in title_rank:
    try:
        with open("./movies.txt", mode='a') as fs:
            fs.write(text + '\n')
    except FileNotFoundError:
        with open("./movies.txt", 'w') as f:
            f.write(text + '\n')
