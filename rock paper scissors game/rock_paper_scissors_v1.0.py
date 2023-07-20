# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:46:08 2023

@author: James
"""

# Rock, Paper, Scissors game v1.0

import random
from art import *

# print text in ascii style.

tprint("Let's play!")

print('Welcome to Rock, Paper, Scissors. \nRock beats scissors, scissors beat paper, and paper beats rock.\n')

# initiate scores.

player_score = 0
computer_score = 0

# game loop.

while True:
    
    # player selection.

    player = input("Let's play! Pick rock, paper, scissors or exit.\n")
    player = player.lower() # accounts for input case.
    
    # exit breaks the loop.

    if player == 'exit':
        if player_score > computer_score:
            print('Thanks for playing. You won!')
        elif player_score < computer_score:
            print('Thanks for playing. You lost!')
        else: print("Thanks for playing. It's a tie!")
        break

    # assign random selection to computer.

    computer = ""
    rand = random.randint(1,3)
    if rand == 1:
        computer = 'rock'
    elif rand == 2:
        computer = 'paper'
    elif rand == 3:
        computer = 'scissors'

    print("Computer has picked " + computer + ".")
    
    # calculate and print the result.

    result = ""
    
    if player == computer:
        result = "It's a tie!"
    elif player == 'rock' and computer == 'paper':
        result = 'You lose!'
        computer_score +=1
    elif player == 'rock' and computer == 'scissors':
        result = 'You win!'
        player_score +=1
    elif player == 'paper' and computer == 'rock':
        result = 'You win!'
        player_score +=1
    elif player == 'paper' and computer == 'scissors':
        result = 'You lose!'
        computer_score +=1
    elif player == 'scissors' and computer == 'rock':
        result = 'You lose!'
        computer_score +=1
    elif player == 'scissors' and computer == 'paper':
        result = 'You win!'
        player_score +=1
    else: print('Player input is not valid. Please try again.')

    print(result)
    
    # print current scores.
    
    print('Your score is ' + str(player_score))
    print('Computer score is ' + str(computer_score))
    
    if player_score > computer_score:
        print("You're winning!\n")
    elif player_score < computer_score:
        print("You're losing!\n")
    else: print("It's neck and neck!\n")