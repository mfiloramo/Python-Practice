import random

random_words = ["Tomato", "Mildew", "Jesus", "Are", "For", "And", "Regard", "Jump",
                "Rendezvous", "Black", "Disregard", "Because", "The", "Spam", "It",
                "Arrive", "With", "Nor", "Or", "Special", "Thin", "Ketchup", "Plenty",
                "Snap", "Santa", "Spear", "Really", "Molten"]

word_count = 0

while word_count < 100:
    print(random.choice(random_words))
    word_count += 1
