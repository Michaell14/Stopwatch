import pygame
import os
import random

#Initializes the pygame
pygame.init()

#Set screen size - with height and width in tuple()
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
 
#Image location is relative to current location in directory
icon = pygame.image.load("../PygameImages/ufo.png")


#Background Image
background=pygame.image.load("../PygameImages/background.png")

#Player
playerImg = pygame.image.load("../PygameImages/space-invaders.png")
playerX = 370
playerY = 480
playerX_change=0

#Enemy
enemyImg=pygame.image.load("../PygameImages/alien.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change=1.5
enemyY_change=25

#Bullet
bullet= pygame.image.load("../PygameImages/b.png")
bulletX = 370+32-2.5
bulletY=480
bullet_change=0
bullet_state=True

pygame.display.set_icon(icon)

def player(playerX,playerY):
    screen.blit(playerImg, (playerX, playerY))

def enemy(enemyX,enemyY):
    screen.blit(enemyImg, (enemyX, enemyY))
def bulletFunc(bX, bY):
    screen.blit(bullet, (bX, bY))
    
#Runs the program
isRunning=True
while (isRunning):
    #Background COLOR - RGB Tuple
    screen.fill((112,128,144))

    #Background image
    screen.blit(background, (0,0))
    
    #Checks for events in pygame.event
    for event in pygame.event.get():
        #Checks if the window is closed and ends the program
        if (event.type == pygame.QUIT):
            isRunning = False

        #Changing player position if key is pressed
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT): 
                playerX_change = -4
            if (event.key == pygame.K_RIGHT):
                playerX_change = 4
            if (event.key==pygame.K_SPACE):
                bullet_change=-7
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change=0
                

    if (playerX <=0):
        playerX=0
    if (playerX>=736):
        playerX=736

    if (enemyX <=0):
        enemyX_change=1.5
        enemyY+=enemyY_change
    if (enemyX>=768):
        enemyX_change=-1.5
        enemyY+=enemyY_change
        
    enemyX+=enemyX_change
    playerX+=playerX_change

    bulletX=playerX+32-2.5
    bulletY=playerY
    bulletY-=bullet_change
    bulletFunc(bulletX, bulletY)
    player(playerX, playerY) 
    enemy(enemyX, enemyY)

    
    #Updates Screen - NEEDED
    pygame.display.update()







