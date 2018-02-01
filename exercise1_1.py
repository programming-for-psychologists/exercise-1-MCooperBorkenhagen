# excercise 1 part 3
#Show a red square for 1 s, then switch it to blue and show it for 1 s

# exercise 1 part 4
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100],pos=[0,0])
square_red.draw()
win.flip()
core.wait(1.0)
win.flip()
square_blue.draw()
win.flip()
core.wait(1.0)
sys.exit()
