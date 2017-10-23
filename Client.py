import asyncio

import aiohttp
import json
from bs4 import BeautifulSoup

class Client:

    def __init__(self, loop):
        self._session = aiohttp.ClientSession(loop=loop)
        pass


    @asyncio.coroutine
    def get(self, url):
        with aiohttp.Timeout(30):
            resp = yield from self._session.get(url)
            try:

            # Any actions that may lead to error:
            #1/0

                return (yield from resp.text())
            except Exception as e:
            # .close() on exception.
                resp.close()
                raise e
            finally:
            # .release() otherwise to return connection into free connection pool.
            # It's ok to release closed response:
            # https://github.com/KeepSafe/aiohttp/blob/master/aiohttp/client_reqrep.py#L664
                yield from resp.release()


    @asyncio.coroutine
    def close(self):
        yield from self._session.close()