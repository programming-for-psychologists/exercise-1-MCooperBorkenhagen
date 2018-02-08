# excercise 1 part 3
#Show a red square for 1 s, then switch it to blue and show it for 1 s

# exercise 1 part 4
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100],pos=[0,0])
square.draw()
win.flip()
core.wait(1)
square.setFillColor('blue')
square.draw()
win.flip()
core.wait(1)
win.close()
sys.exit()
