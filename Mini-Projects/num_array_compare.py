# Given the array nums, for each nums[i] find out how many numbers in
# the array are smaller than it. That is, for each nums[i] you have to count
# the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

new_array = []
array = [1, 2, 3, 4, 5, 6, 7, 8]
num_count = int(0)

num = int(input("What's the number you want to compare with the array? "))

for nums in array:
    if nums < num:
        num_count += 1
        new_array.append(nums)
    # if nums > num:
    #     new_array.append(nums)  # This section of code compares your num upwards.
    #     num_count += 1

print(f"The number of numbers smaller than the inputted number is {num_count}")
print(f"Your new array is: {new_array}")

#  I did it! I (sort of) completed my first challenge! I believe the challenge
#  (from leetcode) wanted the user to use a class for the solution.
