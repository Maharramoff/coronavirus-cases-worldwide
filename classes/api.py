from classes import Coronavirus, Cache, Cabmin, LocalStats


class Api:

    def __init__(self, params):
        self.params = params
        self.coronavirus = Coronavirus()

    def response(self) -> list:
        if self.params == 'stats':
            result = self.coronavirus.get_stats()
        elif self.params == 'articles':
            result = Cache('static/data/covid.json').get()
        elif self.params == 'news':
            result = Cabmin(news_limit=None).news()
        elif self.params == 'local_stats':
            result = LocalStats().get_data()
        elif self.params == 'timeline':
            result = Cache('static/data/timeline.json').get()
        else:
            columns = [
                'country',
                'total_cases',
                'new_cases',
                'total_deaths',
                'new_deaths',
                'total_recovered',
            ]
            result = [dict(zip(columns, row)) for row in self.coronavirus.get_table_rows()]
        return result
