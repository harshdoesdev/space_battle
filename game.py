import pygame
import random
import math

# Initialize game window
pygame.init()

# Setting game canva with height and height
screen = pygame.display.set_mode((800, 600))

# Setting title of the game
pygame.display.set_caption('Space2D')

# Loading image with pygame
gameIcon = pygame.image.load('ufo.png')
# Setting game icon of the game
pygame.display.set_icon(gameIcon)

# Setting game background image for the game

background = pygame.image.load('background.jpg')

# Creating player

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

# Creating an horizently player value changer to move the character
playerX_change = 0


def createPlayer(x, y):
    screen.blit(playerImg, (x, y))

# Creating enemy

# declaring random height and width of enemy so that it can appear randomly in different places in canvas


enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)

# Creating an horizently enemy value changer to move the character
enemyX_change = 0.4
enemyY_change = 20


def createEnemy(x, y):
    screen.blit(enemyImg, (x, y))

# Creating collision method between bullet and enemy


def isCollided(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) +
                         (math.pow(enemyY - bulletY, 2))))

    if distance < 27:
        return True
    else:
        return False

# Creating collision method between player and enemy to make the game over


def isGameOver(playerX, playerY, enemyX, enemyY):
    dist = math.sqrt((math.pow(playerX - enemyX, 2) +
                      (math.pow(playerY - enemyY, 2))))
    
    if dist < 27:
        return True
    else:
        return False

# Creating bullet


bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"


def shootBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


# Creating an horizently enemy value changer to move the character
enemyX_change = 0.4
enemyY_change = 20


def createEnemy(x, y):
    screen.blit(enemyImg, (x, y))


# declaring score variables to check score of the game
score = 0


# Intialize game to infinite to run it until close
running = True

while running:

    # Setting game background canva color with RGB values
    screen.fill((0, 0, 0))

    # Initialize game background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Setting keyboard up and down key mechanism to move our player horizently in canvas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    shootBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Now changing our main player horizentaly value after each movements by keyboard
    playerX += playerX_change

    # Adding boundaries to our canvas for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Now changing our main enemy horizentaly value after each movements randomly
    enemyX += enemyX_change

    # Adding boundaries to our canvas for enemy
    if enemyX <= 0:
        enemyX_change = 0.4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.4
        enemyY += enemyY_change

    # Creating bullet shooting movement

    if bullet_state is "fire":
        #bulletX = playerX
        shootBullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Creating multiple shooting bullet movements

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Calling collided method
    collission = isCollided(enemyX, enemyY, bulletX, bulletY)

    # if collision occured then increase score and set bullet position to initial state
    if(collission):
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)

    # calling gameover method to check the game is over or not

    gameover = isGameOver(playerX,playerY,enemyX,enemyY)

    if gameover:
        exit()

    # Calling player and enemy creation method
    createPlayer(playerX, playerY)
    createEnemy(enemyX, enemyY)

    # update the display -> mandetory
    pygame.display.update()
