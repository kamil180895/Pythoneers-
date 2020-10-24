import pygame, os
class Bullet:
    def self__init__(self, posx, posy, width, height, texture):
        self.posx = posx
        self.posy = posy
        self.width = 5
        self.height = 25
        self.texture = pygame.image.load(os.path.join('textures','Bullet.png'))

class Weapon:
    def self__init__(self,ats,dmg):
        self.ats = 15
        self.dmg = 1

    bullets_player = []
    bullets_enemy = []
    def make_bullet_enemey(self, bullets_enemy, pos1, pos2):
        bullets_enemy.append(Bullet(pos1,pos2))

    def make_bullet_player(self, bullets_player, posx1, posy1):
        bullets_player.append(Bullet(posx1,posy1))
        bullets_player.append(Bullet(posx1+30, posy1))
