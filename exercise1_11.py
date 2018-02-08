#exercise 1 part 11
#Make the rectangle decrease/increase its width by 10% of its current width with each keypress instead of 10 pixels

import time
import sys
from psychopy import visual,event,core


win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="red",fillColor="red",units='pix', pos=[0,0])
square.size = [200,200]
square.draw()
win.flip()
while True:
    sizeThen = square.size
    increment = sizeThen*[1.10,0]
    decrement = sizeThen*[.90,0]
    if event.getKeys(['left']):
        square.size += increment
        square.draw()
        win.flip()
    if event.getKeys(['right']):
        square.size -= decrement
        square.draw()
        win.flip()
    if event.getKeys(['space']):
        break
