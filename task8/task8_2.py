# Задание 8_2
# Создайте класс, один из методов которого способен принимать не одиночный url, а массив url'ов и возвращать массив строк,
# полученных  из заголовков html страницек, которые вы получите из этих заданных url'ов.

import urllib.request, bs4, os
from concurrent.futures import ThreadPoolExecutor, as_completed


class Parser:
    def __init__(self, urls):
        self.urls = urls

    def _pars_html_title(self, url):
        soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
        return soup.title.string

    def get_result(self):
        out = []
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as pool:
            results = [pool.submit(self._pars_html_title, i) for i in self.urls]
            for future in as_completed(results):
                out.append(future.result())
        return list(map(str, out))


urls = ['https://yandex.ru/',
        'https://mail.ru/',
        'https://rambler.ru/',
        'https://google.ru/',
        'https://www.3dnews.ru/',
        'https://gitlab.com/',
        'https://github.com/',
        'https://bitbucket.org/',
        'https://www.ebay.com/',
        'https://www.avito.ru/',
        'http://www.bing.com/',
        'https://nikiladonya.github.io/',
        'http://www.sberbank.ru/',
        'https://alfabank.ru/',
        'http://www.rshb.ru/',
        'https://www.vtb24.ru/',
        'https://www.tinkoff.ru/',
        'https://www.open.ru/',
        'https://www.raiffeisen.ru/',
        'https://www.pochtabank.ru/']

a = Parser(urls)
print("\n".join(a.get_result()))
