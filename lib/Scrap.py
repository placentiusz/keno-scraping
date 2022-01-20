import requests
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self, page):
        self.url = page
        self.html_content = ""


    def getData(self):
        self.html_content = requests.get(self.url,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}).text
        soup = BeautifulSoup(self.html_content, 'html.parser')
        rows = soup.find_all(class_="game-main-box skip-contrast")
        for row in rows:
            print(row)