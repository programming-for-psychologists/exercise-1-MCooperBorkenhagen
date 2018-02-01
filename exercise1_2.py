# exercise 1 part 4
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
square_red.draw()
win.flip()
core.wait(1.5)
win.flip()
core.wait(1.0)
n=3
for num in range(n):
    square_red.draw()
    win.flip()
    core.wait(.3)
    win.flip()
    core.wait(.5)
sys.exit()
