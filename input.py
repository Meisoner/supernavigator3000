import pygame as pg


def window_input(screen, message, size):
    keys = {getattr(pg, 'K_' + str(key)): str(key) for key in range(10)}
    keys[pg.K_PERIOD] = '.'
    keys[pg.K_SPACE] = ' '
    run = True
    text = ''
    font = pg.font.Font(None, 30)
    title = font.render(message, True, (255, 255, 255))
    x, y = size
    textsize = 2 * x // 3
    textcenter = x // 2 - textsize // 2
    titlesize = title.get_size()[0]
    titlecenter = x // 2 - titlesize // 2
    while run:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return
            if i.type == pg.KEYDOWN:
                if i.key in keys.keys():
                    text += keys[i.key]
                elif i.key == pg.K_BACKSPACE:
                    text = text[:-1]
                elif i.key == pg.K_RETURN:
                    run = False
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (255, 255, 255), (textcenter, 50, textsize, 40))
        label = font.render(text, True, (0, 0, 0))
        screen.blit(label, (textcenter, 50))
        screen.blit(title, (titlecenter, 0))
        pg.display.flip()
    return text