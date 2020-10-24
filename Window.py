import pygame

class Window(object):
    def  __init__(self, width,  height, clock):
        self.width  =  width
        self.height = height
        self.clock = clock
        self.win =  pygame.display.set_mode((width,  height))
        self.clock = pygame.time.Clock
        pygame.display.set_caption("Pythoneers++:  Attack on CO2")
    def draw(self, image, position, area):
        self.win.blit(image, position, area=area)
    def update(self):
        pygame.display.update()
