#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:10:03 2019

@author: nicholascooper

Primitive drawing functions

https://www.pygame.org/docs/tut/tom_games2.html#makegames-2

https://inventwithpython.com/pygame/chapter2.html

"""

import pygame
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

