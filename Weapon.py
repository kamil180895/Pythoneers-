import pygame, os

class Weapon:
    def self__init__(self, x, y,image):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 25
        self.image = image
        self.texture1 = pygame.image.load(os.path.join('textures', 'bullet_player.png'))
        self.texture1 = pygame.image.load(os.path.join('textures', 'bullet_enemy.png'))
        self.ats = 20
        self.dmg = 17

    texture1 = pygame.image.load(os.path.join('textures', 'bullet_player.png'))
    texture2 = pygame.image.load(os.path.join('textures', 'bullet_enemy.png'))

    bullets_player = []
    bullets_enemy = []


    def make_bullet_enemey(self, bullets_enemy, posx1, posy2):
        bullets_enemy.append(Weapon (posx1, posy2, texture2))

    def make_bullet_player(self, bullets_player, posx1, posy1):
        bullets_player.append(Weapon(posx1, posy1, texture1))
        bullets_player.append(Weapon(posx1 + 30, posy1, texture1))

    def bullets_sollision_check(self, bullets_player, bullets_enemy, enemy_list, PlayerCharacter.x, PlayerCharacter.y):
        for i in bullets_player:
            if i.y - Weapon.height <= 0:
                bullets_player.pop(i)
                bullets_enemy[i].delete

        for i in bullets_enemy:
            if i.y - Weapon.height >= 1920:
                bullets_enemy.pop(i)
                bullets_enemy[i].delete

        for i in len(enemy_list): #enemy hit
            if bullets_player[i].x - Weapon.width <= enemy_list[i].x - enemy_list[i].width: # warunek na posx1
                if bullets_player[i].x + Weapon.width >= enemy_list[i].x - enemy_list[i].width:
                    if bullets_player[i].y + Weapon.height >= enemy_list[i].y + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].y - Weapon.height <= enemy_list[i].y + enemy_list[i].height:
                            enemy_list[i].hit = 1
                            return 0
                    if bullets_player[i].y - Weapon.height <= enemy_list[i].y - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].y + Weapon.height >= enemy_list[i].y - enemy_list[i].height:
                            enemy_list[i].hit = 1
                            return 0


            if bullets_player[i].x + Weapon.width >= enemy_list[i].x + enemy_list[i].width: # warunek na posx2
                if bullets_player[i].x - Weapon.width <= enemy_list[i].x + enemy_list[i].width:
                    if bullets_player[i].y + Weapon.height >= enemy_list[i].y + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].y - Weapon.height <= enemy_list[i].y + enemy_list[i].height:
                            enemy_list[i].hit = 1
                            return 0
                    if bullets_player[i].y - Weapon.height <= enemy_list[i].y - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].y + Weapon.height >= enemy_list[i].y - enemy_list[i].height:
                            enemy_list[i].hit = 1
                            return 0


            # player hit
        if bullets_enemy[i].x - Weapon.width <= Player.x - Player.width: # warunek na posx1
            if bullets_enemy[i].x + Weapon.width >= Player.x - Player.width:
                if bullets_enemy[i].y + Weapon.height >= Player.y + Player.height:  # warunek na posy1
                    if bullets_enemy[i].y - Weapon.height <= Player.y + Player.height:
                        Player.hit = 1
                        return 0
                if bullets_enemy[i].y - Weapon.height <= Player[i].y - Player[i].height:  # warunek na posy2
                    if bullets_enemy[i].y + Weapon.height >= Player[i].y - Player[i].height:
                        Player.hit = 1
                        return 0


        if bullets_enemy[i].x + Weapon.width >= Player.x + Player.width: # warunek na posx2
            if bullets_enemy[i].x - Weapon.width <= Player.x + Player.width:
                if bullets_enemy[i].y + Weapon.height >= Player.y + Player.height:  # warunek na posy1
                    if bullets_enemy[i].y - Weapon.height <= Player.y + Player.height:
                        Player.hit = 1
                        return 0
                if bullets_enemy[i].y - Weapon.height <= Player.y - Player.height:  # warunek na posy2
                    if bullets_enemy[i].y + Weapon.height >= Player.y - Player.height:
                        Player.hit = 1
                        return 0
        return 0
