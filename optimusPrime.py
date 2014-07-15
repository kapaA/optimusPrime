import RPi.GPIO as GPIO
import time
import thread
from random import randint

eye_color = 'BLUE'

def gpio_initializing():
    GPIO.setmode(GPIO.BOARD)

def face_initializing():
    #GPIO connection for mouth
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    #GPIO connection for Eyes
    GPIO.setup(16, GPIO.OUT) # RED
    GPIO.setup(18, GPIO.OUT) # GREEN
    GPIO.setup(22, GPIO.OUT) # BLUE
    
    #Turn On blue eye
    set_eye_color(eye_color)
   
def set_eye_color(eye):
    if ('RED' == eye):
        GPIO.output(16, True) # RED
        GPIO.output(18, False) # GREEN
        GPIO.output(22, False) # BLUE
    elif('GREEN' == eye):
        GPIO.output(16, False) # RED
        GPIO.output(18, True) # GREEN
        GPIO.output(22, False) # BLUE
    elif('BLUE' == eye):
        GPIO.output(16, False) # RED
        GPIO.output(18, False) # GREEN
        GPIO.output(22, True) # BLUE

def blink():
    while(1):
        t = randint(2,5)
        time.sleep(t)
        GPIO.output(16, False) # RED
        GPIO.output(18, False) # GREEN
        GPIO.output(22, False) # BLUE
        time.sleep(1)
        set_eye_color(eye_color)
        
        print "blink"
        
def main():
    #initialization phase
    gpio_initializing()
    face_initializing()
    try:
        thread.start_new_thread( blink() ) 
    except:
        print "Error: unable to start thread"



if __name__ == "__main__":
    main()