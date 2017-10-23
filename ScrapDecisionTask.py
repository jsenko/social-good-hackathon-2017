import asyncio

import aiohttp
import json
from bs4 import BeautifulSoup

class ScrapDecisionTask:

    def __init__(self, client):
        self._client = client
        pass

    @asyncio.coroutine
    def run(self, url):
        # curl 'http://www.nsoud.cz/JudikaturaNS_new/judikatura_vks.nsf/WebSearch/2E2DE10A653D90E9C1257A920066D543?openDocument'
        # -H 'Host: www.nsoud.cz' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://www.nsoud.cz/Judikaturans_new/judikatura_vks.nsf/$$WebSearch1?SearchView&Query=%5Bidstrediska%5D%3D040%20AND%20(%5Busek%5D%3DObchod%20OR%20%5Busek%5D%3DObcan%20OR%20%5Busek%5D%3DCivil)&SearchMax=0Start=1&Count=15&pohled=1&searchOrder=4' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1'
        # -H 'If-Modified-Since: Sat, 21 Oct 2017 18:47:18 GMT'
        # -H 'Cache-Control: max-age=0'
        html_raw = yield from self._client.get("http://www.nsoud.cz/JudikaturaNS_new/judikatura_vks.nsf/WebPrint/2E2DE10A653D90E9C1257A920066D543?openDocument")
                                          # replace WebSearch/WebPrint
        soup = BeautifulSoup(html_raw, 'html.parser')
        #print(soup.prettify())
        data = {}
        key = None
        for td in soup.find_all('td'):
            if key is None:
                key = td.get_text()
            else:
                data[key] = td.get_text()
                key = None

        soup.find_all('head')[0].decompose()
        for style in soup.find_all('style'): style.decompose()
        soup.find_all('table')[0].decompose()
        divs = soup.find_all('div')
        for i in range(0, 2): divs[i].decompose()
        text = soup.get_text()
        data["text"] = text
        return data
