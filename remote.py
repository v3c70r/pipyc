import curses
import time
#init the curses screen
stdscr = curses.initscr()
stdscr.nodelay(1)
#use cbreak to not require a return key press
curses.cbreak()
print "press q to quit"
quit=False
# loop
previous_key = -1
while quit !=True:
    time.sleep(0.1)
    c = stdscr.getch()
    if c != -1:
        if curses.keyname(c) == "q":
            quit=True
        if c != previous_key:
            print "pressed"
    elif previous_key != c:
        print "released"
    previous_key = c
        
curses.endwin()
