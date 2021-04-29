from tkinter import *
import tkinter.font
from gpiozero import LED

import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)


greenPin =LED(14)
yellowPin =LED(23)
redPin =LED(24)


win = Tk()
win.title("Making GUI LED")
varFont = tkinter.font.Font(family = 'Times New Roman', size = 16, weight = "bold")


# Event  #
def ledGrToggle():
    if greenPin.is_lit:
        greenPin.off()
        greenPinButton["text"]="Turn LED on"

    else:
        greenPin.on()
        yellowPin.off()
        redPin.off()
        greenButton["text"]="Turn LED off"
        
def ledYeToggle():        
    if yellowPin.is_lit:
        yellowPin.off()
        yellowButton["text"]="Turn LED on"

    else:
    
        yellowPin.on()
        greenPin.off()        
        redPin.off()
        yellowButton["text"]="Turn LED off"
        
def ledReToggle():  
    if redPin.is_lit:
        redPin.off()
        redButton["text"]="Turn LED on"

    else:
        redPin.on()
        greenPin.off()
        yellowPin.off()
        redButton["text"]="Turn LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()



ledgrButton = Button(win, text='Turn LED on', font=varFont, command=ledGrToggle, bg='green', height=2, width=28)
ledgrButton.grid(row=0,column=2)

ledyeButton = Button(win, text='Turn on LED', font=varFont, command=ledYeToggle, bg='yellow', height=2, width=28)
ledyeButton.grid(row=1,column=2)

ledreButton = Button(win, text='Turn on LED', font=varFont, command=ledReToggle, bg='red', height=2, width=28)
ledreButton.grid(row=3,column=2)

exitButton = Button(win, text='Exit', font=varFont, command=close, bg='brown', height=2, width=11)
exitButton.grid(row=5, column=2)

win.protocol("WM_DELETE_WINDOW", close)  

win.mainloop()