import random

computer_guess = random.randint(1, 10)
score = 1000
guess_count = 0

play_game = True

while play_game and guess_count < 10:

    # This segment asks user for the number, and eventually drops a hint about the number.

    guess = int(input("What is the magic number? "))
    if guess_count == 4:
        if computer_guess > 5:
            print("\nThe number is greater than 5.\n")
        else:
            print("\nThe number is less than 5.\n")

    # This segment is for determining whether or not you win, and keeps track of your score/guess count.

    if guess == computer_guess:
        print("\nYou win! The computer's number was " + str(computer_guess) + ".")
        print("Your score is " + str(score) + ".")
        exit()
    else:
        score -= 50
        guess_count += 1

print("\nGuess limit reached.")
print("The computer's number was " + str(computer_guess) + ".")