import pygame as pg
import time
import random

pg.init()

display_width = 800
display_height = 600

car_width = 100
car_height = 200

black = (10, 10, 10)
white = (200, 200, 200)
red = (245, 10, 10)

gameDisplay = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Need for speed')
clock = pg.time.Clock()

carImg = pg.image.load("graphics/car.png")
carImg = pg.transform.scale(carImg, (car_width, car_height))


def things(thingx, thingy, thingw, thingh, color):
    pg.draw.rect(gameDisplay,color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pg.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.65)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -5
                if event.key == pg.K_RIGHT:
                    x_change = +5
            if event.type == pg.KEYUP:
                x_change = 0

        x += x_change

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty +=  thing_speed

        car(x, y)

        if x > display_width-car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()

        pg.display.update()
        clock.tick(60)

game_loop()
pg.quit()
quit()