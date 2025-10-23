# Imports
from microbit import *
import random

# Global Variables
player_score = 0
cpu_score = 0
turn = True
player_state = "safe"
stand_streak = 0

# 1 is player, 2 is cpu

# Actions
def take_action(action):
    global turn, cpu_score, player_score, stand_streak

    if turn == True:
        display.show("P")
    elif turn == False:
        display.show("C")
    sleep(1500)
    display.clear()
    
    if action == "hit":
        stand_streak = 0
        if turn == True:
            player_score += random.randint(2, 11)
            update_screen()
            print("Turn 1: Hit")
            turn = False
        elif turn == False:
            cpu_score += random.randint(2, 11)
            update_screen()
            print("Turn 2: Hit")
            turn = True
        sleep(1000)
        
    if action == "stand":
        stand_streak += 1
        if turn == True:
            print("Turn 1: Stand")
            turn = False
        elif turn == False:
            print("Turn 2: Stand")
            turn = True
        
def turn_manager():
    global turn, cpu_score
    
    # Player actions.
    if turn == True:
        if button_a.was_pressed():
            take_action("hit")
        if button_b.was_pressed():
            take_action("stand")
    elif turn == False: #CPU actions.
        sleep(1000)
        if cpu_score <= 20:
            take_action("hit")
        if cpu_score >= 21:
            take_action("stand")

def update_screen():
    global turn, player_score

    if player_score > 25:
        display.show(Image.SAD)
    else:
        for i in range(player_score):
            display.set_pixel(i%5,i//5,9)

while True:
    turn_manager()
