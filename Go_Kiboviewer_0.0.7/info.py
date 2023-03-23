import pygame, sys
from pygame.locals import *

def main() :
    pygame.init()
    screen=pygame.display.set_mode((309,473))
    pygame.display.set_caption('도움말')

    fps=10
    fpsClock=pygame.time.Clock()
    LEFT=1
    WHITE=(255,255,255)
    imginfo=pygame.image.load('./image/info.png')

    while 1 :
        for event in pygame.event.get() :
            if event.type==QUIT :
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==LEFT :
                position=pygame.mouse.get_pos()
                if position[0]>=74 and position[0]<=237 and position[1]>=411 and position[1]<=450 :
                    pygame.quit()
                    return 0
        screen.fill(WHITE)
        screen.blit(imginfo,(0,0))
        pygame.display.flip()
