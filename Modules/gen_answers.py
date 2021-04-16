#  This module handles user input for generic yes/no input questions.

def confirm(query):
    while True:
        answer = input(query)
        if answer in yes_possibilities:
            return True
        elif answer in no_possibilities:
            return False
        elif answer.isnumeric():
            print("I am a number. Please try again.")
        else:
            print("Invalid response. Please try again.")


yes_possibilities = ["Yes", "yes", "Y", "y", "yeah", "hell yeah",
                     "fuck yeah", "sure", "yeah sure", "okay"]
no_possibilities = ["No", "no", "N", "n", "nah", "nope", "fuck no",
                    "nein"]