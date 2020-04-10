import re
import requests
import yaml

from classes import Cache


class LocalStats:
    __website_url = 'https://koronavirusinfo.az/az/page/statistika/azerbaycanda-cari-veziyyet'
    __cache_ttl = 24 * 60 * 60
    __cache_file = 'cache/local_stats.json'

    def __init__(self):
        self.html = requests.get(self.__website_url)
        self.cache = Cache(self.__cache_file)

    def get_data(self):
        cached_data = self.cache.get()
        if None is not self.cache.time_diff() < self.__cache_ttl:
            return cached_data
        dd = r'countryStat([\s\S]*?)\]'
        result = re.search(dd, self.html.text)
        safe_list = yaml.safe_load(u"".join(result[0].split())
                                   .replace("countryStat=", "")
                                   .replace(",]", "]")
                                   .replace(":", ": "))
        result = [{k: str(v) for k, v in d.items()} for d in safe_list]
        self.cache.set(result)
        return result
