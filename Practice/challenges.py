import itertools

def stutter(word):
    """Prints a stuttered version of a string."""
    print(f"{(word.capitalize()[0:2])}... {word.lower()[0:2]}... {word.lower()}.")


def one_adder(num):
    """Adds 1 to the number passed through it."""
    new_num = num + 1
    print(f"Your number plus 1 equals {new_num}.")


def letter_doubler(string):
    """Doubles the letters in any given string."""
    newstr = ""
    for letter in string:
        newstr += letter + letter
    return newstr


def list_in_ord(user_list):
    """Takes a list and tells the user if its values are in alphabetical order."""
    list_copy = user_list.copy()
    user_list.sort()
    if user_list == list_copy:
        return True
    else:
        return False


def list_val_changer(list, change_value):
    """Changes the first value of a list based on user input."""
    list = list
    list[0] = change_value
    return list


def dupe_remover(list):
    """Removes duplicates from a list."""
    set = []
    for i in list:
        if i not in set:  # Had to get help with this one. Notice how I use the "if i not in" conditional.
            set.append(i)
    return sorted(set)


def quiet(str):
    """Sentence-cases any string you input. If the user doesn't put in
    anything, then the function will return a unique statement"""
    if str != "":
        return str.lower().capitalize()
    else:
        return '"Shhhh," whispered the user.'


def age_to_days(age):
    """Returns the approximate number of days of the user based on their age in years."""
    days = int(age) * 365
    return int(days)


def cars_needed_mod(people):
    """Returns the number of cars needed for a number of people.
    We assume that a car can comfortably fit 4 people; 5 would merit another car.
    In this example, I use a module that rounds a value up, thus assuming that any
    people remaining after a division by 4 occurs, another car would be needed."""
    import math
    cars = math.ceil((people / 4))
    return int(cars)


def cars_needed_rem(people):
    """Returns the number of cars needed for a number of people.
    We assume that a car can comfortably fit 4 people; 5 would merit another car.
    In this example, I use the modulo to check whether or not there is a remainder
    of passengers after dividing by 4. If so, there is another car added."""
    cars = people / 4
    if (people % 4) >= 1:
        cars = cars + 1
    return int(cars)


def vowel_counter(string):
    """Counts the vowels, in both cases, in a string the user inputs."""
    vowel_count = 0
    for letter in string:
        if letter in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            vowel_count += 1
    return vowel_count


def x_o_compare(string):
    """
    Looks at the number of Xs and Os in a string. If they are
    both even, the function will return True. Otherwise, it'll return False.
    """
    x_count = 0
    o_count = 0
    for letter in string:
        if letter in ["X", "x"]:
            x_count += 1
        if letter in ["O", "o"]:
            o_count += 1
    if x_count == o_count:
        return True
    else:
        return False


def even_num_counter(num):
    """
    Finds all the even numbers in a range from 1 to the number you specify.
    I added an extra condition that will only return the even number range if the
    inputted number is even. You can also switch it to an odds counter by changing the
    remainder in the modulo to 1."""
    even_nums = []
    for i in range(1, num+1):
        if (i % 2) == 0 and (num % 2 == 0):
            even_nums.append(i)
    return even_nums


def str_in_order(string):
    """
    Checks to see if a string is in order. Note that capitals are
    sorted first, then lowercase letters, each in respective ascending order.
    """
    old_string = string
    new_string = "".join(sorted(string))  # Notice how I use a blank string to join list elements, plus dot notation.
    if old_string == new_string:
        return True
    else:
        return False


def secr_soc_maker(list):
    """
    Takes a list of names, then makes a capitalized, initialed
    acronym based on the items in the inputted list.
    """
    society_list = []
    for name in list:
        society_list.append(name.capitalize()[0])
    society_name = "".join(society_list)
    return society_name


def missing_num_detector_1(list):
    """Takes in a list of numbers from 1-10 and returns the missing number."""
    proper_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in proper_list:
        if num not in list:
            return num


def missing_num_detector_2(list):
    """Takes in a list of numbers from 1-10 and returns a list of missing numbers."""
    proper_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    missing_nums = []
    for num in proper_list:
        if num not in list:
            missing_nums.append(num)
    return missing_nums


def boolean_reverser():
    """Returns the opposite boolean that the user inputs."""
    while True:
        boolean = input("What is your value? ")
        if boolean in ["True", "true", "T", "t"]:
            boolean = False
            break
        if boolean in ["False", "false", "F", "f"]:
            boolean = True
            break
        if boolean not in [True, False]:
            print("Error. Expected boolean.")
    print(f"Hey now! Your boolean is now {boolean}.")


def int_to_str(input):  # Is there another way to do this without the str() function?
    """Converts an integer to a string."""
    ans = input
    new_ans = str(ans)
    return new_ans


def str_to_int(input):  # Is there another way to do this without the int() function?
    """Converts a string to an integer."""
    ans = input
    new_ans = int(ans)
    return new_ans


def fizz_buzz(num):
    """
    Evaluates a numeric input, then outputs a string based on the numbers
    that it's a multiple of. If it is not a multiple of either number, the number itself
    is returned as a string
    """
    if (num % 3) == 0 and (num % 5) == 0:  # My first practical use of the modulus operator.
        print("FizzBuzz")
    elif (num % 3) == 0:
        print("Fizz")
    elif (num % 5) == 0:
        print("Buzz")
    else:
        print(str(num))


def square_areas_difference(radius):
    """
    Returns a value equal to the difference of areas between
    an outer square and an inner square, with a circle inside being a circumcircle for
    the smaller square, and an incircle for the outer one.
    """
    outer_square_area = ((radius * 2) * (radius * 2)) / 2  # My first practical use of geometry.
    return int(outer_square_area)


def num_length(num):
    """Counts the number of digits in a number and returns the value."""
    num = str(num)
    num_count = 0
    for i in num:
        num_count += 1
    return num_count


def profit_calc(dictionary):
    """
    Looks at a dictionary (see below) containing the cost price, sell price
    and total inventory for a given item. Based on the total inventory of that item, and assuming
    all the items have been sold, this function returns the value of the total profie earned.
    """
    profit = {  # You would exclude this dictionary from the function and use it separately.
        "cost_price": 17.64,
        "sell_price": 19.99,
        "inventory": 900,
    }
    single_profit = dictionary.get("sell_price") - dictionary.get("cost_price")
    tot_profit = single_profit * dictionary.get("inventory")
    return tot_profit


def date_reformatter(date_string):
    """Converts a date formatted as MM/DD/YYYY to YYYYDDMM."""
    date = []
    month = date_string[0:2]  # My first practical use of referencing specific index ranges.
    day = date_string[3:5]
    year = date_string[6:10]
    date.append(year)
    date.append(day)
    date.append(month)
    new_date = "".join(date)
    return new_date


def stupid_addition(par_1, par_2):
    """
    Takes two parameters and, if both parameters are strings, adds them
    as if they were integers. If the two parameters are already integers, the function
    will concatenate them.
    """
    if par_1 == str(par_1) and par_2 == str(par_1):
        par_1 = int(par_1)
        par_2 = int(par_2)
        result = par_1 + par_2
        return result
    if par_1 == int(par_1) and par_2 == int(par_2):
        par_1 = str(par_1)
        par_2 = str(par_2)
        result = "".join(par_1 + par_2)
        return result


def unscrambler(list_1, list_2):
    """
    Builds a word by looking at letters in a scrambled list, then referring to the
    integers in a "code list" that tells the function the proper order that the unscrambled words
    should be in. It then returns a string to the user that contains the unscrambled word.
    """
    scrambled_word = ["e", "t", "s", "t"]  # This would be list_1
    scrambled_code = [3, 0, 2, 1]  # This would be list_2
    unscrambled_word_pre = []
    for i in list_2:
        unscrambled_word_pre.append(list_1[i])  # One of my first practical uses of referencing dynamic index ranges.
    unscrambled_word = "".join(unscrambled_word_pre)
    return unscrambled_word


def neutralizer(str_1, str_2):
    """
    Analyzes two 3-character strings consisting of "+" and "-"
    characters. For each position of each character in the first string, it will
    "interact" with the second string in the following ways: +'s against +'s remain
    +, -'s against -'s remain -, and + against - (and vice versa) will return a 0, neutral.
    """
    new_str = []
    # indices = [0, 1, 2]  # My first practical use of using an index to reference a dynamic index range.
    for i in range(0, 3):  # *** This is the more efficient way to do it!
        if str_1[i] == "+" and str_2[i] == "+":
            new_str.append("+")
        if str_1[i] == "-" and str_2[i] == "-":
            new_str.append("-")
        if str_1[i] == "+" and str_2[i] == "-":
            new_str.append("0")
        if str_1[i] == "-" and str_2[i] == "+":
            new_str.append("0")
    return "".join(new_str)


def string_to_phone(string):
    """
    Takes a string of letters and converts it to touch tone letters,
    based on a traditional phone.
    """
    touch_tone = {
        "abc": 2,
        "def": 3,
        "ghi": 4,
        "jkl": 5,
        "mno": 6,
        "pqrs": 7,
        "tuv": 8,
        "wxyz": 9,
    }
    number = []
    for i in string:
        for x in touch_tone:
            if i in x:
                number.append(str(touch_tone[x]))  # My first practical use of using a dictionary as a reference.
    return "".join(number)


def caps_indexes(string):
    """Returns the index values of the capital letters in a string."""
    indices = []
    # counter = [i for i in range(len(string))]  # This is NOT how to make a range on command; my first practical use.
    # for num in counter:
    for i in range(len(string)):  # This is the more efficient way to make a number-scrolling range!
        if string[i].isupper():
            indices.append(i)
    return indices


def pluralize(list):
    """
    Looks at a list of words and pluralizes them if there is
    more than one occurrence of the word, otherwise it returns the word(s)
    by itself/themselves.
    """
    new_list = []
    for i in list:
        if (list.count(i) > 1) and (f"{i}s" not in new_list):  # Ensures that the plural instance doesn't already exist.
            new_list.append(f"{i}s")
        elif list.count(i) == 1:
            new_list.append(i)
    return new_list


def vowel_censor(string):
    """Censors all vowels in a string."""
    new_string = []
    for i in string:
        if i in "AEIOUaeiou":
            new_string.append("*")
        else:
            new_string.append(i)
    return "".join(new_string)


def vowel_censor_mod(string):
    """Censors all vowels in a string, and also returns a string of the stripped vowels."""
    new_string = []
    stripped_vowels = []
    for i in string:
        if i in "AEIOUaeiou":
            new_string.append("*")
            stripped_vowels.append(i)
        else:
            new_string.append(i)
    return "".join(new_string), "".join(stripped_vowels)


def vowel_uncensor(str_1, str_2):
    """
    Looks at a string (str_1) whose vowels have been censored with asterisks,
    and a string (str_2) of the missing vowels in their respective order. It then un-censors the
    censored string using the vowels given in the vowels list.
    """
    new_str = []
    vowels = []
    for i in str_2:
        vowels.append(i)
    for i in str_1:
        if i == "*":
            new_str.append(vowels.pop(0))  # My first practical use of the .pop() list method.
        else:
            new_str.append(i)
    return "".join(new_str)


def vow_cens_uncens_connector(string):  # My first function that allows two other functions to interact.
    """
    Allows vowel_censor_mod and vowel_uncensor to interact with one another.
    A string passed through this function then passes the string through vowel_censor_mod, which
    separates the consonants and vowels, replacing the latter with asterisks in the original
    string. It then passes the two values through the vowel_uncensor function, which assembles
    the original string back together by popping the vowels off of the stripped_vowels list
    from the vowel_censor_mod function. The function also prints out the string before and after
    it allows the functions to work together, to show you that it's working each step of the way.
    """
    for a, b in vowel_censor_mod(string), vowel_censor_mod(string):  # First practical use of a multivariable For loop.
        print(f"Your original string is '{string}'")
        print(f"Your censored string is '{a}', and the vowels removed from it are '{b}'")
        return f"Reassembled, your string is now '{vowel_uncensor(a, b)}'"


def give_me_something(string):
    """Returns the word 'something' at the beginning of the inputted string."""
    phrase = f"Something {string.lower()}."
    return phrase


def water_balloon_pop(list):
    """
    Creates a "water balloon popping effect," in which a center number in a list of otherwise 0s
    'pops,' trailing behind -1 values in either direction, in a returned list.
    """
    # from math import floor  (Requires floor() function from Math module in Python Standard Library.)
    # Example List: water_balloon_pop([0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0])
    balloon_value = list[floor(len(list) / 2)]
    center = int(floor(len(list) / 2))
    rem_indices = [i+1 for i in range(center)]
    for i in rem_indices:
        list[center + i] = balloon_value - i
        list[center - i] = balloon_value - i
    return list


def censor_words(string, censor_list, censor_char):
    """Censors certain words in a string with a specified character."""
    new_str = string.split()  # First practical use of the split() method.
    for i in new_str:
        if i in censor_list:
            new_str.insert(new_str.index(i), (censor_char * len(i)))
            new_str.remove(i)
    return f"{' '.join(new_str)}"


def no_duplicate_letters(string):
    """
    Analyzes a string and tells the user if any of its words have
    duplicate letters (if so, False is returned, otherwise True).
    """
    pre_str = string.split()
    for word in pre_str:
        for letter in word:
            count = word.count(letter)
            if count > 1:
                return False
        return True


def majority_vote(list):
    """
    This function tells the user which element in a list appears more than
    any other. If there are 0 or 1 elements in the list, or if there is no majority,
    None is returned.
    """
    elements = {}
    dup_counts = []

    # Builds a dictionary based on each key in the passed list, as well as the number of
    # occurrences of that key within the list.
    for i in list:
        elements[i] = list.count(i)

    # Builds a list of the number of occurrences of each value, key in the list and sorts in
    # descending order.
    inverse = [(value, key) for key, value in elements.items()]

    # Builds a list of all values (numbers of occurrence) for each key in the dictionary.
    for key, value in elements.items():
        dup_counts.append(value)

    # Check the total count of elements in the list. If there are 1 or 0 elements, assume there
    # is no actual majority (even though, technically, only one element occurrence would be a 100%
    # majority.
    total_count = 0
    for i in list:
        total_count += list.count(i)
    if total_count == 1:  # If there's only one element, return None.
        return None
    if total_count == 0:  # If there are no elements, return None.
        return None

    # Checks to see if any of the occurrences happen more than once (there is a tie between
    # any of the occurrences of the keys in the dictionary). If so, the function cannot determine
    # a key that alone occurs more than any other.
    for i in dup_counts:
        if dup_counts.count(i) > 1:
            return None

    # If there is a key that alone occurs more than any other, the function will print it by
    # referencing a sorted list of value, key occurrences. It then prints the second index position
    # of the highest item(), which is the key that occurs the most (the list was sorted in descending
    # order because the user wants to get the highest number of occurrences (value), sorting the
    # list in that way, then returning the key associated with that highest number.
    return max(inverse)[1]


def show_the_love(list):
    """
    Removes 25% from larger numbers in a list and gives
    the total to the smallest (third) number.
    """
    love = 0
    for i in range((len(list))):
        if list[i] != min(list):
            list[i] = list[i] * .75
            love += (list[i] / .75) * .25
    list[list.index(min(list))] += love
    return list


def all_the_letters(word_1, word_2):
    """
    Takes in two words as input and returns a list of three elements:
        (1) Shared letters between two words.
        (2) Letters unique to word 1.
        (3) Letters unique to word 2.
    Each element should have unique letters, and have each letter be alphabetically sorted.
    """
    letters_list = []
    word_lists = ["", "", ""]

    for x in word_1:
        for y in word_2:

            # Shared letter sorting:
            if x in word_1 and x in word_2 and x not in word_lists[0]:
                word_lists[0] += x

            # Unique letters in word 1 sorting:
            if x in word_1 and x not in word_2 and x not in word_lists[1]:
                word_lists[1] += x

            # Unique letters in word 2 sorting:
            if y in word_2 and y not in word_1 and y not in word_lists[2]:
                word_lists[2] += y

    # Adding alphabetized sets of letters to the output list:
    for i in word_lists:
        i = sorted(i)
        letters_list.append("".join(i))

    return letters_list


def num_to_eng(num):
    """Returns a string representation of an integer, inclusive of 0 to 999, written in English."""

    # Dictionary defines all unique integer values/prefixes in English.
    nums_dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        "hund_poss": "hundred",
    }

    # Final number values, in English, are set to "" by default, unless logically changed.
    num_of_hun, num_of_ten, hund_poss, num_of_one = "", "", "", ""

    # User-inputted number is converted to a list of strings whose index values can be parsed/analyzed.
    num = list(str(num))

    # Original user-inputted number is converted back to its original form as a reference.
    orig_num = int("".join(num))

    # Numbers 0-19 are built using the nums_dict dictionary.
    if orig_num in range(0, 20):
        num_of_one = nums_dict[orig_num]

    # Numbers 20-99 are built using the nums_dict dictionary.
    elif orig_num in range(20, 100):

        # 20-99; Perfect tens.
        if orig_num % 10 == 0:
            num_of_ten = nums_dict[int(''.join(num[0])) * 10]

        # 20-99; Not perfect tens.
        elif orig_num % 10 != 0:
            num_of_ten = nums_dict[int(''.join(num[0])) * 10]
            num_of_one = f"-{nums_dict[int(''.join(num[1]))]}"

    # Numbers 99+ are built using the nums_dict dictionary (perfect hundreds).
    elif orig_num > 99:
        num_of_hun = nums_dict[int(num[0])]
        hund_poss = nums_dict["hund_poss"]

        # Numbers 99+, ending in the ones/teens, are built using the nums_dict dictionary.
        if int("".join(num[1:3])) in range(1, 20):
                num_of_ten = nums_dict[int("".join(num[1:3]))]

        # Numbers 99+, beyond those ending in the ones/teens, are built using the nums_dict dictionary.
        elif int("".join(num[1:3])) > 19:

            # 99+; Perfect tens.
            if int("".join(num[1:3])) % 10 == 0:
                num_of_ten = nums_dict[int(''.join(num[1])) * 10]

            # 99+; Imperfect tens.
            else:
                num_of_ten = nums_dict[int(''.join(num[1])) * 10]
                num_of_one = f"-{nums_dict[int(''.join(num[2]))]}"

    # The final number, written in English, is assembled, neatened and returned.
    final_num = f"{num_of_hun} {hund_poss} {num_of_ten}{num_of_one}"
    return f"{final_num.lstrip().title()}"


def eng_to_num(string):
    """
    Returns an integer representation of a number in string form, written in English.
    Requires the use of the num_to_eng function. Must be title case and hyphenated (for tens place).
    """
    # Set up a dictionary that will hold numeric values for each string number key.
    reverse_dict = {}

    # Pass all 1,000 integer values through the num_to_eng function and build a dictionary
    # by associating each string number (key) with its corresponding integer (value).
    for i in range(0, 1000):
        reverse_dict[(num_to_eng(i))] = i

    # Return the integer value for the key (string number) passed through the function.
    return reverse_dict[string]


def simon_says(list_1, list_2):
    """
    Takes in two lists and returns True if the second list follows the first
    list by one element, and False otherwise.
    """
    # Defines a boolean stored in a variable that will ensure that the list synchronicity is maintained.
    repeat = True

    # Loops through both lists simultaneously and checks that the second index position of the second list is
    # the same as the first index position of list_1.
    while repeat:
        for i in range(1, len(list_1)):
            if list_2[i] == (list_1[i - 1]):    # Optional line at if statement: Restrict list_2's order to be
                pass                            # numerically synchronous with list_1 (line_2's first index position
            else:                               # is equal to the first index position of list_1 - 1:
                return False                    # "and list_2[i - 1] == list_1[i - 1] - 1:"
        return True


def alt_simon_says(lst1, lst2):
    """This is Altenburger's take on the simon_says function."""
    comp2 = lst1[:-1]
    if lst2[1:] == comp2:
        return True
    else:
        return False


def anagram(string, _list):
    """Returns True if a given name can generate an array of words."""
    dissected_word = list(string.lower())
    for item in _list:
        for letter in item:
            if letter in dissected_word:
                dissected_word.remove(letter)
    if dissected_word == [' ']:
        return True
    else:
        return False


def sentence_searcher(text, word):
    """Returns the sentence within a text that contains a specified word."""

    sent_dict = []
    sent_dict2 = []

    # Split up the sentences and add to a list.
    for i in text.split("."):
        if i != '':
            sent_dict.append(i.strip())

    # Replace the periods in the sentences, since they're removed by the split() function.
    for i in sent_dict:
        x = f"{i}."
        sent_dict2.append(x)

    # Return the sentence containing the requested word.
    for i in sent_dict2:
        if (word.lower() in i) or (word.upper() in i) or (word.title() in i):
            return i
        else:
            return f'The word "{word}" is not contained in your text.'


def vowel_links(text):
    """
    Given a sentence as text, return True if any two adjacent words have this property:
    One word ends with a vowel, while the word immediately after begins with a vowel
    """

    # Specify a list of all vowel occurrences.
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    # Add items from text to a list.
    sentence = []
    for i in text.split():
        sentence.append(i)

    # Parse through the split sentence (from the list) and check the index positions
    # of the last letter of each iteration, as well as the first letter of the subsequent
    # iteration. Checks to see if these iterations simultaneously occur as vowels
    # (checking the vowels list).
    try:
        for i in range(len(sentence)):
            if ((sentence[i])[-1] in vowels) and ((sentence[i+1])[0]) in vowels:
                return True
    except IndexError:
        pass

    return False


def find_the_difference(orig_str, new_str):
    """Tells the user the added difference between a set of two strings."""

    # Create a set of lists used to compare the two strings.
    orig_str_list = []
    new_str_list = []
    differences = []

    # Populate lists with string contents.
    for i in orig_str:
        orig_str_list.append(i)
    for i in new_str:
        new_str_list.append(i)

    # Parse the latter string and check to see which elements occur beyond the
    # limit of the original string's contents within the new one.
    str_limit = len(orig_str_list)
    for i in new_str_list[str_limit:]:
        differences.append(i)

    # Return the list of differences, joined together as a string.
    return ''.join(differences)


def longest_nonrepeating_substring(string):
    """Returns the longest non-repeating substring for a string input."""

    # Sets up a list that will be appended with elements of the
    # non-repeating substring.
    longest_string = []
    string_list = []
    parse = True

    # Parses through the elements of the string and appends longest_string
    # if each element subsequent to the parsed one does match it. Does not add
    # repeating elements.
    while parse and longest_string not in string_list:
        try:
            for i in range(len(string)):
                if string[i] not in longest_string:
                    if string[i] != string[i-1]:
                        longest_string.append(string[i])
                    else:
                        longest_string.append(string[i])
                    break

        # Circumvents the error of indexed string elements beyond the range of len().
        except IndexError:
            pass

        # Append

        # else:
        #     longest_string = ''.join(longest_string)
        #     string_list.append(longest_string)

        # Returns a string representation of longest_string.
        return string_list


def rearranged_number(num):
    """
    Returns the difference between the maximum number that can be
    rearranged/formed from a given integer, minus the minimum number.
    """
    # Rearranges the digits of the given integer so that it is sorted
    # to be the smallest possible number.
    num_min = []
    for i in str(num):
        num_min.append(i)
    num_min.sort()

    # Assigns num_max the maximum possible number (based on the reversed
    # num_min).
    num_max = reversed(num_min)

    # Subtracts the minimum numeric configuration from the maximum.
    return int(''.join(num_max)) - int(''.join(num_min))


def animals(num1, num2, num3):
    """
    Tells the user how many legs of farm animals total are counted based on
    the assumption that the first number is chickens (2 legs), and the latter
    two are cows (4 legs) and pigs (4 legs).
    """
    return (num1 * 2) + (num2 + num3) * 4


def loves_me(num):
    """Given a number of petals, returns a string which repeats the
    phrases 'Loves me' and 'Loves me not' for every alternating petal,
    and return the last phrase in all caps."""

    # Sets up the string of 'love mes' depending on user's inputted value.
    new_line = []

    # Appends 'Loves me' to the list for every other index position, with
    # 'loves me not' as the alternating item.
    for x in range(num):
        if x in [0, 2] or (x % 2 == 0):
            new_line.append('Loves me')
        else:
            new_line.append('Loves me not')

    # Uppercases the last value on the list.
    new_line[-1] = new_line[-1].upper()

    return new_line


def sort_by_letter(items):
    """Sorts each string in a list by the letter in alphabetic ascending order."""
    # Creates a blank list that will be populated with the final sorted values.
    final = []

    # Iterates through the given list and appends them to the final list
    # according to each iteration of the sorted alphabet.
    for letter in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz':
        for value in items:
            if letter in value:
                final.append(value)

    # Returns the final, sorted list.
    return final


def isSumEqual(firstword, secondword, targetword):
    """
    :type firstword: str
    :type secondword: str
    :type targetword: str
    :rtype: bool
    """

    letters_dict = {}

    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        letters_dict[letter] = str(letters.index(letter))

    conv_firstword, conv_secondword, conv_targetword = '', '', ''

    for i in firstword:
        conv_firstword += letters_dict[i]
    for i in secondword:
        conv_secondword += letters_dict[i]
    for i in targetword:
        conv_targetword += letters_dict[i]

    if int(conv_firstword) + int(conv_secondword) == int(conv_targetword):
        return True
    else:
        return False


def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    return address.replace('.', '[.]')


def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    new_list = []
    for i in range(1, len(nums) + 1):
        new_list.append(sum(nums[:i]))
    return new_list


def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    new_array = []
    for i in range(0, len(nums)):
        if len(new_array) <= len(nums) - 1:
            new_array.append(nums[i])
            new_array.append(nums[i+n])
        else:
            return new_array


def maximumWealth(accounts):
    """Returns the maximum sum of a series of account totals (integer lists)."""
    max_act = 0
    for account in accounts:
        if sum(account) > max_act:
            max_act = sum(account)
    return max_act


def kidsWithCandies(candies, extraCandies):
    kids_list = []
    for i in candies:
        if i + extraCandies >= max(candies):
            kids_list.append(True)
        else:
            kids_list.append(False)
    return kids_list


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Number of Good Pairs
        Given an array of integers nums.
        A pair (i,j) is called good if nums[i] == nums[j] and i < j.
        Return the number of good pairs.
        """
        pairs = list(itertools.combinations(nums, 2))
        matches = 0
        for i in pairs:
            if i[0] == i[1]:
                matches += 1
        return matches



class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        Jewels & Stones
        You're given strings jewels representing the types of stones that are jewels,
        and stones representing the stones you have. Each character in stones is a type
        of stone you have. You want to know how many of the stones you have are also jewels.
        Letters are case sensitive, so "a" is considered a different type of stone from "A"
        """
        count = 0
        for i in jewels:
            for a in stones:
                if i == a:
                    count += 1
        return count




class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        How Many Numbers Are Smaller Than the Current Number
        Given the array nums, for each nums[i] find out how many numbers in the array are
        smaller than it. That is, for each nums[i] you have to count the number of valid js
        such that j != i and nums[j] < nums[i].
        Return the answer in an array.
        """
        num_nums = []
        for i in nums:
            num_count = 0
            for a in nums:
                if a < i:
                    num_count += 1
            num_nums.append(num_count)
        return num_nums


class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
        """
        sentence = []
        newer_sentence = []
        nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        for word in s.split(' '):
            the_word = []
            for letter in word:
                the_word.append(letter)
            sentence.append(the_word)
        for sort_word in sentence:
            for letter in sort_word:
                if letter in nums:
                    sort_word.remove(letter)
                    sort_word.insert(0, letter)
        sentence = sorted(sentence)
        for i in sentence:
            i.remove(i[0])
            newer_sentence = [''.join(i) for i in sentence]
        return ' '.join(newer_sentence).strip()


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        Given a string s formed by digits ('0' - '9') and '#' . We want to map s to
        English lowercase characters as follows:
        Characters ('a' to 'i') are represented by ('1' to '9') respectively.
        Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
        Return the string formed after mapping.
        It's guaranteed that a unique mapping will always exist.
        """
        nums = range(1, 27)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        dic = {}

        for num, letter in zip(nums, letters):
            if num <= 9:
                dic[str(num)] = str(letter)
            else:
                dic[str(num) + '#'] = str(letter)

        word = ''
        final = []
        nums = range(len(s))
        answer = ''

        for letter, num in zip(s, nums):
            if len(s[num:]) > 2:
                if letter != '#' and s[num+2] != '#':
                    if s[num+1] != '#':
                        word += letter
                        final.append(word)
                        word = ''
                    else:
                        continue
                elif letter != '#' and s[num+2] == '#':
                    if num < len(s):
                        word += s[num:num+3]
                        final.append(word)
                        word = ''
                    else:
                        word += s[num:num + 2]
                        final.append(word)

            if len(s[num:]) <= 2:
                if '#' not in s[num:]:
                    final.append(letter)

            if len(''.join(final)) == len(s):
                break

        # Create and return the final answer.
        for i in final:
            if i != '#':
                answer += dic[i]
        return answer


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        You are given a string allowed consisting of distinct characters and an array of strings words.
        A string is consistent if all characters in the string appear in the string allowed.
        Return the number of consistent strings in the array words.
        """
        num_consistents = 0

        for item in words:
            bools = []
            for letter in item:
                if letter not in allowed:
                    bools.append(False)
                if letter in allowed:
                    bools.append(True)
            if all(bools):
                num_consistents += 1
        return num_consistents


class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        You are given an integer n, the number of teams in a tournament that has strange rules:
        If the current number of teams is even, each team gets paired with another team.
        A total of n / 2 matches are played, and n / 2 teams advance to the next round.
        If the current number of teams is odd, one team randomly advances in the tournament,
        and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1
        teams advance to the next round.
        Return the number of matches played in the tournament until a winner is decided.
        """
        import math

        matches = 0
        teams = n

        while teams > 1:
            matches += math.floor(teams/2)
            teams -= math.floor(teams/2)
        return int(matches)


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        Given a string s. You should re-order the string using the following algorithm:
        1. Pick the smallest character from s and append it to the result.
        2. Pick the smallest character from s which is greater than the last appended character
           to the result and append it.
        3. Repeat step 2 until you cannot pick more characters.
        4. Pick the largest character from s and append it to the result.
        5. Pick the largest character from s which is smaller than the last appended character
           to the result and append it.
        6. Repeat step 5 until you cannot pick more characters.
           Repeat the steps from 1 to 6 until you pick all characters from s.
        7. In each step, If the smallest or the largest character appears more than once you can
           choose any occurrence and append it to the result.
        Return the result string after sorting s with this algorithm.
        """
        s_exp = sorted([i for i in s])
        new_str = ''

        alpha = 'abcdefghijklmnopqrstuvwxyz'

        while len(s_exp) > 0:
            for i in alpha:
                if i in s_exp:
                    new_str += i
                    s_exp.remove(i)
            for i in reversed(alpha):
                if i in s_exp:
                    new_str += i
                    s_exp.remove(i)

        return new_str


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        A self-dividing number is a number that is divisible by every digit it contains.
        For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
        A self-dividing number is not allowed to contain the digit zero.
        Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
        """
        self_divs = []

        assert left > 0 and right > 0, 'The left and right values must be 1 or higher.'

        for num in range(left, right+1):
            div_bools = []
            if '0' not in str(num):
                for digit in str(num):
                    if num % int(digit) == 0:
                        div_bools.append(True)
                    else:
                        div_bools.append(False)
            if all(div_bools) and div_bools != []:
                self_divs.append(num)

        return self_divs


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        You are given two strings s and t.
        String t is generated by random shuffling string s and
        then add one more letter at a random position.
        Return the letter that was added to t.
        """
        s_list = [i for i in s]
        t_list = [i for i in t]
        for i in s_list:
            if i in t_list:
                t_list.remove(i)
        return ''.join(t_list)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x
        causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
        """
        new_int = int(''.join(reversed([i for i in str(x) if i != '-'])))
        if new_int <= (pow(2, 31) - 1):
            if str(x)[0] == '-':
                return new_int * -1
            else:
                return new_int
        else:
            return 0


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward as forward.
        For example, 121 is palindrome while 123 is not.
        """
        if ''.join(list(reversed(str(x)))) == ''.join(list(str(x))):
            return True
        else:
            return False


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written
        as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral
        for four is not IIII. Instead, the number four is written as IV. Because the one is before the five
        we subtract it making four. The same principle applies to the number nine, which is written as IX.
        There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.

        Given a roman numeral, convert it to an integer.
        """
        final_num = 0
        rom_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }

        for i, dig in zip(iter(s), range(len(s))):
            try:
                if dig == len(s) - 1 and s[len(s)-2]+s[len(s)-1] not in ['CD', 'CM', 'XL', 'XC']:
                    final_num += rom_dict[s[dig]]

                # Special additions (400, 900, 40, 90).
                elif s[dig] + s[dig+1] in ['CD', 'CM', 'XL', 'XC']:
                    final_num += rom_dict[s[dig] + s[dig+1]]
                    continue

                elif dig == 0 and i == 'L':
                    final_num += rom_dict[i]

                elif i == 'L' and s[dig - 1] == 'X':
                    pass

                # Final digit additions (4 and 9).
                elif s[dig] + s[dig+1] in ['IV', 'IX']:
                    final_num += rom_dict[s[dig] + s[dig+1]]
                    break

                elif dig == 0:
                    final_num += rom_dict[s[dig]]

                elif s[dig] == 'M' and s[dig - 1] == 'M' or s[dig] == 'M' and s[dig + 1] == 'M':
                    final_num += rom_dict[s[dig]]

                elif i == 'L' and s[dig + 1] in ['X', 'L', 'V', 'I']:
                    final_num += rom_dict[s[dig]]

                elif s[dig] == 'C' and s[dig - 1] == 'C':
                    final_num += rom_dict[s[dig]]

                elif s[dig] in ['L', 'C', 'D', 'M'] and s[dig-1] in ['X', 'C']:
                    pass

                elif dig == 0 or len(s) - dig <= 4 and s[dig] + s[dig+1] not in ['IV', 'IX'] \
                        and s[dig-1] != 'C':
                    final_num += rom_dict[i]

                elif i == 'M' and s[0] == 'M':
                    pass

                else:
                    final_num += rom_dict[i]

            except IndexError:
                continue

        return final_num


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums.copy():
            if nums.count(i) > 1:
                nums.remove(i)

        return len(nums)

class Solution(object):
    def removeElement(self, nums: list[int], val: int) -> int:
        for num in nums.copy():
            if num == val:
                nums.remove(val)
        return len(nums)

class Solution(object):
    def twosum(self, array: list, target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, returns
        indices of the two numbers such that they add up to target.
        """
        from itertools import combinations

        for i in combinations(range(len(array)), 2):
            if array[i[0]] + array[i[1]] == int(target):
                return list(i)

class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consisting of some words separated by some number of
        spaces, return the length of the last word in the string.
        """
        num = 0
        for i in reversed(s):
            if i == ' ' and num == 0:
                pass
            elif i != ' ':
                num += 1
            elif i == ' ' and num > 0:
                break
        return num

class Solution(object):
    def longestprefix(self, strs) -> str:
        """Returns a string that indicates the longest common prefix within the given array."""
        if len(strs) == 0:
            return ""
        current = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(current) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(current) and current[j] == strs[i][j]:
                    temp += current[j]
                else:
                    break
            current = temp
        return current

class Solution(object):
    def isintpalindrome(self, x: int) -> bool:
        """Returns True if given integer is a polindrome, otherwise returns False."""
        return False if x < 0 else x == int(str(x)[::-1])