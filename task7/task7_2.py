# Задание 7_2
# Напишите класс, который запрашивает содержимое веб-странички с помощью стандартной библиотеки urllib.request и
# вытаскивает у нее заголовок (содержимое тэга title) любым придуманным вами способом.

import urllib.request, bs4

def _pars_html_title(self, url):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    return soup.title.string
