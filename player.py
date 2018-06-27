#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pygame import *
import pyganim
from pyganim import *
import blocks

move_speed = 5
# 05/06/2018 -->
move_decay = 1
# 05/06/2018 <--
# 24.04.2018 add -->
move_extra_speed = 2
jump_extra_power = 2
# 24.04.2018 add <--
jump_power = 7
gravity = 0.35
width = 32
height = 47
color = (69, 69, 69)
color = (255, 255, 255)
# 2706 add -->
color = (110, 140, 112)
# 2706 add <--


# add animation -->
animation_delay = 50
# 24.04.2018 add -->
animation_delay_speed = 3
# 24.04.2018 add <--
# 2706 replace -->
animation_right = [
    ('graphics/hero/hero_r01.png')
]
animation_left = [
    ('graphics/hero/hero_l01.png')
]
'''
animation_right = [
    ('graphics/hero/r1.png'),
    ('graphics/hero/r2.png'),
    ('graphics/hero/r3.png'),
    ('graphics/hero/r4.png'),
    ('graphics/hero/r5.png'),
    ('graphics/hero/r6.png'),
]
animation_left = [
    ('graphics/hero/l1.png')
]
'''
# 2706 replace <--
animation_stay = [('graphics/hero/0.png', animation_delay)]
# add animation <--


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)

        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.onGround = False

        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = Rect(x, y, width, height)

        # animation -->
        self.image.set_colorkey(color)

        # 24.04.2018 upd -->
        bolt_anim = []
        bolt_anim_speed = []
        for anim in animation_right:
            bolt_anim.append((anim, animation_delay))
            bolt_anim_speed.append((anim, animation_delay_speed))
        self.bolt_anim_right = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_right.play()
        self.bolt_anim_right_speed = pyganim.PygAnimation(bolt_anim_speed)
        self.bolt_anim_right_speed.play()
        '''
        bolt_anim = []
                for anim in animation_right:
                    bolt_anim.append((anim, animation_delay))
                self.bolt_anim_right = pyganim.PygAnimation(bolt_anim)
                self.bolt_anim_right.play()
        '''
        # 24.04.2018 upd <--

        # 24.04.2018 upd -->
        bolt_anim = []
        bolt_anim_speed = []
        for anim in animation_left:
            bolt_anim.append((anim, animation_delay))
            bolt_anim_speed.append((anim, animation_delay_speed))
        self.bolt_anim_left = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_left.play()
        self.bolt_anim_left_speed = pyganim.PygAnimation(bolt_anim_speed)
        self.bolt_anim_left_speed.play()
        '''
        bolt_anim = []
                for anim in animation_left:
                    bolt_anim.append((anim, animation_delay))
                self.bolt_anim_left = pyganim.PygAnimation(bolt_anim)
                self.bolt_anim_left.play()
        '''
        # 24.04.2018 upd <--

        self.bolt_anim_stay = pyganim.PygAnimation(animation_stay)
        self.bolt_anim_stay.play()
        self.bolt_anim_stay.blit(self.image, (0, 0))
        # animation <--

    # 24.04.2018 upd -->
    '''
    def update(self, left, right, up, platforms):
    '''
    def update(self, left, right, up, running, platforms):
        # 24.04.2018 upd <--
        if up:
            if self.onGround:  # disable for fly mode
                self.yvel = -jump_power
                # 24.04.2018 add -->
                if running:
                    self.yvel -= jump_extra_power
                # 24.04.2018 add <--

        if left:
            self.xvel = -move_speed
            # 13.04.2018 add animation -->
            # 24.04.2018 upd -->
            if running:
                self.xvel -= move_extra_speed
                self.bolt_anim_left_speed.blit(self.image, (0, 0))
            else:
                self.bolt_anim_left.blit(self.image, (0, 0))
            '''
            self.bolt_anim_left.blit(self.image, (0, 0))
            '''
            # 24.04.2018 upd <--
            # 13.04.2018 add animation <--

        if right:
            self.xvel = move_speed
            # 13.04.2018 add animation -->
            # 24.04.2018 upd -->
            if running:
                self.xvel += move_extra_speed
                self.bolt_anim_right_speed.blit(self.image, (0, 0))
            else:
                self.bolt_anim_right.blit(self.image, (0, 0))
            '''
            self.bolt_anim_right.blit(self.image, (0, 0))
            '''
            # 24.04.2018 upd <--
            # 13.04.2018 add animation <--

        if not(left or right):
            # 05/06/2018 upd -->
            if self.xvel != 0:
                if self.xvel > 0:
                    self.xvel -= move_decay
                else:
                    self.xvel += move_decay
            '''
            self.xvel = 0
            '''
            # 05/06/2018 upd <--
            # 13.04.2018 add animation -->
            # self.bolt_anim_stay.blit(self.image, (0, 0))
            # 13.04.2018 add animation <--

        if not self.onGround:
            self.yvel += gravity

        self.onGround = False;
        # 11.04.2018 upd -->
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        '''
        self.rect.y += self.yvel
                self.rect.x += self.xvel
        '''
        # 11.04.2018 upd <--

    # 11.04.2018 upd -->
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, blocks.DeathBlock):
                    self.die()
                elif isinstance(p, blocks.Teleport):
                    self.teleport(p.goX, p.goY)
                else:
                    if xvel > 0:
                        self.rect.right = p.rect.left
                        # 06/06/2018 -->
                        self.xvel = 0
                        # 06/06/2018 <--
                    if xvel < 0:
                        self.rect.left = p.rect.right
                        # 06/06/2018 -->
                        self.xvel = 0
                        # 06/06/2018 <--
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0
                    if (xvel == 0) and (isinstance(p, blocks.DeathMovingSaw)):
                        if p.position_move_right:
                            self.rect.left = p.rect.right
                        else:
                            self.rect.right = p.rect.left
    '''
        def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))
    '''
    # 11.04.2018 upd <--
    # 24.04.2018 add -->
    def die(self):
        time.sleep(5)
        self.teleport(55, 55)

    def teleport(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
    # 24.04.2018 add <--
