import RPi.GPIO as GPIO
import time
from random import randrange

GPIO.output(22, True)



def blink():
    GPIO.output(22, False)
    print "blink"
    time.sleep(1)
    GPIO.output(22, True)



while(1):
 t = randrange(5)
 time.sleep(t)
 blink()
 
 