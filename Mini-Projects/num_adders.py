#  I tried for a while to design a function that could add numbers, but I didn't
#  really know what I wanted my end-product to look like. So, I built a simple
#  program that adds numbers together. The only way to break from the loop is to
#  give the input() a string, which will cause a ValueError, breaking from the loop.
#  Once broken, the program spits out the sum of your inputted numbers using +=.

total = int()

try:
    while True:
        num = int(input("Add your number: "))
        total += num
except ValueError:
    print("Adding numbers...")

print(total)


#  This num_adder uses an array to add the numbers. This particular version has the
#  user input an arbitrary amount of numbers, which the user breaks from when they have put
#  five total numbers. If they put a string, I've set up a Try-Except block to handle
#  the error (ValueError), which will bring the user back to the input. Only when the user
#  has reached 5 total inputted values, then the loop will break. I had to make a point of
#  setting up the "if ask_count == 5" line because otherwise, if the user hit the Except
#  block, they'd break from the main While loop. I only wanted them to break from this loop
#  when they've broken from the input loop.

array = []
total = 0
ask_count = 0

while True:
    try:
        while ask_count < 5:
            array.append(int(input("Number? ")))
            ask_count += 1
    except ValueError:
        print("Invalid value.")
    if ask_count == 5:
        break

for number in array:
    total += number

print(total)
print(array)  # This is put in place to prove to the user that it made the array.


#  This version of the num_adder is, finally, a function. It takes a list, iterates through the
#  list, adds each integer value of the list to "total", and then returns the total (for you
#  to print).


#  This array is a sample array to be used in the function.
array = [1, 1, 1, 1]


def num_adder(array):
    total = 0
    for number in array:
        total += number
    return total


print(num_adder(array))