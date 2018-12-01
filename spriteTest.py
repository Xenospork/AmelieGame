# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:12:48 2018

@author: Desktop1
"""

import pygame

red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)

class wall(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,x,y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0
        self.walls = None
        pygame.draw.ellipse(self.image,colour, [0,0,width,height])
    def update(self):

        self.rect.y += self.dy
# Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list: 
            # Reset our position based on the top/bottom of the object.
            if self.dy > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        self.rect.x += self.dx
        for block in block_hit_list: 
            # Reset our position based on the top/bottom of the object.
            if self.dx > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

wall_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(4):
    x = (i+1)*100
    y = (i+1)*100
    wallSp = wall(red,50,50,x,y)  
    wall_list.add(wallSp)
    all_sprites_list.add(wallSp)

char = wall(blue,50,50,0,0)
char.walls = wall_list
all_sprites_list.add(char)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(white)
    all_sprites_list.draw(screen)
    
        # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            char.dy = 5
        elif event.key == pygame.K_UP:
            char.dy = -5
        elif event.key == pygame.K_RIGHT:
            char.dx = 5
        elif event.key == pygame.K_LEFT:
            char.dx = -5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP: 
            char.dy = 0
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
            char.dx = 0 
    all_sprite_list.update()


   

# Limit to 60 frames per second
    clock.tick(60)
    
pygame.quit()
