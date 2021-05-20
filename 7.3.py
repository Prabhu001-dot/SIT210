import RPi.GPIO as GPIO


import time


###################################################################################################################################
GPIO.setmode(GPIO.BOARD)
trig =9

Echo =11

Led=14
###################################################           GPIO SETUP             ##################################################################
GPIO.setup(trig,GPIO.OUT)

GPIO.setup(Led,GPIO.OUT)

GPIO.setup(Echo,GPIO.IN)

GPIO.output(trig,0)
########################################################################################################################################################
time.sleep(0.1)

pwm=GPIO.PWM(Led,100)

ac=0

pwm.start(ac)

print("dist: ")
###############################################################################################################
def distanceMeasurement():

    GPIO.output(trig,1)

    time.sleep(0.00025)
    GPIO.output(trig,0)

    while GPIO.input(Echo)==0:
        pass
    start=time.time()

    while GPIO.input(Echo)==1:
        pass
    end=time.time()
    
    dist=(end-start)*17000
    return dist
###################################### main loop###################################################################################

check=True
while check:
    distance=distanceMeasurement()

    print(distance)
    
    
    if distance>50:
        GPIO.output(Led,GPIO.HIGH)
        pwm.ChangeDutyCycle(0)
    else:
        pwm.ChangeDutyCycle(100-(dist*2))
        GPIO.output(Led,GPIO.LOW)
