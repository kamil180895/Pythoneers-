from Window import *
import pygame
import Weapon

class World:
    def __init__(self, surface):
        self.window = surface.win
        self.bullets_player = []
        self.bullets_enemy = []
        self.drawIteration = 0
        self.background = pygame.image.load('Atmosphere.png')
        self.background = pygame.transform.scale(self.background, (int(self.background.get_width() * 2.9), int(self.background.get_height() * 2.9)))
    def update(self, time):
        pass

    def draw(self, win):
        self.drawIteration += 1
        win.blit(self.background, (0, -33408 + 1920 + (int(self.drawIteration * 30)) % 21500))

    def make_bullet_enemy(self, bullets_enemy, posx1, posy2):
        bullets_enemy.append(Weapon (posx1, posy2))

    def make_bullet_player(self, bullets_player, posx1, posy1):
        bullets_player.append(Weapon(posx1, posy1))
        bullets_player.append(Weapon(posx1 + 30, posy1))

