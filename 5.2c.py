from tkinter import *
import tkinter.font
from gpiozero import LED

import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)


green =LED(14)
yellow =LED(23)
red =LED(24)


win = Tk()
win.title("GUI LED TOGGLER")
myFont = tkinter.font.Font(family = 'Arial', size = 16, weight = "bold")


# Event  #
def greenToggle():
    if green.is_lit:
        green.off()
        greenButton["text"]="Turn LED on"

    else:
        green.on()
        yellow.off()
        red.off()
        greenButton["text"]="Turn LED off"
        
def yellowToggle():        
    if yellow.is_lit:
        yellow.off()
        yellowButton["text"]="Turn LED on"

    else:
    
        yellow.on()
        green.off()        
        red.off()
        yellowButton["text"]="Turn LED off"
        
def redToggle():  
    if red.is_lit:
        redn.off()
        redButton["text"]="Turn LED on"

    else:
        red.on()
        green.off()
        yellow.off()
        redButton["text"]="Turn LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()



greenButton = Button(win, text='Turn LED on', font=varFont, command=greenToggle, bg='green', height=2, width=28)
greenButton.grid(row=0,column=2)

yellowButton = Button(win, text='Turn on LED', font=varFont, command=yellowToggle, bg='yellow', height=2, width=28)
yellowButton.grid(row=1,column=2)

redButton = Button(win, text='Turn on LED', font=varFont, command=redToggle, bg='red', height=2, width=28)
redButton.grid(row=3,column=2)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='brown', height=2, width=11)
exitButton.grid(row=5, column=2)

win.protocol("WM_DELETE_WINDOW", close)  

win.mainloop()
