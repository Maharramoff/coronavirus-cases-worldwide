from operator import itemgetter

import requests
from bs4 import BeautifulSoup
from classes import Cache
import re


class Cabmin:
    __page_num = 0
    __stop_num = "675"
    __raw_article = True
    __search_words = ['virus', 'yolux', 'covid', 'karantin', 'xəstə']
    __cache_ttl = 30 * 60
    __cache_file = 'cache/news.json'

    def __init__(self, news_limit=20):
        self.limit = news_limit
        self.cache = Cache(self.__cache_file)

    def news(self):
        cached_data = self.cache.get()
        if None is not self.cache.time_diff() < self.__cache_ttl:
            return cached_data
        found = 0
        first_run = False
        if cached_data is None:
            first_run = True
            cached_data = []
        while True:
            url = 'https://cabmin.gov.az/themes/getArticle.php?pagenum=' + str(self.__page_num)
            html = requests.get(url).text
            latest_article_num = cached_data[0]['id'] if first_run is False else self.__stop_num
            # Xəbər yeni deyilsə axtarışı dayandırırıq
            if 'article/' + self.__stop_num in html or (found == self.limit and self.limit is not None):
                break
            # Xəbər koronavirusla bağlıdırsa
            if any(word in html for word in self.__search_words):
                soup = BeautifulSoup(html, "html.parser")
                title = soup.find('div', {'class': 'articleTitle'}).text
                date_time = self.extract_date_time(html)
                article_num = self.get_article_number(soup)
                if article_num <= latest_article_num and first_run is False:
                    break
                article = soup.find('div', style=lambda value: value and 'text-align' in value).extract()
                if not self.__raw_article:
                    paragraphs = article.find_all('p')
                    article = '<br/>'.join([p.get_text(strip=False).replace(u'\xa0', u' ') for p in paragraphs])
                if 'style' in article.attrs:
                    del article.attrs['style']
                row = {'id': article_num, 'datetime': date_time, 'title': title, 'body': str(article)}
                cached_data.append(row)
                found += 1
            self.__page_num += 1
        newlist = sorted(cached_data, key=itemgetter('id'), reverse=True)
        self.cache.set(newlist)
        return newlist

    def get_article_number(self, soup):
        article_href = soup.find('div', {'class': 'article'}).attrs.get('data-href')
        return self.extract_digit(article_href)

    @staticmethod
    def extract_digit(txt):
        return ''.join(filter(str.isdigit, txt))

    @staticmethod
    def extract_date_time(txt):
        dd = r'(0[1-9]|[12]\d|3[01])'
        months = '(Yanvar|Fevral|Mart|Aprel|May|Iyun|Iyul|Avqust|((Senty|Okty|Noy|Dek)abr))'
        year = r'[12]\d{3}'
        hhmm = '([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
        result = re.search('(' + dd + ' ' + months + ' ' + year + ' - ' + hhmm + ')', txt)
        return result[0]
