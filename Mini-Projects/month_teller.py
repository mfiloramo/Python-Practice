monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

guess = ""
replay = ""
guess_count = 0
guess_limit = 5
asking_user = True

while asking_user:
    if guess_count < guess_limit:
        guess = input("What is the month you want to convert? ")
        print(monthConversions.get(guess, "Not a valid month.\n"))
        guess_count += 1
    else:
        replay = input("Would you like to play again? ")
        if replay == "yes" or replay == "Yes":
            print("\nGreat! Let's try again.\n")
            guess_count = 0
        elif replay == "no" or replay == "No":
            asking_user = False
        else:
            print("\nInvalid option!\n")

if not asking_user:
    print("\nThanks for playing!")
