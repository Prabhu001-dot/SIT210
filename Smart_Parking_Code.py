#Libraries
import RPi.GPIO as GPIO
import time
import requests
#Disable warnings (optional)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



buzzer=23
trigger=15
echo=14
led=4
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(trigger,0)



GPIO.output(buzzer,GPIO.LOW)
def distCalc():
    GPIO.output(trigger,1)
    time.sleep(0.0001)
    GPIO.output(trigger,0)
    while GPIO.input(echo)==0:
        pass
    start=time.time()
    while GPIO.input(echo)==1:
        pass
    end=time.time()
    
    dist=(end-start)*17000
    return dist
GPIO.output(led,GPIO.LOW)
def buzz(times):
    GPIO.output(buzzer,GPIO.HIGH)
    
    time.sleep(times) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    
    time.sleep(times)
while True:
    
    dist=distCalc()
    print(dist)
    
    if dist < 4.0:
               
        buzz(0.1)
        
        
    elif dist>4.5 and dist < 7:
        buzz(0.5)
    
    
    elif dist >  10:
        
        #print("TOO far")
        GPIO.output(led,GPIO.HIGH)
    if dist > 14:
        GPIO.output(led,GPIO.HIGH)
    else:
        GPIO.output(led,GPIO.LOW)
    if dist > 14:
        r = requests.post('https://maker.ifttt.com/trigger/slot_empty/with/key/y5w11eCfT0Ff9uepS5Ev', params={"value1":"none","value2":"none","value3":"none"})
    else:
        r = requests.post('https://maker.ifttt.com/trigger/slot_full/with/key/y5w11eCfT0Ff9uepS5Ev', params={"value1":"none","value2":"none","value3":"none"})
GPIO.output(buzzer, GPIO.LOW)
GPIO.cleanup()
'''   
#Select GPIO mode

#Set buzzer - pin 23 as output
buzzer=3
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
while True:
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    sleep(1) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beep")
    sleep(1)
    '''