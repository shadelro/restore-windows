import sys
import time
from Quartz.CoreGraphics import *       # imports all of the top-level symbols in the module

def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)
def move(posx,posy):
    mouseEvent(kCGEventMouseMoved, posx,posy);
def down(posx,posy):
    mouseEvent(kCGEventLeftMouseDown, posx,posy);
def up(posx,posy):
    mouseEvent(kCGEventLeftMouseUp, posx,posy);
def drag(posx,posy):
    mouseEvent(kCGEventLeftMouseDragged, posx,posy);
def click(posx,posy):
    down(posx, posy)
    up(posx, posy)

if __name__ == "__main__":
    command = sys.argv[1]
    if command == 'click_high':
        click(950, 5)
    elif command == 'down':
        down(750, 30)
    elif command == 'up':
        up(750, 30)
    else:
        print 'Unrecognized command.'
    sys.exit()
