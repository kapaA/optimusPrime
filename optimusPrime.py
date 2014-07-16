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
        t = randint(3,15)
        time.sleep(t)
        GPIO.output(16, False) # RED
        GPIO.output(18, False) # GREEN
        GPIO.output(22, False) # BLUE
        t = randint(10,100)
        t=t/100.0
        time.sleep(t)
        set_eye_color(eye_color)
    
def moveMouth():
    
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    
    time.sleep(0.2)
    
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    GPIO.output(12, False)
    
    time.sleep(0.2)
    
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, True)
    GPIO.output(12, False)
    
    time.sleep(0.2)
    
    GPIO.output(7, True)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, True)
    GPIO.output(12, True)

    time.sleep(0.2)    
    
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)


        
def main():
    #initialization phase
    gpio_initializing()
    face_initializing()
    try:
        thread.start_new_thread( blink() ) 
    except:
        print "Error: unable to start thread"

    moveMouth()
    moveMouth()
    moveMouth()
    moveMouth()

if __name__ == "__main__":
    main()