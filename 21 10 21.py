import random
import math
randomChoice = random.randint(1, 1000)
minNumberGuesses = round(math.log(1000 - 1 + 1, 2))
guessCount = 0
while guessCount <= minNumberGuesses:
    answer = int(input("I'm thinking of a number between 1 and 1000 good luck guessing it lol"))
    if answer == randomChoice:
        guessCount = minNumberGuesses+1
    else:
        print("nah")
    guessCount = guessCount+1
if answer == randomChoice:
    print("what the heck how")
else:
    print("haha skill issue")