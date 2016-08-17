#Magic 8 Ball
import random

input("What is the question that you'd like to ask the magic 8 ball? ")

def magic_8_ball(number):
    if number == 1:
        print("It is certain.")
    elif number == 2:
        print("It is decidely so.")
    elif number == 3:
        print("Without a doubt.")
    elif number == 4:
        print("Yes, definitely.")
    elif number == 5:
        print("Yes, you may rely on it.")
    elif number == 6:
        print("As I see it, yes.")
    elif number == 7:
        print("Most Likely")
    elif number == 8:
        print("Outlook good.")
    elif number == 9:
        print("Yes.")
    elif number == 10:
        print("Signs point to yes.")
    elif number == 11:
        print("Ask again later.")
    elif number == 12:
        print("Cannot predict now.")
    elif number == 13:
        print("Concentrate and ask again")
    elif number == 14:
        print("Don't count on it.")
    elif number == 15:
        print("My reply is no.")
    elif number == 16:
        print("My sources say no.")
    elif number == 17:
        print("Very doubtful.")

shake = random.randint(1,17)

magic_8_ball(shake)
