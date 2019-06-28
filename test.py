import pygame
import sys
import random as rd


pygame.init()

WIDTH = 500
HEIGHT = 500
WHITE = (255,255,255)
playerPosition = [250,375]
playerSize = 20
BACKGROUND = (0,0,0)
SPEED = 5

enemySize = 20
enemyPosition = [480,25]
enemyList = [enemyPosition]

RED = (255,0,0)
enemyLine = [25,75,125, 175, 225, 275]


screen = pygame.display.set_mode((WIDTH, HEIGHT))

gameOver = False

clock = pygame.time.Clock()

def updateEnemyPosition(enemyList):
    for idx, enemyPosition in enumerate(enemyList):
        if enemyPosition[0] > 0:
            enemyPosition[0] -= SPEED
        # if enemyPosition[0] == 0:
        #    enemyPosition[0] = 480
        #    enemyPosition[1] = enemyLine[ rd.randint(0, 5) ]
        else:
            enemyList.pop(idx)

def collisionCheck(enemyList, playerPosition) -> bool:
    for enemyPosition in enemyList:
        if detectCollision(playerPosition, enemyPosition):
            return True
    return False


def dropEnemies(enemyList):
    delay = rd.random()
    if len(enemyList) < 10 and delay < 0.1:
        yP = enemyLine[ rd.randint(0, 5)]
        xP = 480
        enemyList.append([xP,yP])

def drawEnemy(enemyList):
    for enemy in enemyList:
        pygame.draw.circle(screen, RED, enemy, enemySize, 0)


def detectCollision(playerPosition, enemyPosition) -> bool:
    pX = playerPosition[0]
    pY = playerPosition[1]

    eX = enemyPosition[0]
    eY = enemyPosition[1]

    # if eX > pX and eX < (pX + playerSize) :
    #     return True
    if eY >= pY and eY <= (pY + playerSize) and eX > pX and eX < (pX + playerSize):
        return True
    else:
        return False



while not gameOver:

    for event in pygame.event.get():

        x = playerPosition[0]
        y = playerPosition[1]

        if event.type == pygame.QUIT:
            sys.exit()

#update position of player
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                y -= 50
            elif event.key == pygame.K_DOWN:
                y += 50
            elif event.key == pygame.K_LEFT:
                x -= 40
            elif event.key == pygame.K_RIGHT:
                x += 40

            playerPosition = [x,y]

    screen.fill(BACKGROUND)

#update animation of the enemy
    # if enemyPosition[0] > 0:
    #     enemyPosition[0] -= 10
    # if enemyPosition[0] == 0:
    #     enemyPosition[0] = 480
    #     enemyPosition[1] = enemyLine[ rd.randint(0, 5) ]

    pygame.draw.line(screen, WHITE, (0,50), (WIDTH,50), 5)
    pygame.draw.line(screen, WHITE, (0, 100), (WIDTH, 100), 5)
    pygame.draw.line(screen, WHITE, (0, 150), (WIDTH, 150), 5)
    pygame.draw.line(screen, WHITE, (0, 200), (WIDTH, 200), 5)
    pygame.draw.line(screen, WHITE, (0, 250), (WIDTH, 250), 5)

    pygame.draw.circle(screen, WHITE, playerPosition, playerSize, 0)

    dropEnemies(enemyList)
    updateEnemyPosition(enemyList)
    if collisionCheck(enemyList, playerPosition):
        gameOver = True
        break

    drawEnemy(enemyList)


    clock.tick(60)

    pygame.display.update()

    if detectCollision(playerPosition, enemyPosition):
        gameOver = True