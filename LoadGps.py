import asyncio

from Dao import Dao
from Geocode import Geocode

class LoadGps:

    def __init__(self, dao, geo):
        self._geo = geo
        self._dao = dao


    @asyncio.coroutine
    def run(self):

        for i in range(0,2450):
            data = yield from self._dao.get_advocate_with_and_address_and_no_gps()
            if len(data) == 0:
                break
            print(str(data))
            point = yield from self._geo.run(data[1])
            print(str(point))
            yield from self._dao.update_gps(id=data[0], gps_lat=point[0], gps_lon=point[1])
