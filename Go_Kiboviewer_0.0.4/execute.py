import mainmenu
import kiboopen
import savemode
import pygame, sys
from tkinter import *

a=0
while 1 :
    while a==0 :
        if mainmenu.main()==1 :
            if savemode.kibosave()==0:
                break
        else :
            if kiboopen.kiboopen()==0:
                break
