import asyncio
import aiopg

class Dao:

    _CREATE_SPEC = """
CREATE TABLE specialization (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL
);
"""
    _CONNECTION = 'dbname=social_good' \
                  + ' user=social_good' \
                  + ' password=' \
                  +' host=social-good.cbyzlfhidcnr.eu-central-1.rds.amazonaws.com'


    _CREATE_ADVOCATES = """
CREATE TABLE advocate (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  address TEXT NULL,
  gps_lat DOUBLE PRECISION NULL,
  gps_lon DOUBLE PRECISION NULL
);
    """

    def __init__(self):
        pass

    @asyncio.coroutine
    def start(self):
        self._pool = yield from aiopg.create_pool(Dao._CONNECTION)
        self._conn = yield from self._pool.acquire()


    @asyncio.coroutine
    def get_cursor(self):
        cur = yield from self._conn.cursor()
        return cur

    @asyncio.coroutine
    def run_no_result(self, query, params):
        cur = yield from self.get_cursor()
        yield from cur.execute(query, params)
        cur.close()

    @asyncio.coroutine
    def test(self):
        cur = yield from self.get_cursor()
        yield from cur.execute("SELECT 1")
        ret = []
        for row in cur:
            ret.append(row)
        print(str(ret))
        cur.close()

    @asyncio.coroutine
    def create_advocate_table(self):
        yield from self.run_no_result(Dao._CREATE_ADVOCATES, ())

    @asyncio.coroutine
    def create_spec_table(self):
        yield from self.run_no_result(Dao._CREATE_SPEC, ())

    @asyncio.coroutine
    def insert_advocate(self, id, name, address):
        # print(str(id))
        # print(str(name))
        # print(str(address))
        if address.strip() == "":
            address = None
        yield from self.run_no_result("""
INSERT INTO advocate (id, name, address, gps_lat, gps_lon) VALUES (%s, %s, %s, NULL, NULL)
        """, (id, name, address))

    @asyncio.coroutine
    def insert_spec(self, id, name):
        yield from self.run_no_result("""
INSERT INTO specialization (id, name) VALUES (%s, %s)
        """, (id, name))

    # return [id, address]
    @asyncio.coroutine
    def get_advocate_with_and_address_and_no_gps(self):
        cur = yield from self.get_cursor()
        yield from cur.execute("""
SELECT id,address FROM advocate
WHERE advocate.address IS NOT NULL
 AND advocate.gps_lat IS NULL
 AND advocate.gps_lon IS NULL
LIMIT 1
""")
        ret = []
        for row in cur:
            ret.append(row)
        cur.close()
        return ret[0]

# SET temp_lo = temp_lo+1, temp_hi = temp_lo+15, prcp = DEFAULT
#WHERE city = 'San Francisco'
    @asyncio.coroutine
    def update_gps(self, id, gps_lat, gps_lon):
        print(str([id, gps_lat,gps_lon]))
        yield from self.run_no_result("""
UPDATE advocate SET (gps_lat, gps_lon) = (%s, %s)
        """, (id, gps_lat, gps_lon))


#         yield from self.run_no_result("""
# INSERT INTO specialization (id, name) VALUES (%s, %s)
#         """, (id, name))

    @asyncio.coroutine
    def close(self):
        self._conn.close()
        self._pool.close()
        pass
