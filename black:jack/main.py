# Imports
from microbit import *
import random

# Global Variables
player_score = 0
cpu_score = 0
turn = 1

# 1 is player, 2 is cpu

# Actions
def take_action(action):
    global turn, cpu_score, player_score

    if action == "hit":
        if turn == 1:
            player_score = player_score + random.randint(1, 11)
            print("Turn 1: Hit")
            turn = 2
        elif turn == 2:
            cpu_score = cpu_score + random.randint(1, 11)
            print("Turn 2: Hit")
            turn = 1

    if action == "stand":
        if turn == 1:
            print("Turn 1: Stand")
            turn = 2
        elif turn == 2:
            print("Turn 2: Stand")
            turn = 1
        

def turn_manager():
    global turn, cpu_score
    
    # Player actions.
    if turn == 1:
        if button_a.was_pressed():
            take_action("hit")
        if button_b.was_pressed():
            take_action("stand")

    # CPU actions.
    if turn == 2:
        sleep(1000)
        if cpu_score <= 16:
            take_action("hit")
        if cpu_score >= 17:
            take_action("stand")


def update_screen():
    global turn, player_score

    for i in range(player_score):
        pass
        
while True:
    turn_manager()
    update_screen()
