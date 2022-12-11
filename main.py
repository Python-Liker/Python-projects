#Import libraries
import random
import time


#Introduction
print("Press enter to roll the dice")
input()

#Rolling the dice
print("Rolling the dice")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)

#Printing the number on the dice
n = random.randint(1,6)
print(f"You rolled {n}")