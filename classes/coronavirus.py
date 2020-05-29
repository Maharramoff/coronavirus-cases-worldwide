from classes import Cache, TableScraper


class Coronavirus:
    __check_params = [None, 'All']
    __ignored_countries = ['Total',]
    __table_attribute = 'id'
    __attribute_value = 'main_table_countries_today'
    __website_url = 'https://www.worldometers.info/coronavirus/'
    __cache_ttl = 10
    __cache_file = 'cache/data.json'
    __cache_stat_file = 'cache/stat.json'
    __trs = None
    __cache_data = None
    __cache_stats_data = None
    __stats_columns = [
        'total_cases',
        'new_cases',
        'total_deaths',
        'new_deaths',
        'total_recovered',
        'new_recovered',
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
                if self.validate_row(tds[1:]):
                    rows.append(tds[1:7])
                if self.country not in self.__check_params and self.country in tds[1]:
                    return [tds[1:7]]
            self.cache.set(rows)
        return rows

    def get_stats(self):
        if self.__cache_stats_data is not None:
            return self.cache_stat.get()
        rows = []
        if self.__trs is not None:
            tds = self.table_scraper.get_tds(self.__trs[-1])
            rows = dict(zip(self.__stats_columns, tds[2:]))
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

    def validate_row(self, row):
        if any(word in row[0] for word in self.__ignored_countries) or len(row[0]) == 0:
            return False
        return True
