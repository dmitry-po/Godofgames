from pygame import *

move_speed = 5
width = 65
height = 95

class Enemy(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y

        self.image = Surface((width, height))
        self.image = image.load('graphics/hero/hero_l01.png')
        self.rect = Rect(x, y, width, height)
    
    def move(self):
        self.rect.x += 3
        #self.image.blit(self.image, (self.rect.x, self.rect.y))