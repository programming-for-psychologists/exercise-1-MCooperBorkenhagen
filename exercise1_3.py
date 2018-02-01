#exercise1_3.py
# exercise 1 part 5:
#Show the following sequence: blue, red, blue, red, blue, red
# (with each square appearing for 1 s with a 50 ms blank screen in the middle).
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100],pos=[0,0])
n=3
interval1 = 1.0
interval2 = .5
for num in range(n):
    square_red.draw()
    win.flip()
    core.wait(interval1)
    win.flip()
    core.wait(interval2)
    square_blue.draw()
    win.flip()
    core.wait(interval1)
    win.flip()
    core.wait(interval2)
sys.exit()
