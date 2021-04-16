is_male = input("Are you a male? ")
is_tall = input("Are you tall? ")
is_stupid = input("Are you stupid? ")

if is_male == "Yes" or is_male == "yes":
    is_male = True
elif is_male == "No" or is_male == "no":
    is_male = False
else:
    is_male = False

if is_tall == "Yes" or is_tall == "yes":
    is_tall = True
elif is_tall == "No" or is_tall == "no":
    is_tall = False
else:
    is_tall = False

if is_stupid == "Yes" or is_stupid == "yes":
    is_stupid = True
elif is_stupid == "No" or is_stupid == "no":
    is_stupid = False
else:
    is_stupid = False

if is_male and is_tall and is_stupid:
    print("You are a tall, male dumbass.")
elif is_male and is_tall and not(is_stupid):
    print("You are a tall, male genius.")
elif is_male and not(is_tall) and is_stupid:
    print("You are a short, male dumbass.")
elif is_male and not(is_tall) and not(is_stupid):
    print("You are a short, male genius.")
elif not(is_male) and (is_tall) and (is_stupid):
    print("You are a tall, dumb woman.")
elif not(is_male) and not(is_tall) and (is_stupid):
    print("You are a short, dumb woman.")
elif not(is_male) and (is_tall) and not(is_stupid):
    print("You are a tall, smart woman.")
elif not(is_male) and not(is_tall) and not(is_stupid):
    print("You are a short, smart woman.")
else:
    print("I don't fuckin' know what you are.")