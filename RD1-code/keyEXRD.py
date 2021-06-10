#Raspberry-Pi pan and tilt using arrow keys script
# This code references the source https://github.com/nguyenrobot/palt-tilt-cam
# Modified by Ninh Tran.

#must be run from Pi's terminal!
# Up        key : droid moves forward
# DOWN      key : droid moves backward
# LEFT      key : droid turns left
# RIGHT     key : droid turns right
# j         key : camera go up
# n         key : camera go down
# b         key : camera rotate left
# m         key : camera rotate right
# s         key : stop the droid

#!/usr/bin/python
import curses
import os
import time
import picamera
import serial
import speech_recognition as sr
import time
from PCA9685 import PCA9685
from gtts import gTTS
from mpyg321.mpyg321 import MPyg321Player
import RPi.GPIO as GPIO
from io import BytesIO


player = MPyg321Player()
mp3_fp = BytesIO()
 
# Must connect Raspberry-Pi(USB) and Ardunio(USB) 
port = serial.Serial("/dev/ttyACM0", baudrate=9600)

LEFT  = ['turn left' , 'left' , 'left left']
RIGHT = ['turn right' , 'right' , 'right right','sunlight','turn bright','turn cry']
FORWARD  = ['go forward' ,'forward','go', 'forward forward' , 'go go', 'go go go']
BACKWARD = ['go back','back' ,'go backward', 'backward','back back']
STOP = ['stop', 'stop stop', 'wait']



# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

        


def text_to_command(text):
    if any(sub in text for sub in LEFT):        
        myobj = gTTS(text="Alright, I will turn left", lang='en', slow=False)
        myobj.save("audio.mp3")
        os.system("mpg321 audio.mp3 >/dev/null 2>&1")    
        return 'l'
    elif any(sub in text for sub in RIGHT):
        myobj = gTTS(text="Alright, I will turn right", lang='en', slow=False)
        myobj.save("audio.mp3")
        os.system("mpg321 audio.mp3 >/dev/null 2>&1")          
        return 'i'
    elif any(sub in text for sub in FORWARD):
        myobj = gTTS(text="Alright, I will move forward", lang='en', slow=False)
        myobj.save("audio.mp3")
        os.system("mpg321 audio.mp3 >/dev/null 2>&1")   
        return 'f'
    elif any(sub in text for sub in BACKWARD):
        myobj = gTTS(text="Alright, I will move backward", lang='en', slow=False)
        myobj.save("audio.mp3")
        os.system("mpg321 audio.mp3 >/dev/null 2>&1")   
        return 'b'    
    elif any(sub in text for sub in STOP):
        myobj = gTTS(text="Alright, I will stop here", lang='en', slow=False)
        myobj.save("audio.mp3")
        os.system("mpg321 audio.mp3 >/dev/null 2>&1")          
        return 's'   
    else:
        return 'No Command'



def speech_to_text():
    required = -1
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required= index
    r = sr.Recognizer()
    with sr.Microphone(device_index=required) as source:
        r.adjust_for_ambient_noise(source)        
        audio = r.listen(source, phrase_time_limit = 3)
    try:
        input = r.recognize_google(audio)         
        return text_to_command(input)        
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass



#setting start up serrvo positions
pwm = PCA9685()
pwm.setPWMFreq(50)

max_PAN      = 180
max_TILT     = 180
min_PAN      = 10
min_TILT     = 10
    
step_PAN     = 1
step_TILT    = 1
current_PAN  = 120
current_TILT = 120
pwm.setRotationAngle(0, current_PAN) #PAN    
pwm.setRotationAngle(1, current_TILT) #TILT


voice_command= "" 
try:
    while True:      
        char = screen.getch()
        if char == ord('q'):
           #if q is pressed quit
           break

        elif char == ord('t'):
           screen.addstr(0, 0, "Say somethings :  ")
           voice_command = speech_to_text()            
           if(voice_command):
               print(voice_command)
                    
            
        if char == ord('m'):
            screen.addstr(0, 0, 'right ')
            current_PAN = max(min_PAN, current_PAN - step_PAN)
            pwm.setRotationAngle(0, current_PAN) #PAN 

            
        elif char == ord('b'):
            screen.addstr(0, 0, 'left ')
            current_PAN = min(max_PAN, current_PAN + step_PAN)
            pwm.setRotationAngle(0, current_PAN) #PAN 

            
        elif char == ord('j'):
            screen.addstr(0, 0, 'up ')
            current_TILT = max(min_TILT, current_TILT - step_TILT)
            pwm.setRotationAngle(1, current_TILT) #TILT 

            
        elif char == ord('n'):
            screen.addstr(0, 0, 'down ')
            current_TILT = min(max_TILT, current_TILT + step_TILT)
            pwm.setRotationAngle(1, current_TILT) #TILT 
  
            
        elif char == ord('s') or  voice_command == 's':
            #if s is pressed stop the droid!
            screen.addstr(0, 0, 's')    
            port.write('s'.encode());       
            
        elif char == curses.KEY_RIGHT or voice_command == 'i': 
            screen.addstr(0, 0, chr(char))         
            port.write('i'.encode());            
            
        elif char == curses.KEY_LEFT or  voice_command == 'l':
            screen.addstr(0, 0, chr(char)) 
            port.write('l'.encode());

        elif char == curses.KEY_UP or  voice_command == 'f':
            screen.addstr(0, 0, chr(char)) 
            port.write('f'.encode());
            
        elif char == curses.KEY_DOWN or  voice_command == 'b':
            screen.addstr(0, 0, chr(char)) 
            port.write('b'.encode());         
        else:           
            screen.addstr(0, 0, "Nothing to do") 


finally:
    # shut down cleanly
    pwm.exit_PCA9685()
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()








