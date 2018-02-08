# Exercise 1 part 9
#Make a square stop rotating when you press 's' and then
#start rotating again when you press 'r'

import time
import sys
from psychopy import visual,event,core


win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="red",fillColor="red",size=[100,100],pos=[0,0])
while True:
   square.ori += 5
   square.draw()
   win.flip()
   if event.getKeys('s'):
       event.waitKeys(keyList='r')
    if event.getKeys(['space']):
        break
