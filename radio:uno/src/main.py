# radio:uno USER MANUAL

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
import my_radio

# Code in a 'while True:' loop repeats forever
while True:
    sleep(100)
    my_radio.consumeMessages()
