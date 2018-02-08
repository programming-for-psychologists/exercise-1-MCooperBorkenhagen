#exercise1_3.py
# exercise 1 part 5:
#Show the following sequence: blue, red, blue, red, blue, red
# (with each square appearing for 1 s with a 50 ms blank screen in the middle).
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
interval1 = 1.0
interval2 = .5
for color in ['blue', 'red']*3:
    square.setFillColor(color)
    square.draw()
    win.flip()
    core.wait(interval1)
    win.flip()
    core.wait(interval2)
sys.exit()
