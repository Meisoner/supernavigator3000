import requests
from dictutils import *


def get_spn(coordinates):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": coordinates,
        "format": "json",
    }
    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    up = keydictsearch(json_response, 'uppercorner')[0].split()
    down = keydictsearch(json_response, 'lowercorner')[0].split()
    return str(float(up[0]) - float(down[0])) + ',' + str(float(up[1]) - float(down[1]))