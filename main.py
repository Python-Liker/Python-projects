#Import libraries
import random

#Printing introduction
print("Hi welcome to number guessing.")
print("Choose a number between 1 and 100")
print("Press enter to start")
input()

#Creating the game
found = False
n = random.randint(1, 100)
guesses = 0

while found == False:
    guess = int(input("Type your guess: "))

    if guess < n and guess >= 1:
        print("Your guess is lower than the number")
    elif guess > n and guess <= 100:
        print("Your guess is greater than the number")
    elif guess == n:
        print("You guessed the number correctly")
        print(f"It took you {guesses} guesses")
        break
    elif guess > 100 or guess < 1:
        print("Please enter a valid number")
