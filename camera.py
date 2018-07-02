#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pygame import *


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target, smooth=1):
        l, t, w, h = self.state
        # 02/07/18 replace -->
        return_state = Rect(l*smooth,
                            t*smooth,
                            w,
                            h)
        return target.rect.move(return_state.topleft)
        # return target.rect.move(self.state.topleft)
        # 02/07/18 replace <--

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
