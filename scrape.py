import os
import pandas as panda
import requests
from bs4 import BeautifulSoup
import flask
import json
import time

app = flask.Flask(__name__)


class Coronavirus:
    __check_params = [None, 'All']
    __table_attribute = 'id'
    __attribute_value = 'main_table_countries_today'
    __website_url = 'http://www.worldometers.info/coronavirus'
    __result = []
    __cache_ttl = 15 * 1
    __cache_file = 'cache/data.json'

    def __init__(self, country=None):
        self.country = country

    def get_result(self):
        if None is not self.cache_time_diff() < self.__cache_ttl:
            return self.get_local_data()
        table = self.get_remote_data()
        trs = self.__find_all_trs(table)
        rows = []
        for tr in trs[1:-1]:
            tds = self.__find_all_tds(tr)
            rows.append(tds[:6])
            if self.country not in self.__check_params and self.country in tds[0]:
                return [tds[:6]]
        self.cache_set(rows)
        return rows

    def cache_set(self, rows) -> None:
        if len(rows) == 0:
            return None
        os.makedirs(os.path.dirname(self.__cache_file), exist_ok=True)
        with open(self.__cache_file, 'w+', encoding='utf-8') as f:
            json.dump(rows, f, ensure_ascii=False, indent=4)
        pass

    def cache_get(self):
        try:
            with open(self.__cache_file) as json_file:
                return json.load(json_file)
        except EnvironmentError:
            return None

    def cache_time_diff(self):
        if os.path.isfile(self.__cache_file):
            last_time = int(os.path.getmtime(self.__cache_file))
            current_time = int(time.time())
            return current_time - last_time
        return None

    def get_remote_data(self):
        html = requests.get(self.__website_url)
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup.find('table', {self.__table_attribute: self.__attribute_value})

    def get_local_data(self):
        return self.cache_get()

    @staticmethod
    def __find_all_trs(table):
        return [] if table is None else table.find_all('tr')

    @staticmethod
    def __find_all_tds(tr):
        return [td.get_text(strip=True) for td in tr.find_all('td')]


@app.route('/')
def index():
    covid = Coronavirus('All')
    columns = ['Ölkə', 'Xəstələr', 'Yeni Xəstələr', 'Ölüm', 'Yeni Ölüm', 'Sağalıb']
    panda.set_option('display.max_rows', None)
    rows = covid.get_result()
    panda_table = panda.DataFrame(rows, columns=columns)
    return flask.render_template('index.html',
                                 mixed=rows,
                                 table=panda_table.to_html(header='true', classes=['display', 'compact'], border=0,
                                                           justify='left'))
