import asyncio
import json
import urllib.parse


class Geocode:
    _API_KEY = ""

    foo = {'results': [{'address_components':
                            [{'short_name': '34', 'long_name': '34', 'types': ['street_number']},
                             {'short_name': '750', 'long_name': '750', 'types': ['premise']},
                             {'short_name': 'Jungmannova', 'long_name': 'Jungmannova', 'types': ['route']},
                             {'short_name': 'Nové Město', 'long_name': 'Nové Město',
                              'types': ['neighborhood', 'political']}, {'short_name': 'Praha 1', 'long_name': 'Praha 1',
                                                                        'types': ['political', 'sublocality',
                                                                                  'sublocality_level_1']},
                             {'short_name': 'Hlavní město Praha', 'long_name': 'Hlavní město Praha',
                              'types': ['administrative_area_level_2', 'political']},
                             {'short_name': 'Hlavní město Praha', 'long_name': 'Hlavní město Praha',
                              'types': ['administrative_area_level_1', 'political']},
                             {'short_name': 'CZ', 'long_name': 'Czechia', 'types': ['country', 'political']},
                             {'short_name': '110 00', 'long_name': '110 00', 'types': ['postal_code']}], 'geometry': {
        'viewport': {'southwest': {'lat': 50.0812288197085, 'lng': 14.4210666197085},
                     'northeast': {'lat': 50.0839267802915, 'lng': 14.4237645802915}},
        'location': {'lat': 50.0825778, 'lng': 14.4224156}, 'location_type': 'ROOFTOP'}, 'types': ['street_address'],
                        'place_id': 'ChIJWfRfuO2UC0cRucHqcnRZIgY', 'formatted_address':
                            'Jungmannova 750/34, Nové Město, 110 00 Praha-Praha 1, Czechia'}], 'status': 'OK'}

    def __init__(self, client):
        self._client = client
        pass

    # returns [lat, lon]
    @asyncio.coroutine
    def run(self, address):
        address = urllib.parse.quote_plus(address)
        raw_json = yield from self._client.get("https://maps.googleapis.com/maps/api/geocode/json?" \
                                               + "address=" + address \
                                               + "&key=" + Geocode._API_KEY)
        data = json.loads(raw_json)
        #print(str(data["results"][0]))
        res = [
            data["results"][0]["geometry"]["location"]["lat"],
            data["results"][0]["geometry"]["location"]["lng"]
        ]
        #print(str(res))
        return res
