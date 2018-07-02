#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame import *
from player import *
from blocks import *
from camera import *

# screen variables -->
win_width = 880
win_height = 500
display = (win_width, win_height)
background_color = (110, 140, 112)
# screen variables <--

# 22/05/2018 -->
level = []
entities = pygame.sprite.Group()
platforms = []
# animated_entities = pygame.sprite.Group()
# 22/05/2018 <--

# 30/06/2018 add -->
class Background(sprite.Sprite):
    def __init__(self, x, y):
        w, h = 5274,2000
        sprite.Sprite.__init__(self)
        self.image = Surface((w, h))
        self.image = image.load('graphics/bg_m.png')
        self.rect = Rect(x, y, w, h)
# 30/06/2018 add <--


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + win_width / 2, -t + win_height / 2

    l = min(0, l)
    l = max(-(w-win_width), l)
    t = max(-(h-win_height), t)
    t = min(0, t)

    return Rect(l, t, w, h)


# 22/05/2018 -->
def load_level():
    global player_x, player_y
    level_file = open('levels/level_01.lvl')
    line = " "
    commands = []
    while line[0] != "/":
        line = level_file.readline()
        if line[0] == "[":
            line = level_file.readline()
            while line[0] != "]" and line[0] != "\n":
                end_line = line.find("|")
                level.append(line[0:end_line])
                line = line[end_line+1:]
            line = level_file.readline()
        if line != "":
            commands = line.split()
            if len(commands) > 1:
                if commands[0] == 'player':
                    player_x = int(commands[1])
                    player_y = int(commands[2])
                if commands[0] == 'teleport':
                    tp = Teleport(int(commands[1]), int(commands[2]),
                                  int(commands[3]), int(commands[4]))
                    entities.add(tp)
                    platforms.append(tp)

# 22/05/2018 <--


def main():
    # screen initiation -->
    pygame.init()
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption('SMB')
    # screen initiation <--

    # background -->
    moving = True
    if moving:
        bg = Background(0,0)
        screen.blit(bg.image,(0,0))
        bg_t = Background(0,0)
        bg_t.image = image.load('graphics/bg_t.png')
    else:
        bg = Surface(display)
        bg.fill(background_color)
        bg_image = image.load('graphics/bg_01.png')
        bg.blit(bg_image, (0,0))
    # background <--

    # 22/05/2018 upd -->
    load_level()
    hero = Player(player_x, player_y)
    entities.add(hero)
    '''
    hero = Player(55,55)
    '''
    # 22/05/2018 upd <--
    left = right = False
    up = False
    running = False

    timer = pygame.time.Clock()

    # 22/05/2018 upd -->
    '''
    entities = pygame.sprite.Group()
    platforms = []
    # animated_entities = pygame.sprite.Group()
    entities.add(hero)
    '''
    # 22/05/2018 upd <--

    # 22/05/2018 upd -->
    '''
    level = [
            "--------------",
            "-            -",
            "-   ---      -",
            "-          ---",
            "--           -",
            "---   ----   -",
            "-            -",
            "-------     --",
            "-        --  -",
            "-            -",
            "-     --     -",
            "-          ---",
            "---          -",
            "--    ----   -",
            "-            -",
            "-------     --",
            "-       ---  -",
            "--------------",
        ]
        level = [
            "----------------------------------------",
            "-   -                                  -",
            "-       -   -            --        -----",
            "-        - -    - -                    -",
            "-     -             --         -       -",
            "-    -           -            -        -",
            "-            -                -  -     -",
            "-               -   --                 -",
            "-          -     --           -       --",
            "-       --   -                         -",
            "---            -  -              - -   -",
            "--         -      -  - -   -          --",
            "-                               -      -",
            "-                   -     -       -  - -",
            "-              -               -       -",
            "-         -    -            -          -",
            "-            -                         -",
            "--       -           -        -  --    -",
            "-       -       -           -          -",
            "-         --      -              -     -",
            "-   -             -      - -          --",
            "-           -               -          -",
            "-    -- -     -     -            -     -",
            "-                     --      -      - -",
            "-    --     -                       -  -",
            "-     -       -                        -",
            "-                      -         -     -",
            "-      --    -    -                    -",
            "--              -     -                -",
            "-- -          -                       --",
            "-      -    -    -                    --",
            "-          -   -         -          -  -",
            "-                       --     -       -",
            "-     -          - -  -  -       - -   -",
            "-     -             -         -        -",
            "-   -      -                        -  -",
            "-                            -         -",
            "-                                -    --",
            "- -     _     -     *      -      -    -",
            "-   --   -                 -      --   -",
            "----------------------------------------"
        ]
    '''
    # 22/05/2018 upd <--

    # level drawing -->
    print(level)
    x = y = 0
    for row in level:
        for col in row:
            # 11.04.2018 upd -->
            if col == '-':
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            # 24.04.2018 add -->
            elif col == '*':
                db = DeathBlock(x, y)
                entities.add(db)
                platforms.append(db)
            elif col == '_':
                dms = DeathMovingSaw(x, y)
                entities.add(dms)
                platforms.append(dms)
            # 24.04.2018 add <--
            '''
            if col=='-':
                pf = Surface(platform)
                pf.fill(platform_color)
                screen.blit(pf, (x,y))
            '''
            # 11.04.2018 upd <--
            x += platform_width
        y += platform_height
        x = 0
    # 22/05/2018 upd -->
    '''
    tp = Teleport(144, 576, 144, 48)
        entities.add(tp)
        platforms.append(tp)
    '''
    # 22/05/2018 upd <--
    # animated_entities.add(tp)
    # level drawing <--

    total_level_width = len(level[0])*platform_width
    total_level_height = len(level)*platform_height
    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            # 24.04.2018 add -->
            if e.type == KEYDOWN and e.key == K_LSHIFT:
                running = True
            if e.type == KEYUP and e.key == K_LSHIFT:
                running = False
            # 24.04.2018 add <--
        
        # 2906 replace -->
        # new code below
        '''
        screen.blit(bg, (0, 0))  # background drawing
        '''
        # 2906 replace

        hero.update(left, right, up, running, platforms)
        # animated_entities.update()
        # for e in moving_platforms:
        #     e.get_move()
        # 11.04.2018 upd -->
        # 11.04.2018 upd -->
        camera.update(hero)
        # 2906 replace -->
        if moving:
            screen.blit(bg.image, camera.apply(bg, smooth=0.5))
            screen.blit(bg_t.image, camera.apply(bg_t, smooth=0.7))
        else:
            screen.blit(bg_image, (0, 0))  # background drawing
        # 2906 replace
        for e in entities:
            if isinstance(e, blocks.DeathMovingSaw):
                e.get_move()
            screen.blit(e.image, camera.apply(e))
        # entities.draw(screen)
        '''
        entities.draw(screen)
        '''
        # 11.04.2018 upd <--
        '''
        hero.draw(screen)
        '''
        # 11.04.2018 upd <--

        pygame.display.update()


if __name__ == '__main__':
    main()
