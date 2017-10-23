import asyncio
import aiopg

class Csv:

    def __init__(self, dao):
        self._dao = dao

    @asyncio.coroutine
    def _load_advocate(self, line):
        #advocate_id;name;surname;street;city;valid_from;valid_to;email
        data = line.split(";")
        print(str(data))
        yield from self._dao.insert_advocate(
            id = data[0],
            name = data[1] + " " + data[2],
            address = data[3] + " " + data[4])

    @asyncio.coroutine
    def load_advocates(self, file_name):
        with open(file_name) as fp:
            for line in fp:
                yield from self._load_advocate(line)

    def load_specialization(self, file_name):
        with open(file_name) as fp:
            for line in fp:
                yield from self._load_spec(line)

    def _load_spec(self, line):
        #specialization_full;specialization_id;specialization_name;synthetic_id;specialization_stem
        #01 generální praxe;1;generální praxe;0;general
        data = line.split(";")
        print(str(data))
        yield from self._dao.insert_spec(
            id = data[3],
            name = data[2])
        pass


