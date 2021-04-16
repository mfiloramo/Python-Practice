import random

choices = ("Rock", "Paper", "Scissors")

play_game = True
play_game_count = 0


while play_game == True:

    # This segment gives user the option of replaying or ending the game after a set number of tries.

    while play_game_count >= 5:
        replay = input("Would you like to play again? ")
        if replay == "No" or replay == "no":
            play_game = False
            print("Thanks for playing!")
            exit()
        elif replay == "Yes" or replay == "yes":
            play_game_count = 0
            print("")
        else:
            print("Invalid option!\n")

    # This segment is for the user shooting "rock."

    user_guess = input("Rock, paper, scissors and SHOOT! ")
    computer_guess = random.choice(choices)
    if (user_guess == "Rock" or user_guess == "rock") and computer_guess == "Scissors":
        print("You win!")
        print("Computer's guess was " + computer_guess + "\n")
        play_game_count += 1
    elif (user_guess == "Rock" or user_guess == "rock") and computer_guess == "Rock":
        print("Draw!")
        print("Computer's guess was " + computer_guess + "\n")
        play_game_count += 1

    # This segment is for the user shooting "paper."

    elif (user_guess == "Paper" or user_guess == "paper") and computer_guess == "Rock":
        print("You win!")
        print("Computer's guess was " + computer_guess + "\n")
        play_game_count += 1
    elif (user_guess == "Paper" or user_guess == "paper") and computer_guess == "Paper":
        print("Draw!")
        print("Computer's guess was " + computer_guess + "\n")
        play_game_count += 1

    # This segment is for the user shooting "scissors."

    elif (user_guess == "Scissors" or user_guess == "scissors") and computer_guess == "Paper":
        print("You win!")
        print("Computer's guess was " + computer_guess + "\n")
        play_game_count += 1
    elif (user_guess == "Scissors" or user_guess == "scissors") and computer_guess == "Scissors":
        print("Draw!")
        print("Computer's guess was " + computer_guess + "\n")
        play_game_count += 1
    else:
        print("You lose!")
        print("Computer's guess was " + computer_guess + "\n")
        play_game_count += 1

