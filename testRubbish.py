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

container = pygame.Surface([10,10])

black = (0,0,0) #rgb definitions of these colours to prevent us having to type out the numbers later
white = (255,255,255)

bunScale = 0.5
charScale = 0.1
bunWidth = int(bunScale*537)#These are the original dimensions of the bunny. I'll use them to scale the bunny in a second.
bunHeight = int(bunScale*784)
charWidth = int(charScale*675)
charHeight = int(charScale*781)
bunImg = pygame.transform.scale(pygame.image.load("resources\\bunny.png"),(bunWidth,bunHeight)) #defining bunImg, which means we can use the bunny image later on
charImg = pygame.transform.scale(pygame.image.load("resources\\charTest.png"),(charWidth,charHeight))


def bunny(x,y):
    gameDisplay.blit(bunImg,(x,y)) #Defines a function. every time we type in bunny(x,y), the game will display our bunny image at location (x,y)
def char(x,y):
    gameDisplay.blit(charImg,(x,y))

x =  (display_width-bunWidth)
y = (display_height * 0) # There we are, this is where the bunny will start
#pygame.transform.scale(pygame.image.load(r'sprites\enemies\runningleft-5.png'), (130, 100))
clock = pygame.time.Clock()

crashed = False
xchar = 0
ychar = 0
ychar_change = 0
xchar_change = 0
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
        
    gameDisplay.fill(white)

    char(xchar,ychar)
    bunny(x,y) # let's try putting the bunny on the screen
    ######### Movement behaviour for character. When an arrow key is pressed, we assign a value to y/xchar_change
    ######### we update the xchar and ychar coordinates, and next time our character is drawn, we change the coordinates
    ######### when you let go of the key, the change variable is set to 0, and the position stops changing every frame
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            ychar_change = 5
        elif event.key == pygame.K_UP:
            ychar_change = -5
        elif event.key == pygame.K_RIGHT:
            xchar_change = 5
        elif event.key == pygame.K_LEFT:
            xchar_change = -5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP: 
            ychar_change = 0
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
            xchar_change = 0
    #########    
    ychar += ychar_change
    xchar += xchar_change
    if ychar < 0:
        ychar = 0
    elif ychar > display_height-charHeight:
        ychar = display_height-charHeight
    if xchar < 0:
        xchar = 0
    elif xchar > display_width-charWidth:
        xchar = display_width - charWidth
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
