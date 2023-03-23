import mainmenu
import kiboopen
import savemode
import info
import pygame, sys
from tkinter import *

a=0
k=0
'''while 1 :
    if a==0 :
        if mainmenu.main()==1 :
            if savemode.kibosave()==0:
                break
        else :
            if kiboopen.kiboopen()==0:
                break''' # 0.0.5까지 쓰던 코드

while 1 :
    if k==0 : #시작시 k=0이기 때문에 무조건 얘부터 실행된다.
        k=mainmenu.main() #mainmenu를 한번 실행하고, return 값에 따라 기보 저장, 열기, 도움말이 실행된다.
    if k==1 :
        k=savemode.kibosave()
    if k==2 :
        k=kiboopen.kiboopen()
    if k==3 :
        k=info.main()
