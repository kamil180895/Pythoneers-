import pygame, os
class Bullet:
    def self__init__(self, posx, posy, width, height, texture, ats, dmg):
        self.posx = posx
        self.posy = posy
        self.width = 5
        self.height = 25
        self.texture = pygame.image.load(os.path.join('textures','Bullet.png'))
        self.ats = 15
        self.dmg = 1


    bullets_player = []
    bullets_enemy = []


    def make_bullet_enemey(self, bullets_enemy, posx1, posy2):
        bullets_enemy.append(Bullet(posx1,posy2))

    def make_bullet_player(self, bullets_player, posx1, posy1):
       bullets_player.append(Bullet(posx1,posy1))
        bullets_player.append(Bullet(posx1+30, posy1))

    def delete_bullet(self, bullets_player, bullets_enemy):
        for i in bullets_player:
            if i.posy - Bullet.height <= 0:
                bullets_player.pop(i)
        for i in bullets_enemy:
            if i.posy - Bullet.height >= 1960:
                bullets_enemy.pop(i)

        for i in
