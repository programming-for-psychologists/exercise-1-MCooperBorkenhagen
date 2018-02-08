#exercise 1 part 6
#Show a red square for 1 s then change its orientation by 45-deg


import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="red",fillColor="red",size=[100,100],pos=[0,0])
square.draw()
win.flip()
core.wait(1.0)
win.flip()
square.setOri(45)
square.draw()
win.flip()
core.wait(1.0)
sys.exit()
