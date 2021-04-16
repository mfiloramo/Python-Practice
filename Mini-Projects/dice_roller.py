import random
from Modules import gen_answers

while True:
    play = input("Would you like to roll the dice? ")
    if play in gen_answers.yes_possibilities:
        print(random.randint(1, 6), (random.randint(1, 6)))
    elif play in gen_answers.no_possibilities:
        print("\nThanks for playing!")
        exit()
    else:
        print("Invalid response. Please try again.")
