# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:12:48 2018

@author: Desktop1
"""

import pygame

red = (255,0,0)
white = (255,255,255)

class wall(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image,colour, [0,0,width,height])

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

wall_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(4):
    wallSp = wall(red,50,50)
    wallSp.rect.x = i*100
    wallSp.rect.y = i*100   
    wall_list.add(wallSp)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(white)
    wall_list.draw(screen)
    
        # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
    
pygame.quit()