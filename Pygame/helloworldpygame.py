#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:02:42 2019

@author: nicholascooper

Blank screen - Hello World

https://inventwithpython.com/pygame/chapter2.html


"""


import pygame, sys
from pygame.locals import *
#%%
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World!")
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:  # pygame.locals.QUIT
            pygame.quit()
            sys.exit()
    pygame.display.update()
