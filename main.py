import pygame as pg
import requests
from input import window_input
from spn import get_spn
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


pg.init()
screen = pg.display.set_mode(size := (600, 450))
coordinates = window_input(screen, 'Ввведите координаты', size)
toponym_longitude, toponym_lattitude = coordinates.split()
spn = get_spn(coordinates)
print(spn)
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
img.save('data.png')
photo = pg.image.load('data.png')
while True:
    ev = [i.type for i in pg.event.get()]
    if pg.QUIT in ev:
        break
    screen.blit(photo, (0, 0))
    pg.display.flip()