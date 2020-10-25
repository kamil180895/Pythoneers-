import pygame, os

class Weapon:
    def self__init__(self, posx, posy,image):
        self.posx = posx
        self.posy = posy
        self.width = 5
        self.height = 25
        self.image = image
        self.texture1 = pygame.image.load(os.path.join('textures', 'Bullet_player.png'))
        self.texture1 = pygame.image.load(os.path.join('textures', 'Bullet_weapon.png'))
        self.ats = 20
        self.dmg = 17

    texture1 = pygame.image.load(os.path.join('textures', 'Bullet_player.png'))
    texture2 = pygame.image.load(os.path.join('textures', 'Bullet_weapon.png'))

    bullets_player = []
    bullets_enemy = []


    def make_bullet_enemey(self, bullets_enemy, posx1, posy2):
        bullets_enemy.append(Weapon (posx1, posy2, texture2))

    def make_bullet_player(self, bullets_player, posx1, posy1):
        bullets_player.append(Weapon(posx1, posy1, texture1))
        bullets_player.append(Weapon(posx1 + 30, posy1, texture1))

    def bullets_sollision_check(self, bullets_player, bullets_enemy, enemy_list, Player.posx, Player.posy):
        for i in bullets_player:
            if i.posy - Weapon.height <= 0:
                bullets_player.pop(i)
                bullets_enemy[i].delete

        for i in bullets_enemy:
            if i.posy - Weapon.height >= 1920:
                bullets_enemy.pop(i)
                bullets_enemy[i].delete

        for i in len(enemy_list): #enemy hit
            if bullets_player[i].posx - Weapon.width <= enemy_list[i].posx - enemy_list[i].width: # warunek na posx1
                if bullets_player[i].posx + Weapon.width >= enemy_list[i].posx - enemy_list[i].width:
                    if bullets_player[i].posy + Weapon.height >= enemy_list[i].posy + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].posy - Weapon.height <= enemy_list[i].posy + enemy_list[i].height:
                            enemy_list[i].hit = 1
                    if bullets_player[i].posy - Weapon.height <= enemy_list[i].posy - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].posy + Weapon.height >= enemy_list[i].posy - enemy_list[i].height:
                            enemy_list[i].hit = 1


            if bullets_player[i].posx + Weapon.width >= enemy_list[i].posx + enemy_list[i].width: # warunek na posx2
                if bullets_player[i].posx - Weapon.width <= enemy_list[i].posx + enemy_list[i].width:
                    if bullets_player[i].posy + Weapon.height >= enemy_list[i].posy + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].posy - Weapon.height <= enemy_list[i].posy + enemy_list[i].height:
                            enemy_list[i].hit = 1
                    if bullets_player[i].posy - Weapon.height <= enemy_list[i].posy - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].posy + Weapon.height >= enemy_list[i].posy - enemy_list[i].height:
                            enemy_list[i].hit = 1


            # player hit
        if bullets_enemy[i].posx - Weapon.width <= Player.posx - Player.width: # warunek na posx1
            if bullets_enemy[i].posx + Weapon.width >= Player.posx - Player.width:
                if bullets_enemy[i].posy + Weapon.height >= Player.posy + Player.height:  # warunek na posy1
                    if bullets_enemy[i].posy - Weapon.height <= Player.posy + Player.height:
                        Player.hit = 1
                if bullets_enemy[i].posy - Weapon.height <= Player[i].posy - Player[i].height:  # warunek na posy2
                    if bullets_enemy[i].posy + Weapon.height >= Player[i].posy - Player[i].height:
                        Player.hit = 1


        if bullets_enemy[i].posx + Weapon.width >= Player.posx + Player.width: # warunek na posx2
            if bullets_enemy[i].posx - Weapon.width <= Player.posx + Player.width:
                if bullets_enemy[i].posy + Weapon.height >= Player.posy + Player.height:  # warunek na posy1
                    if bullets_enemy[i].posy - Weapon.height <= Player.posy + Player.height:
                        Player.hit = 1
                if bullets_enemy[i].posy - Weapon.height <= Player.posy - Player.height:  # warunek na posy2
                    if bullets_enemy[i].posy + Weapon.height >= Player.posy - Player.height:
                        Player.hit = 1
