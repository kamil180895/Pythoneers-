import time
import pygame
from World import *

class Enemy(object):

    def __init__(self, x, y, img, hptimer):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 10
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.hitbox = [x, y, self.width, self.height]
        self.hp = 15 + int(time.time()-hptimer)*2
        self.timer = pygame.time.Clock()

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def movement(self, enemies):
        if self.vy > 0:
            if (len(enemies)//5 == 0) and (self.y == (1080 - (self.height*2 + 30))):
                self.vy = 0
                self.vx = 10
            if (len(enemies)//5 == 1) and (self.y == (1080 - (self.height + 20))):
                self.vy = 0
                self.vx = 10
            if (len(enemies)//5 >= 2) and (self.y == (1070)):
                self.vy = 0
                self.vx = 10
            self.y -= self.vy
        else:
            if (self.vx > 0) and (self.x + self.width):
                self.vx = -10
            if (self.vx < 0) and self.x == 0:
                self.vx = 10
            self.x += self.vx

    def shoot(self):
        if self.vy ==0:
            if self.timer.tick() >= 0.5:
                make_bullet_enemy(self.x,self.y)

    def hit(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.__delete__(self)

    def __delete__(self, instance):
        del instance

    def update(self, enemies, window):
        self.movement(enemies)
        self.draw(window)
        self.shoot()
