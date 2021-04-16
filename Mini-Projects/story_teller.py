# Design a program that will write a short story using random conjunctions, nouns, verbs, adjectives,
# and sentence types. There needs to be a rough structure to the way that the program writes each sentence
# of the story. The program will write this story and store it in a text file. The program will also have various
# functions that allow it to manipulate the date. It will have a function that allows it to count the number of
# vowels, consonants, and words throughout the story.

import random
from Modules import rand_items_2

story_name = rand_items_2.r_name
story_name_2 = rand_items_2.r_name
story_noun = rand_items_2.r_noun

# Maybe build a function that executes this sentence generation?
word_count = 0
word_limit = random.randint(4, 12)
sentence = ""

# while word_count <= word_limit:
#     sentence += random.choice([random.choice(rand_items_2.conjunctions).lower(),
#                                random.choice(rand_items_2.r_noun)]).lower() + str(" ")

print(f"This story will be about {story_name} and their {rand_items_2.r_adj} {story_noun.lower()}.\n\n"
      f"Once upon a time, there lived a {rand_items_2.r_adj} {story_noun.lower()} named {story_name}. This person "
      f"was quite the {rand_items_2.r_noun.lower()}.")

# Sentence structure:
# I. First Chunk:
    # "This story will be about:"
        # name = [story_name]
        # "and their"
        # possession = [story_noun]
    # [introduction piece] <-- Such as "first", "to start", "at first", etc.
    # [indefinite article] <-- Such as "an", "a", "the".
        # Write a block of code that makes it so that if the subsequent word starts with a vowel, then the
        # indefinite article will be "an", otherwise "a", "the", etc.
    # [noun]
    # [verb] <-- Make sure to randomize the tense (past = +ed, present = "s", future puts the word "will" before it.
    # [story_name_1] felt [adjective].
    # "But," [story_name_2] = [name] "came in!."
    # [story_name_2] was [adjective].

# II. Second Chunk:
    # [transition word] <-- "then", "and then", "after that", "coincidentally", etc.
    # [story_name] + ['s]
    # [story_noun]
    # [rand_choice: is, was, will be, can be, would be, should be, is going to be, wasn't, won't be, can't be,
    # wouldn't be, probably would be, probably wouldn't be, shall be, shall not be]
    # [adjective]
    # [random sentence]

# III. Third Chunk:
    # [conjunction]
    # [indefinite article] <-- Such as "an", "a", "the".
        # Write a block of code that makes it so that if the subsequent word starts with a vowel, then the
        # indefinite article will be "an", otherwise "a", "the", etc.
    # [noun]
    # [verb] <-- Make sure to randomize the tense (past = +ed, prsent = "s", future puts the word "will" before it.
    # [but], or some word that indicates contrast.
    # [random sentence]
    # "It was" + [adjective]

# IV. Fourth Chunk:
    # [conjunction]
    # [transition word] <-- "then", "and then", "after that", "coincidentally", etc.
    # [story_name] + 's
    # [story_noun]
    # [verb] + ed
    # [story_name_2] + 's was [adjective].
    # [random sentence]

# Cycle II, III, IV.
# Don't forget embedding proper punctuation. Make sure that all punctuation is random.
# The [random_sentence] choices are sentences that you create yourself.