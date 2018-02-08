#exercise1_11
#something creative


import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square_left = visual.Polygon(win,lineColor="pink",fillColor="yellow",size=[100,100],pos=[-100,0])
square_right = visual.Line(win,lineColor="pink",fillColor="turquoise",size=[100,200],pos=[100,0])
square_left.draw()
square_right.draw()
win.flip()
while True:
    square_left.ori += 5
    square_left.draw()
    square_right.ori += -5
    square_right.draw()
    win.flip()
    core.wait(.05)
    if event.getKeys(['space']):
        break
win.close()
sys.exit()
