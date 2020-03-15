import pandas as panda
import requests
from bs4 import BeautifulSoup
import flask

app = flask.Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Confirmed Coronavirus Cases and Deaths by Country</title>
    <link rel="shortcut icon" type="image/x-icon" href="https://www.herokucdn.com/favicons/favicon.ico"/>
    <link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://www.herokucdn.com/favicons/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://www.herokucdn.com/favicons/apple-touch-icon-152x152.png">
    <link rel="mask-icon" href="https://www.herokucdn.com/favicons/icon.svg" color="#79589F">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
    
</head>
<body>
<div class="container p-3">
    <div class="row">
        <div class="col-12">
            <div class="table-responsive">
                {{table | safe}}
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
<script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('.dataframe').DataTable({
        "paging": false,
        "info":   false
    });
} );
</script>
</body>
</html>
"""
 
class Coronavirus:
    __check_params = [None, 'All']
    __table_attribute = 'id'
    __attribute_value = 'main_table_countries'
    __website_url = 'http://www.worldometers.info/coronavirus'
 
    def __init__(self, country=None):
        self.country = country
        html = requests.get(self.__website_url)
        soup = BeautifulSoup(html.text, 'html.parser')
        self.table = soup.find('table', {self.__table_attribute: self.__attribute_value})
 
    def get_result(self):
        trs = self.find_all_trs()
        rows = []
        for tr in trs[1:]:
            tds = self.__find_all_tds(tr)
            rows.append(tds[:6])
            if self.country not in self.__check_params and self.country in tds[0]:
                return [tds[:6]]
        return rows
 
    def find_all_trs(self):
        return self.table.find_all('tr')
 
    @staticmethod
    def __find_all_tds(tr):
        return [td.get_text(strip=True) for td in tr.find_all('td')]
    
    
@app.route('/') 
def index():
    covid = Coronavirus('All')
    columns = ['Ölkə', 'Xəstələr', 'Yeni Xəstələr', 'Ölüm', 'Yeni Ölüm', 'Sağalıb']
    panda.set_option('display.max_rows', None)
    panda_table = panda.DataFrame(covid.get_result(), columns=columns)
    return flask.render_template_string (html, table = panda_table.to_html (header = 'true', classes='display', border = 0, justify='left'))

