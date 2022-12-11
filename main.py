#Import libraries
import random

#Defining the lists and variables
caracters = 0
formated_pass = ""
password = []
Uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M" , "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Lowercase = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = ["0", "1", "2", "3", "4", "5","6", "7", "8", "9"]
Symbols = ["!", "#", "$", "%", "&"]
 
#Generating a random password
def random_password():
    x = 0
    for x in range(caracters):
        x = random.randint(1,4)
        if x == 1:
            password.append(random.choice(Lowercase))
            x += 1
            
        elif x == 2:
            password.append(random.choice(Numbers))
            x += 1
            
        elif x == 3:
            password.append(random.choice(Symbols))
            x += 1
            
        elif x == 4:
            password.append(random.choice(Uppercase))
            x += 1
            
            
#Taking the lenght of the password
caracters = int(input("How long will the password be? \n"))

#Generating the password
random_password()

#Making the result a string
for i in password:
    formated_pass = formated_pass + i

#Printing the result   
print(f"Your password is: {formated_pass}")
