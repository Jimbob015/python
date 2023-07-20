# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:13:36 2023

@author: James
"""

# Number Guessing game v1.0

import random
from art import *

# print text in ascii style.

tprint("Let's play!")

print("Welcome to Number Guessing. \nI'll pick a random number between 1 - 20 and you'll have 5 attempts to guess the correct number. Good luck!\n")

# random number selection and define number of attempts.

choice = random.randint(1,20)
attempts_remaining = 5

# game loop.

while True:
    guess_str = input('Guess a number between 1 and 20.\n')
    attempts_remaining = attempts_remaining -1 # remove 1 attempt for each guess.
    
    # try statement to account for input errors.    
    
    try:
        guess = int(guess_str)
        
        # calculate and print the result.
    
        if guess == choice:
            print("That's correct! Well done.\n")
            break # break the loop if number is guessed.
        elif guess > choice:
            print("That's incorrect, the number is smaller than " + str(guess) + ".")
            print(str(attempts_remaining) + " attempts remaining.\n")
        elif guess < choice:
            print("That's incorrect, the number is bigger than " + str(guess) + ".")
            print(str(attempts_remaining) + " attempts remaining.\n")
        
        # break the loop if all attempts are used.
        
        if attempts_remaining == 0:
            print("All 5 attempts have been used. The number was " + str(choice) + ".")
            print("Thanks for playing!\n")
            break
    
    # except statement for invalid input.    
    
    except: 
        print("Input is invalid.")
        print(str(attempts_remaining) + " attempts remaining.\n")