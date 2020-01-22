user_numbers = input('Type in random amount of random numbers or words divided by space')
swapping_list = user_numbers.split(" ")

print(swapping_list)

for num, val in enumerate(swapping_list, 1):
    if num % 2 == 0:
        num_new = num - 2
        swapping_list.insert(num_new, val)
        swapping_list.pop(num)

print(swapping_list)
