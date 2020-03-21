import flask

from classes.coronavirus import Coronavirus

app = flask.Flask(__name__, static_folder='static')


@app.route('/')
def index():
    covid = Coronavirus('All')
    columns = ['Ölkə', 'Xəstələr', 'Yeni Xəstələr', 'Ölüm', 'Yeni Ölüm', 'Sağalıb']
    rows = covid.get_table_rows()
    stats = {k: v.replace(',', '') for (k, v) in covid.get_stats().items()}
    return flask.render_template('home/index.html',
                                 stats=stats,
                                 rows=rows,
                                 columns=columns)
