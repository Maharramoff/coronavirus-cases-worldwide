import requests
from bs4 import BeautifulSoup


class TableScraper:
    table = []

    def __init__(self, url, attr, value):
        self.url = url
        self.attr = attr
        self.value = value

    def get_data(self):
        html = requests.get(self.url)
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup.find('table', {self.attr: self.value})

    def get_trs(self):
        table = self.get_data()
        return [] if table is None else table.find_all('tr')

    @staticmethod
    def get_tds(tr):
        return [td.get_text(strip=True) for td in tr.find_all('td')]