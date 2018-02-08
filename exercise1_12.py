#Excercise 1 part 12
#Show two rotating squares simultaneously, one left of center rotating clockwise,
#the other right of center, rotating counterclockwise
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square_left = visual.Rect(win,lineColor="black",fillColor="purple",size=[100,100],pos=[-100,0])
square_right = visual.Rect(win,lineColor="black",fillColor="purple",size=[100,100],pos=[100,0])
square_left.draw()
square_right.draw()
win.flip()

while not event.getKeys(keyList=['q']):
    square_left.ori += 6
    square_right.ori += -6
    square_left.draw()
    square_right.draw()
    win.flip()
win.close()
sys.exit()
