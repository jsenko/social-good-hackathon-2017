import asyncio
from aiohttp import web
import json

from Dao import Dao

loop = asyncio.get_event_loop()
#client = Client(loop)
dao = Dao()
loop.run_until_complete(dao.start())
#csv = Csv(dao)
#geo = Geocode(client)
#gps = LoadGps(dao, geo)


# find advocates in area
# req
# {"top_lat"}

@asyncio.coroutine
def advocate_geo(request):
  body = yield from request.json()
  data = body#json.loads(body)
  data = yield from dao.get_advocate_geo(
    topl_lat=data["topl_lat"],
    topl_lon=data["topl_lon"],
    botr_lat=data["botr_lat"],
    botr_lon=data["botr_lon"])
  text=json.dumps(data)
  return web.Response(text=text)


@asyncio.coroutine
def index(request):
    content = None
    with open('./index.html', 'r') as content_file:
        content = content_file.read()
    return web.Response(text=content,content_type='text/html')

# body = yield from request.json()

app = web.Application()
app.router.add_post('/advocate_geo', advocate_geo)
app.router.add_get('/', index)

web.run_app(app)

# test ~Prague
# curl -H "Content-Type: application/json" -X POST -d '{"topl_lat":50.0825778,"topl_lon":14.4224156,"botr_lat":50.007955,"botr_lon":14.673234}' http://localhost:8080/advocate_geo