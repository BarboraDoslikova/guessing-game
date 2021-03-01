# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

Created on Mon Mar  1 17:19:02 2021. @author: Barbora Doslikova
"""
import numpy as np

# generate a number to be guessed
numberToGuess = np.random.randint(1,10)
print("to guess: ", numberToGuess)

# keep track of the round and the guess
roundNo = 1

# get user input for the first round
userInput = input("Guess a number between 0-9 or type exit to finish: ")
print("round: ", roundNo, ", guessed: ", userInput)

# get user input for the other rounds
while userInput != "exit":    
    if int(userInput) == numberToGuess:
        print("you win the game after " + str(roundNo) + " rounds")
        break
    else:
        userInput = input("Guess again or write exit: ")
        roundNo += 1
    
# for exiting the game
if userInput == "exit":
    print("exited the game after " + str(roundNo) + " rounds")