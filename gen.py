from PIL import Image, ImageFont, ImageDraw
import pygame as pg
import requests
from io import BytesIO


def get_photo(coordinates, spn):
    toponym_longitude, toponym_lattitude = coordinates.split()
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": spn,
        "l": "sat"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    img = Image.open(BytesIO(
        response.content))
    font = ImageFont.load_default()
    dr = ImageDraw.Draw(img)
    dr.text((0, 0), coordinates, font=font, fill=(0, 0, 0, 255))
    name = 'data.png'
    img.save(name)
    return pg.image.load(name)