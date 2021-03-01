# -*- coding: utf-8 -*-
"""
Generates a random number between 1 and 9 (including 1 and 9).
Asks the user to guess the number,
then tells them whether they guessed too low, too high, or exactly right.

Keeps the game going until the user types “exit”.
Keeps track of how many guesses the user has taken, and when the game ends, prints this out.

Created on 1.3.2021. @author: Barbora Doslikova
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
    elif int(userInput) > numberToGuess:
        userInput = input("Guess a smaller number or type exit to finish: ")
        roundNo += 1
    elif int(userInput) < numberToGuess:
        userInput = input("Guess a higher number or type exit to finish: ")
        roundNo += 1
    else:
        print("something went wrong and you exited the game after " + str(roundNo) + " rounds")
    
# for exiting the game
if userInput == "exit":
    print("you exited the game after " + str(roundNo) + " rounds")