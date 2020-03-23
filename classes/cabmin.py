import requests
from bs4 import BeautifulSoup
from classes import Cache


class Cabmin:
    __page_num = 0
    __stop_word = "article/675"
    __raw_article = True
    __search_words = ['koronavirus', 'məqsədilə']
    __cache_ttl = 5 * 60
    __cache_file = 'cache/news.json'

    def __init__(self, news_limit=20):
        self.limit = news_limit
        self.cache = Cache(self.__cache_file)

    def news(self):
        if None is not self.cache.time_diff() < self.__cache_ttl:
            return self.cache.get()
        articles = []
        found = 0
        while True:
            url = 'https://cabmin.gov.az/themes/getArticle.php?pagenum=' + str(self.__page_num)
            html = requests.get(url).text
            # Xəbər 24 fevraldan əvvələ aiddirsə axtarışı dayandırırıq
            if self.__stop_word in html or found == self.limit:
                break
            # Xəbər koronavirusla bağlıdırsa
            if any(word in html for word in self.__search_words):
                soup = BeautifulSoup(html, "html.parser")
                title = soup.find('div', {'class': 'articleTitle'}).text
                article = str(soup.find('div', style=lambda value: value and 'text-align' in value).extract())
                if not self.__raw_article:
                    paragraphs = article.find_all('p')
                    article = '<br/>'.join([p.get_text(strip=False).replace(u'\xa0', u' ') for p in paragraphs])
                row = {'title': title, 'body': article}
                articles.append(row)
                found += 1
            self.__page_num += 1
        self.cache.set(articles)
        return articles
