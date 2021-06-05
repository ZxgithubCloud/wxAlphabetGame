import sys, pygame
import os

pwd = os.path.abspath('.')

pygame.init()

size = width, height = 1200, 650
speed = [0, 1]
#speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

balldir = os.path.abspath('.') + '/pygame/resources/'
a_dir = balldir + 'a.png'
ball = pygame.image.load(a_dir)
ballrect = ball.get_rect()

Aball = pygame.image.load(a_dir)
Aballrect = Aball.get_rect()

Bball = pygame.image.load(a_dir)
Bballrect = Bball.get_rect()
#ballrect = Aballrect


fireball = pygame.image.load(a_dir)
fireballrect = fireball.get_rect()


ballrect.left += 120

CurrentAlphabit = pygame.K_a
isFire = False
rightInput = False

firexValue = ballrect.left
xValue = ballrect.left
yValue = ballrect.bottom

while 1:
    #pygame.event.set_grab(True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pygame.KEYDOWN == event.type:
            if (event.key == pygame.K_b and pygame.K_b == CurrentAlphabit):
                xValue = ballrect.left;
                yValue = ballrect.top;
                ballrect = Aballrect
                ball = Aball
                CurrentAlphabit = pygame.K_a
                isFire = True
                ballrect.left += 20
                if ballrect.right > width:
                    ballrect.left = 30
            if (event.key == pygame.K_a and  pygame.K_a == CurrentAlphabit) :
                xValue = ballrect.left;
                yValue = ballrect.top;
                ballrect = Bballrect
                ball = Bball

                ballrect.left += 20
                isFire = True
                rightInput = True
                CurrentAlphabit = pygame.K_b 
                
                if ballrect.right > width:
                    ballrect.left = 30

    if isFire:
        fireballrect.left = xValue
        #fireballrect.right = Aballrect.right
        fireballrect.top = yValue
        #fireballrect.bottom = Aballrect.bottom
        screen.fill(black)
        screen.blit(fireball, fireballrect)
        pygame.display.flip()
        pygame.time.wait(300)
        screen.fill(black)
        pygame.display.flip()
        #pygame.display.quit()
        #screen.clear()
        xValue = ballrect.left
        yValue = ballrect.bottom
        isFire = False
        continue;
    
    pygame.time.wait(3)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)

    pygame.display.flip()


