
#from pygameInterface import GetRightRect
import sys, pygame
import os
import common
import pygameInterface

#pwd = os.path.abspath('.')

def StartAlphabetGame(scoreValue):
    pygame.init()
    size = width, height = 1500, 900
    #speed = [0, 1]
    speed = [0, 1]
    #speed = [1, 1]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    currentRectInfo = pygameInterface.GetCurrentBallRect()
    rightRectInfo = pygameInterface.GetRightRect()
    failRectInfo = pygameInterface.GetFailRect()


    ballRect = currentRectInfo['rect']
    ball = currentRectInfo['ball']
    currentAlphabit = ord(currentRectInfo['alphabet'])

    randomSeed = width - ballRect.right
    randomValue = common.GetRandomValue(randomSeed)

    ballRect.left = ballRect.left + randomValue

    xValue = ballRect.left
    yValue = ballRect.bottom
    isInputHappen = False
    rightInput = False

    #update score value.
    scoreValue['right'] = 0
    scoreValue['wrong'] = 0

    while 1:
        isInputHappen = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #sys.exit()
                pygame.quit()
            if pygame.KEYDOWN == event.type:
                isInputHappen = True
                xValue = ballRect.left;
                yValue = ballRect.top;
                if (event.key == currentAlphabit):
                    rightInput = True
                    scoreValue['right'] = scoreValue['right'] + 1
                else:
                    rightInput = False
                    scoreValue['wrong'] = scoreValue['wrong'] + 1


        #display input whether right 
        if isInputHappen:   
            currentRectInfo = pygameInterface.GetCurrentBallRect()
            ballRect = currentRectInfo['rect']
            ball = currentRectInfo['ball'] 
            currentAlphabit = ord(currentRectInfo['alphabet'])

            randomSeed = width - ballRect.right
            randomValue = common.GetRandomValue(randomSeed)

            ballRect.left = ballRect.left + randomValue
            #isInputHappen = False

            if rightInput:
                fireballrect = rightRectInfo['rect']
                fireball = rightRectInfo['ball']
            else:
                fireballrect = failRectInfo['rect']
                fireball = failRectInfo['ball']

            fireballrect.left = xValue
            fireballrect.top = yValue

            screen.fill(black)
            screen.blit(fireball, fireballrect)
            pygame.display.flip()
            pygame.time.wait(300)
            screen.fill(black)
            pygame.display.flip()
            rightInput = False
            continue

        # display alphabet
        #pygame.time.wait(3)
        pygame.time.wait(3)
        ballRect = ballRect.move(speed)
        if ballRect.left < 0 or ballRect.right > width:
            speed[0] = -speed[0]
        if ballRect.top < 0 or ballRect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballRect)

        pygame.display.flip()


