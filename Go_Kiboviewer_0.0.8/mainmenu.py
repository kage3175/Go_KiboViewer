import pygame, sys
from pygame.locals import *
import savemode
import kiboopen

def main() :
    pygame.init()
    screen=pygame.display.set_mode((350,300))
    pygame.display.set_caption('메인 메뉴')

    fps=20
    fpsClock=pygame.time.Clock()
    LEFT=1
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    fontObj = pygame.font.Font('./font/NanumGothic.ttf', 20)
    imgmain1=pygame.image.load('./image/main1.png')
    imgmain2=pygame.image.load('./image/main2.png')
    imgmain3=pygame.image.load('./image/main3.png')

    while 1 :
        for event in pygame.event.get() :
            if event.type==QUIT :
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==LEFT :
                position=pygame.mouse.get_pos()
                if position[0]>=27 and position[0]<=320 and position[1]>=53 and position[1]<=104 :
                    pygame.quit()
                    return 1
                    # savemode.kibosave()
                if position[0]>=27 and position[0]<=320 and position[1]>=128 and position[1]<=177 :
                    pygame.quit()
                    return 2
                    #kiboopen.kiboopen()
                if position[0]>=27 and position[0]<=320 and position[1]>=203 and position[1]<=252 :
                    pygame.quit()
                    return 3
        screen.fill(WHITE)
        '''pygame.draw.rect(screen, BLACK, (50,50,250,50), 1)
        pygame.draw.rect(screen, BLACK, (50,125,250,50), 1)
        textSurfaceObj1 = fontObj.render('기보 만들기', True, BLACK)
        textRectObj1=textSurfaceObj1.get_rect();
        textRectObj1.center =(175,75)
        textSurfaceObj2 = fontObj.render('기보 열기', True, BLACK)
        textRectObj2=textSurfaceObj2.get_rect();
        textRectObj2.center =(175,150)
        screen.blit(textSurfaceObj1, textRectObj1)
        screen.blit(textSurfaceObj2, textRectObj2)'''
        screen.blit(imgmain1,(25,50))
        screen.blit(imgmain2,(25,125))
        screen.blit(imgmain3,(25,200))
        pygame.display.flip()

# main()
