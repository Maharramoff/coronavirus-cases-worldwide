import flask

from classes import Coronavirus, Cache, Api, Cabmin

app = flask.Flask(__name__, static_folder='static')
app.config['JSON_AS_ASCII'] = False


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
    return flask.render_template('covid/index.html', data=data.get())


@app.route('/news')
def news():
    cabmin = Cabmin(news_limit=30)
    return flask.render_template('news/index.html', data=cabmin.news())


@app.route('/api/')
@app.route('/api/<params>')
def api(params=None):
    return flask.jsonify(Api(params).response())
