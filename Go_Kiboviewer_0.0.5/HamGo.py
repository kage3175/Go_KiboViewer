import mainmenu
import kiboopen
import savemode
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
                break'''

while 1 :
    if k==0 :
        k=mainmenu.main()
    if k==1 :
        k=savemode.kibosave()
    if k==2 :
        k=kiboopen.kiboopen()
