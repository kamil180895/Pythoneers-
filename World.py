from Window import *
import pygame

class World:
    def __init__(self, surface):
        self.window = surface.win

    def update(self, time):
        pass

    def draw(self, win):
        background = pygame.image.load('Atmosphere.png')
        win.blit(pygame.transform.scale(background, (int(background.get_width() * 8), int(background.get_height() * 8))), (0, 0))