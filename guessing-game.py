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

numberToGuess = np.random.randint(1,10) # low inclusive, high exclusive

roundNo = 0
userInput = 0

while str(userInput) != "exit" and int(userInput) != numberToGuess:

    userInput = input("Guess a number between 0-9 or type exit to finish: ")
    roundNo += 1
        
    sentenceEnding = " guess"
    if roundNo != 1:
        sentenceEnding = " guesses"
    
    if userInput == "exit":
        print("you exited the game")
    elif int(userInput) == numberToGuess:
        print("you win the game after " + str(roundNo) + sentenceEnding)
    elif int(userInput) > numberToGuess:
        print("Guess a smaller number!")
    elif int(userInput) < numberToGuess:
        print("Guess a higher number!")
    else:
        print("something went wrong and you exited the game after " + str(roundNo) + sentenceEnding)