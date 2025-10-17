# micro:uno Radio USER MANUAL

# Starting Play
# After Pressing A/B to Host/Join a Game,
# Use A/B to enter a PASSWORD.
# A increments the current row
# while B goes to the next one down
# if you Join a game, you must put in the same PASSWORD as
# the host
# (Turn order is in the Join order)

# Game 
# Screen:    Key:
# CCNNT       C  - Top Pile Card Color
# CCNNT       N  - Top Pile Card Number
# ccnnT      c&n - same but for selected hand card
# ccnnT       T  - Turn Order
# HHHHH       H  - Hand





# Imports go at the top
from microbit import *
import radio

state = 0
statefuncts = dict()

def inpPass():
    passW = 0
    digits = 0
    currentDigit = 0
    while digits<5:
        for i in range(5):
            if i < currentDigit:
                display.set_pixel(i,digits,9)
            else: 
                display.set_pixel(i,digits,0)
        if button_a.was_pressed():
            currentDigit=(currentDigit+1)%6
        elif button_b.was_pressed():
            digits+=1
            passW*=10
            passW+=currentDigit
            print(passW)
            currentDigit=0
        sleep(10)
    return passW
def changeState(x):
    global state
    global statefuncts
    def pas():
        pass
    func = statefuncts.get(x,pas)
    func()
    state = x
def assignStateFunction(x,func):
    global statefuncts
    statefuncts.update({x:func})

def scrollLoopStateFunc(str):
    def returnFunc():
        display.scroll(str,wait=False,loop=True)
    return returnFunc
def clearscroll():
    display.scroll("")
    
assignStateFunction(0,scrollLoopStateFunc("A-HOST B-JOIN "))
assignStateFunction(1,clearscroll)
assignStateFunction(2,clearscroll)
assignStateFunction(3,scrollLoopStateFunc("Connecting..."))

#bytes are: [who, who, what, with]
radio.config(length=4,queue=15)
orb = 10

radio.on()
display.scroll("UNO",wait=True,delay=150)
sleep(100)
changeState(0)
# Code in a 'while True:' loop repeats forever
while True:
    if state==0:
        if button_a.was_pressed():
            changeState(1)
        elif button_b.was_pressed():
            changeState(2)
    elif state==1:
        passw = inpPass()
        passb: bytearray = bytearray(passw.to_bytes(2,"big"))
        passb.append(0b01)
        passb.append(0b0)
        print(passb)
        radio.send_bytes(passb)
    elif state==2:
        pass
    sleep(10)
        
    
