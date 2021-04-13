#Raspberry-Pi pan and tilt using arrow keys script
# This code references the source https://github.com/nguyenrobot/palt-tilt-cam
# Modified by Ninh Tran.

#must be run from Pi's terminal!

import curses
import os
import time
import picamera
import serial

# Up        key : droid moves forward
# DOWN      key : droid moves backward
# LEFT      key : droid turns left
# RIGHT     key : droid turns right
# j         key : camera go up
# n         key : camera go down
# b         key : camera rotate left
# m         key : camera rotate right
# s         key : stop the droid
 
# Must connect Raspberry-Pi(USB) and Ardunio(USB) 
port = serial.Serial("/dev/ttyACM0", baudrate=9600)

#!/usr/bin/python
import RPi.GPIO as GPIO
from PCA9685 import PCA9685


# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

#setting start up serrvo positions

pwm = PCA9685()
pwm.setPWMFreq(50)

max_PAN      = 180
max_TILT     = 180
min_PAN      = 10
min_TILT     = 10
    
step_PAN     = 2
step_TILT    = 2
current_PAN  = 90
current_TILT = 90
pwm.setRotationAngle(0, current_PAN) #PAN    
pwm.setRotationAngle(1, current_TILT) #TILT

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            #if q is pressed quit
            break
            
        elif char == ord('m'):
            screen.addstr(0, 0, 'right ')
            current_PAN = max(min_PAN, current_PAN - step_PAN)
            pwm.setRotationAngle(0, current_PAN) #PAN 
            time.sleep(0.001)
            
        elif char == ord('b'):
            screen.addstr(0, 0, 'left ')
            current_PAN = min(max_PAN, current_PAN + step_PAN)
            pwm.setRotationAngle(0, current_PAN) #PAN 
            time.sleep(0.001)
            
        elif char == ord('j'):
            screen.addstr(0, 0, 'up ')
            current_TILT = max(min_TILT, current_TILT - step_TILT)
            pwm.setRotationAngle(1, current_TILT) #TILT 
            time.sleep(0.001)
            
        elif char == ord('n'):
            screen.addstr(0, 0, 'down ')
            current_TILT = min(max_TILT, current_TILT + step_TILT)
            pwm.setRotationAngle(1, current_TILT) #TILT 
            time.sleep(0.001)
            
        elif char == ord('s'):
            #if s is pressed stop the droid!
            screen.addstr(0, 0, 's')    
            port.write('s'.encode());       
            
        elif char == curses.KEY_RIGHT: 
            screen.addstr(0, 0, chr(char))         
            port.write('i'.encode());            
            
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, chr(char)) 
            port.write('l'.encode());

        elif char == curses.KEY_UP:
            screen.addstr(0, 0, chr(char)) 
            port.write('f'.encode());
            
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, chr(char)) 
            port.write('b'.encode());   
        
        elif ( (char == ord('0')) or (char == ord('1')) or (char == ord('2')) or (char == ord('3')) \
               or (char == ord('4')) or (char == ord('5')) or (char == ord('6')) or (char == ord('7')) \
               or (char == ord('8')) or (char == ord('9')) or (char == ord('*')) or (char == ord('#')) \
         ):
            screen.addstr(0, 0, chr(char)) 
            port.write('b'.encode());  


finally:
    # shut down cleanly
    pwm.exit_PCA9685()
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()