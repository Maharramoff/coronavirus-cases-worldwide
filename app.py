import flask

from classes import Coronavirus, Cache

app = flask.Flask(__name__, static_folder='static')


@app.route('/')
def home():
    covid19 = Coronavirus('All')
    columns = ['Ölkə', 'Xəstələr', 'Yeni Xəstələr', 'Ölüm', 'Yeni Ölüm', 'Sağalıb']
    rows = covid19.get_table_rows()
    stats = {k: v.replace(',', '') for (k, v) in covid19.get_stats().items()}
    return flask.render_template('home/index.html',
                                 stats=stats,
                                 rows=rows,
                                 columns=columns)


@app.route('/covid')
def covid():
    data = Cache('static/data/covid.json')
    return flask.render_template('covid/index.html', data=data.get())\



@app.route('/api/')
@app.route('/api/<stats>')
def api(stats=None):
    columns = [
        'country',
        'total_cases',
        'new_cases',
        'total_deaths',
        'new_deaths',
        'total_recovered',
    ]
    covid19 = Coronavirus()
    result = [dict(zip(columns, row)) for row in covid19.get_table_rows()] if stats is None else covid19.get_stats()
    return flask.jsonify(result)
