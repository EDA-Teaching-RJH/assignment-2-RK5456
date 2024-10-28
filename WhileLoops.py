### Part Two -- your code goes here. 

import random


correctguess = random.randint(1,100)

# now I will use a while loop until guess is correct

while True:
    guessnum = int(input("Guess the number from 1-100 "))

    if guessnum < correctguess:
        print("Number is less than the correct number. Try again")
    elif guessnum > correctguess:
        print("Number is higher than the correct number. Try again")
    else:
        print("You guessed the correct number")
        break