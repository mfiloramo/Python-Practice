from Modules import gen_answers

#  dog_file_name = "C:\\Users\\Filoramo\\Desktop\\dog_file.txt"
#  The above line is for accessing files externally.

dog_file = open("../Practice/Scrap Text Files/dog_file.txt", "r")
user_input = input("Would you like to open dog_file? ")
yes = gen_answers.yes_possibilities
no = gen_answers.no_possibilities

#  Notice the assignment of variables for the use of the answer possibilities
#  within the module generic_answers. This cleans up the code a bit and makes
#  notation simpler.

if user_input != "yes" and user_input != "Yes":
    print("Have a nice day!")
    dog_file.close()
    exit()

# This is the initial user input, then asking the user to count lines.

if dog_file:
    lines_count_ask = input("Would you like me to count the lines in this document? ")
    if lines_count_ask in yes:
       number_of_lines = len(dog_file.readlines())
       print(f"The total number of lines in this document is {number_of_lines}.\n")

    # This is the document vowel count of the program.
    # NOTE: You have to open the file in every instance within a loop.

    vowel_count = input("Would you like me to count the vowels in this document? ")
    if vowel_count in yes:
        dog_file = open("../Practice/Scrap Text Files/dog_file.txt", "r")
        string = dog_file.read()
        vowel_count = 0
        vowels = "AaEeIiOoUu"
        for vowels in vowels:
            for file_vowels in string:
                if vowels == file_vowels:
                    vowel_count += 1
        print(f"The total number of vowels in this document is {vowel_count}.\n")

#        for vowels in string:
#            if (vowels == 'A' or vowels == 'a' or vowels == 'E' or vowels == 'e' or vowels == 'I'
#                    or vowels == 'i' or vowels == 'O' or vowels == 'o'
#                    or vowels == 'U' or vowels == 'u'):


# This is the document consonant count of the program.
    # Originally, I wrote this segment to compare whether or not each iteration of the file reading
    # was individually equal to every single consonant, both lowercase and uppercase. It was an
    # unnecessarily large chunk of code. Now, however, I've condensed it down to a few lines, telling
    # the program to iterate through each consonant in a consonants list for every time it iterates
    # through a character in the dog_file.
    # NOTE: You have to open the file in every instance within a loop. See below; compare to highlighted:

#    for consonants in string:
#        if (consonants == 'Q' or consonants == 'W' or consonants == 'R' or consonants == 'T' or consonants == 'P'
#                or consonants == 'S' or consonants == 'D' or consonants == 'F'
#                or consonants == 'G' or consonants == 'H' or consonants == 'J'
#                or consonants == 'K' or consonants == 'Z' or consonants == 'X'
#                or consonants == 'C' or consonants == 'V' or consonants == 'B'
#                or consonants == 'N' or consonants == 'M' or consonants == 'q'
#                or consonants == 'w' or consonants == 'r' or consonants == 't'
#                or consonants == 'y' or consonants == 'Y' or consonants == 's'
#                or consonants == 'd' or consonants == 'f' or consonants == 'g'
#                or consonants == 'h' or consonants == 'j' or consonants == 'k'
#                or consonants == 'l' or consonants == 'z' or consonants == 'x'
#                or consonants == 'c' or consonants == 'v' or consonants == 'b'
#                or consonants == 'n' or consonants == 'm'):
#            consonant_count += 1

    consonants_count = input("Would you like me to count the consonants in this document? ")
    if consonants_count in yes:
        dog_file = open("../Practice/Scrap Text Files/dog_file.txt", "r")
        string = dog_file.read()
        consonant_count = 0
        consonants = "QqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
        for consonants in consonants:
            for file_consonants in string:
                if consonants == file_consonants:
                    consonant_count += 1
        print(f"The total number of consonants in this document is {consonant_count}.\n")

    # This is the document reading of the program.
    # NOTE: You have to open the file in every instance within a loop.

    read_ask = input("Would you like me to read this document to you? ")
    if read_ask in yes:
        dog_file = open("../Practice/Scrap Text Files/dog_file.txt", "r")
        for lines in dog_file.readlines():
            print(lines.rstrip())  # First practical use of the rstrip() function.

print("\nThanks for playing!")
dog_file.close()
exit()
