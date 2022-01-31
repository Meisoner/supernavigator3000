from input import window_input
from spn import get_spn
from gen import *


def arithm(spn, act):
    intspn = [float(i) for i in spn.split(',')]
    return str(intspn[0] + act) + ',' + str(intspn[1] + act)


pg.init()
screen = pg.display.set_mode(size := (600, 450))
coordinates = window_input(screen, 'Ввведите координаты', size)
spn = get_spn(coordinates)
run = True
new = False
photo = get_photo(coordinates, spn)
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_PAGEDOWN and max([float(t) for t in spn.split(',')]) < 30:
                spn = arithm(spn, 0.5)
                new = True
            elif i.key == pg.K_PAGEUP and min([float(t) for t in spn.split(',')]) > 1:
                spn = arithm(spn, -0.5)
                new = True
    if new:
        print(spn)
        photo = get_photo(coordinates, spn)
        new = False
    screen.blit(photo, (0, 0))
    pg.display.flip()