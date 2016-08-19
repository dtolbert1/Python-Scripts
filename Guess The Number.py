#Guess the number game
import random

#Set up the secret number that the user will try to guess.
secret_number = random.randrange(1,10,1)

#Setting up a variable to keep the while loop going.
active = True

#The while loop continuously checks the user's guess to see if it matches the secret number.
#Once it matches the secret number, the loop exits and the program is complete.
while active:
    guess = input("Guess a number to 1-10 to win the game!: ")
    if guess == str(secret_number):
            print("You guessed correctly! Good job!")
            break
    elif guess < str(secret_number):
            print("Your number is too low, try again.")
    elif guess > str(secret_number):
            print("Your number is too high, try again.")
