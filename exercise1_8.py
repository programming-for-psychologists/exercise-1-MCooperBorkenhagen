#exercise 1 part 8
#Now make a square rotate continuously, one full revolution
#(360 degrees) per second
# and make the rotating square stop rotating when you press the 's' key

import time
import sys
from psychopy import visual,event,core


win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="red",fillColor="red",size=[100,100],pos=[0,0])
while True:
   square.draw()
   square.ori += 5
   win.flip()
   if event.getKeys(['s']):
       break
