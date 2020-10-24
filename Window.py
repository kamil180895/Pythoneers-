import pygame

class Window(object):
    def  __init__(self):
        self.width  =  1000
        self.height = 800
        self.win =  pygame.display.set_mode((self.width,  self.height))
        pygame.display.set_caption("Pythoneers++:  Attack on CO2")
