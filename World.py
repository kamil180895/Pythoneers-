from Window import *
import pygame
import Weapon

class World:
    def __init__(self, surface):
        self.window = surface.win
        self.bullets_player = []
        self.bullets_enemy = []
    def update(self, time):
        pass

    def draw(self, win):
        background = pygame.image.load('Atmosphere.png')
        win.blit(pygame.transform.scale(background, (int(background.get_width() * 8), int(background.get_height() * 8))), (0, 0))

    def make_bullet_enemy(self, bullets_enemy, posx1, posy2):
        bullets_enemy.append(Weapon (posx1, posy2))

    def make_bullet_player(self, bullets_player, posx1, posy1):
        bullets_player.append(Weapon(posx1, posy1))
        bullets_player.append(Weapon(posx1 + 30, posy1))

