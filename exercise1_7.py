#exercise 1 part 7
#Now make a square rotate continuously, one full revolution (360 degrees) per second

import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="red",fillColor="red",size=[100,100],pos=[0,0])
degreesIncr = 45
degreesRot = 360
perTime = 1.0
win.flip()
square.draw()
win.flip()
for num in range (degreesRot/degreesIncr):
    core.wait(perTime/(degreesRot/degreesIncr))
    win.flip()
    square.ori+=degreesIncr
    square.draw()
    win.flip()
sys.exit()
