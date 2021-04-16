import random
from Modules import gen_answers

computer_guess = random.randint(1, 20)
player_guesses = 0
score = 1000

yes = gen_answers.yes_possibilities
no = gen_answers.no_possibilities

#  This program takes a slightly different and more complicated approach to building
#  a number guessing game. I use the notequal variables to create conditions for additional turns.
#  I also use different score- and player_guess resetting.

while player_guesses < 10:
    # replay_ask = True
    guess = int(input("What is the computer's number? "))  # ValueError crashes the program. How to prevent?
    if guess != computer_guess:
        print("Incorrect guess. Please try again.\n")
        score -= 50
        player_guesses += 1
        print(f"You have {10 - player_guesses} guesses left!")
        if player_guesses == 5 and computer_guess <= 10:
            print("Hint: The computer's number is 10 or lower.\n")
        if player_guesses == 5 and computer_guess > 10:
            print("Hint: The computer's number is 11 or higher.\n")

#  I tried to practically use an f-string. It works, but I don't really see a stylistic advantage
#  to it. I may end up sticking with regular strings with the str() function for when I need to keep
#  the entire string unified.

    if guess == computer_guess:
        print(f"Correct guess. The computer's number was: {computer_guess}\n")
        print("Your score was: " + str(score) + "\n")

# These lines were rearranged because this segment was before the if replay == "no" line,
# thus allowing the program to move back to the beginning of the program without telling
# the user "Invalid option."

        while player_guesses > 0 and True:
            replay = input("Would you like to play again? ")
            if replay in yes:
                player_guesses = 0
                score = 1000
                computer_guess = random.randint(1, 20)
                break
            if replay in no:
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid option. Please try again.\n")


print("Game over!")
print(f"The computer's number was: {computer_guess}")
