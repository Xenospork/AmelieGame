# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:40:33 2018

@author: matth
"""

import os
import pygame

class char(object):
        def __init__(self):
            self.charImg = pygame.image.load(os.path.join("resources","charTest.png"))
            self.charRect = self.charImg.get_rect()
        def move(self,dx,dy):
            
            