# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 19:52:50 2018

@author: matth
"""
import pygame

display_width = 800 #Defining these here, as I will create sprites that are located at some fraction of these lengths
display_height = 600

pygame.init()

gameDisplay = pygame.display.set_mode((display_width,display_height)) #This defines the canvas - the window that comes up on the screen
pygame.display.set_caption('Hello world') #This is what the window is called

black = (0,0,0) #rgb definitions of these colours to prevent us having to type out the numbers later
white = (255,255,255)

bunScale = 0.5
bunWidth = int(bunScale*537)#These are the original dimensions of the bunny. I'll use them to scale the bunny in a second.
bunHeight = int(bunScale*784)

bunImg = pygame.transform.scale(pygame.image.load("resources\\bunny.png"),(bunWidth,bunHeight)) #defining bunImg, which means we can use the bunny image later on

def bunny(x,y):
    gameDisplay.blit(bunImg,(x,y)) #Defines a function. every time we type in bunny(x,y), the game will display our bunny image at location (x,y)

x =  (display_width-bunWidth)
y = (display_height * 0) # There we are, this is where the bunny will start
#pygame.transform.scale(pygame.image.load(r'sprites\enemies\runningleft-5.png'), (130, 100))
clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
        
    gameDisplay.fill(white)
    bunny(x,y) # let's try putting the bunny on the screen

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
