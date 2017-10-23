import asyncio

import aiohttp
import json
from bs4 import BeautifulSoup

class ScrapDecisionListTask:

    def __init__(self, client):
        self._client = client
        pass

    # http://www.nsoud.cz/Judikaturans_new/judikatura_vks.nsf/$$WebSearch1?SearchView&Query=[idstrediska]=040 AND ([usek]=Obchod OR [usek]=Obcan OR [usek]=Civil)&SearchMax=0Start=1&Count=15&pohled=1&searchOrder=4
    @asyncio.coroutine
    def run(self, id_strediska, count = 15):
        # http://www.nsoud.cz/Judikaturans_new/judikatura_vks.nsf
        # /$$WebSearch1?SearchView&Query=[idstrediska]=040 AND ([usek]=Obchod OR [usek]=Obcan OR [usek]=Civil)&SearchMax=0Start=1&Count=15&pohled=1&searchOrder=4
        html_raw = yield from self._client.get("http://www.nsoud.cz/Judikaturans_new/judikatura_vks.nsf/$$WebSearch1?SearchView&Query=%5Bidstrediska%5D%3D"+id_strediska+"&SearchMax=0Start=1&Count="+str(count)+"&pohled=1&searchOrder=4")
                                          # replace WebSearch/WebPrint
        soup = BeautifulSoup(html_raw, 'html.parser')
        data = []
        table_res = soup.find_all('table', {"class":"res"})[0] #todo check length
            #print(">>>>>> table class "+str(table["class"]))
        #if "res" in table["class"]: table_res = table

        for a in table_res.find_all('a'):
            url = a.get('href')
            data.append("http://www.nsoud.cz" + url)

        #print(str(data))

        return data
