import requests
import random
from lxml.html import fromstring

url = 'https://free-proxy-list.net/anonymous-proxy.html'
response = requests.get(url)
parser = fromstring(response.text)
proxies = []

for i in parser.xpath('//tbody/tr')[:20]:
    if i.xpath('.//td[7][contains(text(),"yes")]'):
        proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                          i.xpath('.//td[2]/text()')[0]])

    try:
        t = requests.get("https://www.google.com/",
                         proxies={"http": proxy, "https": proxy}, timeout=5)
        if t.status_code == requests.codes.ok:
            proxies.append(proxy)
    except:
        pass

proxy = proxies[random.randint(0, len(proxies) - 1)]

response = requests.get('https://websiteiwantget',
                        proxies={"http": proxy, "https": proxy})
