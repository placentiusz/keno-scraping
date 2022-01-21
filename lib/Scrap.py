from datetime import datetime

import requests
from bs4 import BeautifulSoup


class Scrap:
    def __init__(self, page):
        self.url = page
        self.html_content = ""

    def get_keno_data(self):
        self.html_content = requests.get(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            },
        ).text
        soup = BeautifulSoup(self.html_content, "html.parser")
        rows = soup.find_all(class_="game-main-box skip-contrast")
        results = []
        for row in rows:
            date_from_page = (
                row.find_all("p", class_="sg__desc-title")[0]
                .text.replace(",", "")
                .strip()
                .split()
            )
            date = datetime.strptime(
                f'{date_from_page[1]} {date_from_page[3]}', "%d.%m.%Y %H:%M"
            )
            result = " ".join(
                row.find_all(class_="multi-keno-special-box")[0].text.strip().split()
            )
            number = row.find_all("p", class_="result-item__number")[0].text.strip()
            if len(result.split()) == 20 and number is not None:
                results.append((date, result, number))

        return results
