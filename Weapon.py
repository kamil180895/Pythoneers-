from PlayerCharacter import *
import os
class Weapon():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 25
        self.texture1 = pygame.image.load(os.path.join('textures', 'bullet_player.png'))
        self.dmg = 17

    def bullets_move(self, bullets_player, bullets_enemy):
        for i in bullets_enemy:
            for i in 10:
                bullets_enemy.y -= 1.5
        for i in bullets_player:
            for i in 10:
                bullets_player.y += 2

    def bullets_sollision_check(self, bullets_player, bullets_enemy, enemy_list, Player.x, Player.y):
        for i in bullets_player:
            if i.y - Weapon.height <= 0:
                i.pop(i)
                i.delete

        for i in bullets_enemy:
            if i.y - Weapon.height >= 1920:
                i.pop(i)
                i.delete

        for i in len(enemy_list): #enemy hit
            if bullets_player[i].x - Weapon.width <= enemy_list[i].x - enemy_list[i].width: # warunek na posx1
                if bullets_player[i].x + Weapon.width >= enemy_list[i].x - enemy_list[i].width:
                    if bullets_player[i].y + Weapon.height >= enemy_list[i].y + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].y - Weapon.height <= enemy_list[i].y + enemy_list[i].height:
                            enemy_list[i].hit = 1
                            bullets_player.pop(i)
                            bullets_enemy[i].delete
                            return 0
                    if bullets_player[i].y - Weapon.height <= enemy_list[i].y - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].y + Weapon.height >= enemy_list[i].y - enemy_list[i].height:
                            enemy_list[i].hit = 1
                            bullets_player.pop(i)
                            bullets_enemy[i].delete
                            return 0


            if bullets_player[i].x + Weapon.width >= enemy_list[i].x + enemy_list[i].width: # warunek na posx2
                if bullets_player[i].x - Weapon.width <= enemy_list[i].x + enemy_list[i].width:
                    if bullets_player[i].y + Weapon.height >= enemy_list[i].y + enemy_list[i].height:  # warunek na posy1
                        if bullets_player[i].y - Weapon.height <= enemy_list[i].y + enemy_list[i].height:
                            enemy_list[i].hit = 1
                            bullets_player.pop(i)
                            bullets_enemy[i].delete
                            return 0
                    if bullets_player[i].y - Weapon.height <= enemy_list[i].y - enemy_list[i].height:  # warunek na posy2
                        if bullets_player[i].y + Weapon.height >= enemy_list[i].y - enemy_list[i].height:
                            enemy_list[i].hit = 1
                            bullets_player.pop(i)
                            bullets_enemy[i].delete
                            return 0


            # player hit
        if bullets_enemy[i].x - Weapon.width <= Player.x - Player.width: # warunek na posx1
            if bullets_enemy[i].x + Weapon.width >= Player.x - Player.width:
                if bullets_enemy[i].y + Weapon.height >= Player.y + Player.height:  # warunek na posy1
                    if bullets_enemy[i].y - Weapon.height <= Player.y + Player.height:
                        Player.hit = 1
                        bullets_player.pop(i)
                        bullets_enemy[i].delete
                        return 0
                if bullets_enemy[i].y - Weapon.height <= Player[i].y - Player[i].height:  # warunek na posy2
                    if bullets_enemy[i].y + Weapon.height >= Player[i].y - Player[i].height:
                        Player.hit = 1
                        bullets_player.pop(i)
                        bullets_enemy[i].delete
                        return 0


        if bullets_enemy[i].x + Weapon.width >= Player.x + Player.width: # warunek na posx2
            if bullets_enemy[i].x - Weapon.width <= Player.x + Player.width:
                if bullets_enemy[i].y + Weapon.height >= Player.y + Player.height:  # warunek na posy1
                    if bullets_enemy[i].y - Weapon.height <= Player.y + Player.height:
                        Player.hit = 1
                        bullets_player.pop(i)
                        bullets_enemy[i].delete
                        return 0
                if bullets_enemy[i].y - Weapon.height <= Player.y - Player.height:  # warunek na posy2
                    if bullets_enemy[i].y + Weapon.height >= Player.y - Player.height:
                        Player.hit = 1
                        bullets_player.pop(i)
                        bullets_enemy[i].delete
                        return 0
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
