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
            with open(self.file) as json_file:
                return json.load(json_file)
        except EnvironmentError:
            return None


class Coronavirus:
    __check_params = [None, 'All']
    __table_attribute = 'id'
    __attribute_value = 'main_table_countries_today'
    __website_url = 'http://www.worldometers.info/coronavirus'
    __result = []
    __cache_ttl = 15 * 60
    __cache_file = 'cache/data.json'

    def __init__(self, country=None):
        self.country = country
        self.cache = Cache(self.__cache_file)

    def get_result(self):
        if None is not self.cache.time_diff() < self.__cache_ttl:
            return self.__get_local_data()
        table = self.__get_remote_data()
        trs = self.__find_all_trs(table)
        rows = []
        for tr in trs[1:-1]:
            tds = self.__find_all_tds(tr)
            rows.append(tds[:6])
            if self.country not in self.__check_params and self.country in tds[0]:
                return [tds[:6]]
        self.cache.set(rows)
        return rows

    def __get_remote_data(self):
        html = requests.get(self.__website_url)
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup.find('table', {self.__table_attribute: self.__attribute_value})

    def __get_local_data(self):
        return self.cache.get()

    @staticmethod
    def __find_all_trs(table):
        return [] if table is None else table.find_all('tr')

    @staticmethod
    def __find_all_tds(tr):
        return [td.get_text(strip=True) for td in tr.find_all('td')]