import pygame, os
from Window import *
from World import *

pygame.init()
win = Window(1920, 1080)
world = World(win)
clock = pygame.time.Clock()
state = "Game"

def handleInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if state == "Game":
            #tutaj sterowanie gry
            pass
        elif state == "Menu":
            #tutaj sterowanie w menu
            pass
        elif state == "GameOver":
            #tutaj sterowanie w gameover
            pass


def update():
    elapsedTime = clock.tick()
    if state == "Game":
        world.update(elapsedTime)
    elif state == "Menu":
        # tutaj update w menu
        pass
    elif state == "GameOver":
        # tutaj update w gameover
        pass


def render():
    if state == "Game":
        world.draw(win.win)
        win.update()
    elif state == "Menu":
        # tutaj render w menu
        pass
    elif state == "GameOver":
        # tutaj render w gameover
        pass

    pygame.display.update()


if __name__ == '__main__':
    while True:
        clock.tick(60)
        handleInput()
        update()
        render()
