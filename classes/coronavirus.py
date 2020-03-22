import os
import requests
from bs4 import BeautifulSoup
import json
import time


class Cache:

    def __init__(self, file):
        self.file = file

    def time_diff(self):
        if os.path.isfile(self.file):
            last_time = int(os.path.getmtime(self.file))
            current_time = int(time.time())
            return current_time - last_time
        return None

    def set(self, data) -> None:
        if len(data) == 0:
            return None
        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        with open(self.file, 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        pass

    def get(self):
        try:
            with open(self.file, encoding="utf8") as json_file:
                return json.load(json_file)
        except EnvironmentError:
            return None


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


class Coronavirus:
    __check_params = [None, 'All']
    __table_attribute = 'id'
    __attribute_value = 'main_table_countries_today'
    __website_url = 'https://www.worldometers.info/coronavirus/'
    __cache_ttl = 5 * 60
    __cache_file = 'cache/data.json'
    __cache_stat_file = 'cache/stat.json'
    __trs = None
    __cache_data = None
    __cache_stats_data = None
    __stats_columns = [
        'total_title',
        'total_cases',
        'new_cases',
        'total_deaths',
        'new_deaths',
        'total_recovered',
        'active_cases',
        'critical_cases',
        'per_mln',
    ]

    def __init__(self, country=None):
        self.country = country
        self.cache = Cache(self.__cache_file)
        self.cache_stat = Cache(self.__cache_stat_file)
        self.table_scraper = TableScraper(self.__website_url, self.__table_attribute, self.__attribute_value)
        self.__prepare_table_data()

    def get_table_rows(self):
        if self.__cache_data is not None:
            return self.cache.get()
        rows = []
        if self.__trs is not None:
            for tr in self.__trs[1:-1]:
                tds = self.table_scraper.get_tds(tr)
                rows.append(tds[:6])
                if self.country not in self.__check_params and self.country in tds[0]:
                    return [tds[:6]]
            self.cache.set(rows)
        return rows

    def get_stats(self):
        if self.__cache_stats_data is not None:
            return self.cache_stat.get()
        rows = []
        if self.__trs is not None:
            tds = self.table_scraper.get_tds(self.__trs[-1])
            rows = dict(zip(self.__stats_columns, tds))
            self.cache_stat.set(rows)
        return rows

    def __prepare_table_data(self) -> None:
        if None is not self.cache.time_diff() < self.__cache_ttl or \
                None is not self.cache_stat.time_diff() < self.__cache_ttl:
            self.__cache_data = self.cache.get()
            self.__cache_stats_data = self.cache_stat.get()
        else:
            self.__trs = self.table_scraper.get_trs()
        pass
