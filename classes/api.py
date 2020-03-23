import json


class Api:

    def __init__(self, params, cache, coronavirus):
        self.params = params
        self.cache = cache
        self.coronavirus = coronavirus()

    def response(self) -> list:
        if self.params == 'stats':
            result = self.coronavirus.get_stats()
        elif self.params == 'articles':
            result = self.cache('static/data/covid.json').get()
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
