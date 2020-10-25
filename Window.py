import pygame

class Window(object):
    def  __init__(self, width,  height):
        self.width  =  width
        self.height = height
        self.win =  pygame.display.set_mode((width,  height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pythoneers++:  Attack on CO2")
    def update(self):
        pygame.display.update()



