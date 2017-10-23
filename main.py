import asyncio

from Dao import Dao
from Csv import Csv
from Client import Client
from ScrapDecisionListTask import ScrapDecisionListTask
from Geocode import Geocode
from LoadGps import LoadGps

loop = asyncio.get_event_loop()
client = Client(loop)
dao = Dao()
loop.run_until_complete(dao.start())
csv = Csv(dao)
geo = Geocode(client)
gps = LoadGps(dao, geo)

def task1():
    #loop.run_until_complete(ScrapDecisionListTask(client).run("040"))
    pass

def task2():
    loop.run_until_complete(csv.load_advocates("./advocates_table.csv"))

def task3():
    loop.run_until_complete(csv.load_specialization("./specialization_stem.csv"))

def task4():
    loop.run_until_complete(dao.create_spec_table())

def task5():
    loop.run_until_complete(geo.run("Jungmannova 750/34 Praha 1"))

def task6():
    loop.run_until_complete(dao.get_advocate_with_and_address_and_no_gps())

def task7():
    loop.run_until_complete(gps.run())


task7()

loop.run_until_complete(dao.close())
loop.run_until_complete(client.close())


