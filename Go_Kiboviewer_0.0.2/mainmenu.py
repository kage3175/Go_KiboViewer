import pygame, sys
from pygame.locals import *
import savemode
import kiboopen

pygame.init()
screen=pygame.display.set_mode((350,350))
pygame.display.set_caption('메인 메뉴')

fps=20
fpsClock=pygame.time.Clock()
LEFT=1
WHITE=(255,255,255)
BLACK=(0,0,0)

while 1 :
    for event in pygame.event.get() :
        if event.type==QUIT :
            pygame.quit()
            sys.exit()
        if event.type==MOUSEBUTTONDOWN and event.button==LEFT :
            position=pygame.mouse.get_pos()
            if position[0]>=50 and position[0]<=300 and position[1]>=50 and position[1]<=100 :
                pygame.quit()
                savemode.kibosave()
            if position[0]>=50 and position[0]<=300 and position[1]>=125 and position[1]<=175 :
                pygame.quit()
                kiboopen.kiboopen()
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (50,50,250,50), 1)
    pygame.draw.rect(screen, BLACK, (50,125,250,50), 1)
    pygame.display.flip()
    
