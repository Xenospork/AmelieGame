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

black = (255,0,0) #rgb definitions of these colours to prevent us having to type out the numbers later
white = (255,255,255)

backImg = pygame.transform.scale(pygame.image.load("resources\\background.png"),(display_width,display_height))
#gameDisplay.blit(backImg,(0,0))
bunScale = 0.5
charScale = 0.06
bunWidth = int(bunScale*537)#These are the original dimensions of the bunny. I'll use them to scale the bunny in a second.
bunHeight = int(bunScale*784)
charWidth = int(charScale*675)
charHeight = int(charScale*781)
bunImg = pygame.transform.scale(pygame.image.load("resources\\bunny.png"),(bunWidth,bunHeight)) #defining bunImg, which means we can use the bunny image later on
charImg = pygame.transform.scale(pygame.image.load("resources\\charTest.png"),(charWidth,charHeight))
charRect = charImg.get_rect()
bunRect = bunImg.get_rect()

def bunny():
    gameDisplay.blit(bunImg,bunRect) #Defines a function. every time we type in bunny(x,y), the game will display our bunny image at location (x,y)


def char():
    gameDisplay.blit(charImg,charRect)

bunRect.x =  (display_width-bunWidth)
bunRect.y = (display_height * 0) # There we are, this is where the bunny will start
#pygame.transform.scale(pygame.image.load(r'sprites\enemies\runningleft-5.png'), (130, 100))
clock = pygame.time.Clock()

crashed = False
charRect.x = 0
charRect.y = 0
ychar_change = 0
xchar_change = 0

thing_startx = 300
thing_starty = 400
thing_speed = 1
thing_width = 100
thing_height = 100
xCross = 0
yCross = 0 

class wall:
    def __init__(self,surface,x,y):
        self.surface = surface
        self.x = x
        self.y = y
    def drawWall(self):
        self.wallImg = pygame.draw.rect(self.surface,(255,0,0),(self.x,self.y,50,50),0)
        #self.surface.blit(self.wallImg)
maze = [
['.','.','w','w','w'],
['w','.','w','w','.'],
['.','.','w','.','.'],
['.','w','.','.','w'],
['.','.','.','w','w']
]
mazeX = 200
mazeY = 200
while not crashed:
######


    ######
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
        
    gameDisplay.fill(white)
    #gameDisplay.blit(backImg,(0,0))
    #pygame.draw.rect(gameDisplay,(255,0,0),(0,0,100,100),0)
    if event.type == pygame.KEYDOWN and not bunRect.colliderect(charRect):
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
    if charRect.y < 0:
        charRect.y = 0
    elif charRect.y > display_height-charHeight:
        charRect.y = display_height-charHeight
    if charRect.x < 0:
        charRect.x = 0
    elif charRect.x > display_width-charWidth:
        charRect.x = display_width - charWidth    
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == 'w':
                p = wall(gameDisplay,column*50,row*50)
                p.drawWall()
                if charRect.colliderect(p.wallImg):
                    charRect.y += -2*ychar_change
                    charRect.x += -2*xchar_change
                    ychar_change = 0
                    xchar_change = 0
                    
    charRect.y += ychar_change
    charRect.x += xchar_change    
    char()
    bunny() # let's try putting the bunny on the screen
    ######### Movement behaviour for character. When an arrow key is pressed, we assign a value to y/xchar_change
    ######### we update the xchar and ychar coordinates, and next time our character is drawn, we change the coordinates
    ######### when you let go of the key, the change variable is set to 0, and the position stops changing every frame

    '''if bunRect.colliderect(charRect): #Collision detection must take place at the end of loop, otherwise
        #there's a chance you'll collide after this detection, and you won't be able to get out!
        #print("collide")
        charRect.y += -2*ychar_change
        charRect.x += -2*xchar_change
        ychar_change = 0
        xchar_change = 0
    charRect.y += ychar_change
    charRect.x += xchar_change'''

   
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
