#Import libraries
import random

#Setting the variables
i = 0

#Asking for user input
print("Welcome to the Rock Paper Scissors game")
while i < 1:
    player = str(input("Enter your choice(r;p;s): "))
    choices = ["rock", "paper", "scissors"]
    bot = random.choice(choices)

    #Seeing who won the game
    if player == "r":
        if bot == "rock":
            print("It is a draw! We both chose rock")
            i = i + 1
            break
        elif bot == "paper":
            print("I beated you! I chose paper")
            i = i + 1
            break
        elif bot == "scissors":
            print("You beated me! I chose scissors")
            i = i + 1
            break
    if player == "p":
        if bot == "rock":
            print("You beated me! I chose rock")
            i = i + 1
            break
        elif bot == "paper":
            print("It is a draw! We both chose paper")
            i = i + 1
            break
        elif bot == "scissors":
            print("I beated you! I chose scissors")
            i = i + 1
            break
    if player == "s":
        if bot == "rock":
            print("I beated you! I chose rock")
            i = i + 1
            break
        elif bot == "paper":
            print("You beated me! I chose paper")
            i = i + 1
            break
        elif bot == "scissors":
            print("It is a draw! We both chose scissors")
            i = i + 1
            break
    #Retrying if input is invalid
    else:
            print("Please chose a valid form")
