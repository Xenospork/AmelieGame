# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:40:33 2018

@author: matth
"""

import os
import pygame

white = (255,255,255)
red = (255,0,0)
# image references
rDir = "resources"
charPng = "charTest.png"


charPngRef = os.path.join(rDir,charPng)

class char(pygame.sprite.Sprite):
        def __init__(self,scale,speed):
            super().__init__()
            ##########################################This will give us the dimensions of the sprite
            charImgRaw = pygame.image.load(charPngRef)
            charRectRaw = charImgRaw.get_rect()
            wRaw = charRectRaw.width
            hRaw = charRectRaw.height
            ########################################## and this will scale these dimensions
            self.speed = speed
            self.charImg = pygame.transform.scale(charImgRaw,(int(wRaw*scale),int(hRaw*scale)))
            self.charRect = self.charImg.get_rect()
            self.dx = 0
            self.dy = 0
        def move(self):
            self.charRect.x += self.dx
            self.charRect.y += self.dy

class wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.wallSurface = pygame.Surface([50,50])
        self.wallSurface.fill(red)
        self.wallRect = self.wallSurface.get_rect()
        self.wallRect.x = 300
        self.wallRect.y = 300
            
c = char(0.1,5)
w = wall()

pygame.init()

display_width = 800 #Defining these here, as I will create sprites that are located at some fraction of these lengths
display_height = 600
screen = pygame.display.set_mode([display_width,display_height])

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Collision Detection Test")

screen.blit(w.wallSurface,w.wallRect)

finished = False
clock = pygame.time.Clock()

allSpriteGroup = pygame.sprite.Group()
wallSpriteGroup = pygame.sprite.Group()

allSpriteGroup.add(c)
allSpriteGroup.add(w)

wallSpriteGroup.add(w)
collideTest = False

while not finished:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            finished = True
    screen.fill(white)
    wallSpriteGroup.draw(screen)
    #screen.blit(w.wallSurface,w.wallRect)
  
    

  


    if event.type == pygame.KEYDOWN:# and collideTest == False:
        if event.key == pygame.K_DOWN:
            c.dy += c.speed
        elif event.key == pygame.K_UP:
            c.dy += -c.speed
        elif event.key == pygame.K_LEFT:
            c.dx += -c.speed
        elif event.key == pygame.K_RIGHT:
            c.dx += c.speed
    c.move()   
    screen.blit(c.charImg,c.charRect)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            c.dy = 0 
        elif event.key == pygame.K_UP:
            c.dy = 0
        elif event.key == pygame.K_LEFT:
            c.dx = 0
        elif event.key == pygame.K_RIGHT:
            c.dx = 0
  ###################################### 
   ######################################
    if w.wallRect.colliderect(c.charRect):
        collideTest = True
        if c.dy < 0:
            c.charRect.y = w.wallRect.y + w.wallRect.height
            c.dy = 0#-c.dy
        elif c.dy > 0:
            c.charRect.y = w.wallRect.y - c.charRect.height
            c.dy = 0#-c.dy
        elif c.dx < 0:
            c.charRect.x = w.wallRect.x + w.wallRect.width
            c.dx = 0
        elif c.dx > 0:
            c.charRect.x = w.wallRect.x - c.charRect.width
    else:
        collideTest = False
 ####################################### 
       

    c.dx = 0
    c.dy = 0
    pygame.display.update()
    clock.tick(60)

pygame.quit()
            
            