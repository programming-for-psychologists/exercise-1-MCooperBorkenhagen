#exercise 1 part 10
#Display a blue square and increase its width (making it a rectangle) by 10 pixels whenever the user presses the left-arrow key.
# Decrease the width by 10 pixels when the user presses the right-arrow key

import time
import sys
from psychopy import visual,event,core


win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="red",fillColor="red",units='pix', pos=[0,0])
square.size = [200,200]
square.draw()
win.flip()
increment = [10,0]
decrement = [-10,0]
while True:
    if event.getKeys(['left']):
        square.size += increment
        square.draw()
        win.flip()
    if event.getKeys(['right']):
        square.size += decrement
        square.draw()
        win.flip()
    if event.getKeys(['space']):
        break
