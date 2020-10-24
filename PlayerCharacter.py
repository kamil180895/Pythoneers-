import pygame, os

class PlayerCharacter:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.texture1 = pygame.image.load(os.path.join('assets', 'player.png'))
        self.texture2 = self.texture1.copy()
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.weapon = Weapon()
        self.elapsedTime = 0.0
        self.frametime = 0.1


    def draw(self, window):
        window.draw(self.texture, (self.x, self.y))

    def update(self, newelapsed):
        self.elapsedTime += newelapsed
        if self.elapsedTime<self.frametime:
            pygame.transform.scale(self.texture, ())

        self.hitbox.move_ip(self.x , self.y)

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def death(self):
        pass