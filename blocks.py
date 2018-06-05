#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pygame import *

# levels variables -->
platform_width = 48
platform_height = 48
platform = (platform_width, platform_height)
platform_color = (40, 10, 12)
color = (255, 255, 255)
# levels variables <--


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface(platform)
        # 21/05/2018 upd -->
        self.image.fill(platform_color)
        '''
        self.image = image.load('graphics/block.png')
        '''
        # 21/05/2018 upd <--
        self.rect = Rect(x, y, platform_width, platform_height)


class DeathBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.set_colorkey(color)
        self.image = image.load('graphics/death.png')


class DeathMovingSaw(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(platform_color)
        self.position_start = 0
        self.position_end = 100
        self.position_now = 0
        self.position_move_right = True

    def get_move(self):
        if self.position_move_right:
            if self.position_now < self.position_end:
                self.position_now += 1
                self.move(1)
            else:
                self.position_now -= 1
                self.position_move_right = False
                self.move(-1)
        else:
            if self.position_now > self.position_start:
                self.position_now -= 1
                self.move(-1)
            else:
                self.position_now += 1
                self.position_move_right = True
                self.move(1)

    def move(self, _x=0, _y=0):
        self.rect.x += _x
        self.rect.y += _y


class Teleport(Platform):
    def __init__(self,x, y,  goX, goY):
        Platform.__init__(self, x, y)
        self.goX = goX
        self.goY = goY
        self.image.fill((90, 10, 12))



