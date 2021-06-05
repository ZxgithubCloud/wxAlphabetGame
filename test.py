
print("hello world.")
a = 100;
print(a)

def StreamToInt(inputStream):
    inputStream = "yeiurjdjf"
    intValues = int(inputStream)
     
inputStream = "yeiurjdjf"
intValues = ord(inputStream[0])
print("intvalues is: 0x%x", intValues)


import sys
import pygame
#import sys
from pygame.locals import *

pygame.init()
size = width, height = 800, 700
screen = pygame.display.set_mode(size)
color = (0, 0, 0)
color1 = (123,1,7)

clock = pygame.time.Clock()

while True:
    clock.tick(60)#限制60帧
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
    screen.fill(color)
    pygame.draw.rect(screen,color1,Rect(300,250,50,50))
    pygame.display.flip()

pygame.quit()
