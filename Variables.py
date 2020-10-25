import  time, pygame

class Variables(object):

    def  __init__(self):
        self.timer = time.time()
        self.hptimer = time.time()
        self.bullets = []
        self.enemies = []

    def get_bigger(self, pic):
        return pygame.transform.scale(pic, (int(pic.get_width()*1.1), int(pic.get_height()*1.1)))

    def get_smaller(self, pic):
        return pygame.transform.scale(pic, (int(pic.get_width()*0.9), int(pic.get_height()*0.9)))

    def update_pic(self, pic):
        if time.time()-self.timer < 0.15:
            return pic
        if time.time()-self.timer < 0.30:
            return self.get_bigger(pic)
        if time.time()-self.timer < 0.45:
            return pic
        if time.time()-self.timer < 0.60:
            return self.get_smaller(pic)
        self.timer = time.time()

    def enemies_randomizer(self):
        from random import randrange
        return randrange(1000, 2000, 100)
