import pygame, os

class Weapon:
    def self__init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.width = 5
        self.height = 25
        self.texture = pygame.image.load(os.path.join('textures','Bullet.png'))
        self.ats = 20
        self.dmg = 17


    bullets_player = []
    bullets_enemy = []


    def make_bullet_enemey(self, bullets_enemy, posx1, posy2):
        bullets_enemy.append(Bullet(posx1,posy2))

    def make_bullet_player(self, bullets_player, posx1, posy1):
        bullets_player.append(Bullet(posx1,posy1))
        bullets_player.append(Bullet(posx1+30, posy1))

    def bullets_sollision_check(self, bullets_player, bullets_enemy, enemy_list, Player.posx, Player.posy):
        for i in bullets_player:
            if i.posy - Bullet.height <= 0:
                bullets_player.pop(i)

        for i in bullets_enemy:
            if i.posy - Bullet.height >= 1920:
                bullets_enemy.pop(i)

        for i in len(enemy_list): #enemy hit
            if bullets_player[i].posx - Bullet.width <= enemy_list[i].posx - enemy_list[i].width: # warunek na posx1
                if bullets_player[i].posx + Bullet.width >= enemy_list[i].posx - enemy_list[i].width:
                    if bullets_player[i].posy + Bullet.height >= enemy_list[i].posy + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].posy - Bullet.height <= enemy_list[i].posy + enemy_list[i].height:
                            enemy_list[i].hit = 1
                    if bullets_player[i].posy - Bullet.height <= enemy_list[i].posy - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].posy + Bullet.height >= enemy_list[i].posy - enemy_list[i].height:
                            enemy_list[i].hit = 1


            if bullets_player[i].posx + Bullet.width >= enemy_list[i].posx + enemy_list[i].width: # warunek na posx2
                if bullets_player[i].posx - Bullet.width <= enemy_list[i].posx + enemy_list[i].width:
                    if bullets_player[i].posy + Bullet.height >= enemy_list[i].posy + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].posy - Bullet.height <= enemy_list[i].posy + enemy_list[i].height:
                            enemy_list[i].hit = 1
                    if bullets_player[i].posy - Bullet.height <= enemy_list[i].posy - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].posy + Bullet.height >= enemy_list[i].posy - enemy_list[i].height:
                            enemy_list[i].hit = 1



        if bullets_enemy[i].posx - Bullet.width <= Player.posx - Player.width: # warunek na posx1
            if bullets_enemy[i].posx + Bullet.width >= Player.posx - Player.width:
                if bullets_enemy[i].posy + Bullet.height >= Player.posy + Player.height:  # warunek na posy1
                    if bullets_enemy[i].posy - Bullet.height <= Player.posy + Player.height:
                        Player.hit = 1
                if bullets_enemy[i].posy - Bullet.height <= Player[i].posy - Player[i].height:  # warunek na posy2
                    if bullets_enemy[i].posy + Bullet.height >= Player[i].posy - Player[i].height:
                        Player.hit = 1


        if bullets_enemy[i].posx + Bullet.width >= Player.posx + Player.width: # warunek na posx2
            if bullets_enemy[i].posx - Bullet.width <= Player.posx + Player.width:
                if bullets_enemy[i].posy + Bullet.height >= Player.posy + Player.height:  # warunek na posy1
                    if bullets_enemy[i].posy - Bullet.height <= Player.posy + Player.height:
                        Player.hit = 1
                if bullets_enemy[i].posy - Bullet.height <= Player.posy - Player.height:  # warunek na posy2
                    if bullets_enemy[i].posy + Bullet.height >= Player.posy - Player.height:
                        Player.hit = 1


