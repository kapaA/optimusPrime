import RPi.GPIO as GPIO


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
    set_eye_color('BLUE')
   
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

def main():

    # initialization phase
    gpio_initializing()
    face_initializing()



















if __name__ == "__main__":
    main()