import random
from Modules import rand_items

password = ""
word_count = 0
word_limit = random.randint(7, 20)

while word_count <= word_limit:
    character = random.choice(str([rand_items.letters, rand_items.numbers, rand_items.symbols]))
    if character != " ":
        password += character
        word_count += 1

print(f"Your randomly generated password is: {password}")
