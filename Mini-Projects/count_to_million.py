print(list(range(1,1000001)))

#  The below chunk of code was effectively reduced to the above line of code. Woo!

list_nums = []
nums = 0

add_nums = True

while add_nums:
    nums += 1
    list_nums.append(nums)
    print(nums)
    if nums == 1000000:
        add_nums = False


