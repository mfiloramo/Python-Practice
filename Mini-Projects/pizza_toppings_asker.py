#  In this program, I play with several basic list methods, .append() and .clear().
#  Notice how I make them modify the pizza_toppings list dynamically as the user
#  interacts with the program.

from Modules import gen_answers

ask_count = 0
pizza_toppings = []

while ask_count <= 5:
    pizza_toppings.append(input("What kind of pizza topping would you like? "))
    ask_count += 1
    if ask_count == 5:
        print(f"Your pizza will include {pizza_toppings}.")
    while ask_count == 5:
        ask = input("Would you like to play again? ")
        if ask in gen_answers.yes_possibilities:
            ask_count = 0
            pizza_toppings.clear()
        elif ask in gen_answers.no_possibilities:
            print("Thanks for playing.")
            exit()
        else:
            print("Invalid response.\n")
