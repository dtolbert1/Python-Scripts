import random

active = True

while active:
    random_number = random.randrange(0, 6, 1)

    response = input("Would you like to roll the dice? (y or n) ")

    if response == 'n':
        active = False
    else:
        print(random_number)




