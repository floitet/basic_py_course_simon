# Вариант с ручным вводом

user_input_numbers = input('Type in random amount of natural random numbers divided by space')
random_numbers = user_input_numbers.split(" ")

for num, val in enumerate(random_numbers):
    random_numbers[num] = int(val)

random_numbers.sort(reverse=True)

print(f"OK, great! This is your list of numbers in descending order {random_numbers}.")

user_number = int(input('Type in any natural number.'))

for num, val in enumerate(random_numbers):
    if user_number > val:
        user_number = str(user_number)
        random_numbers.insert(num, user_number)
        break

    if num + 1 == len(random_numbers):
        user_number = str(user_number)
        random_numbers.append(user_number)
        break

print(f"Here is your new list with added number: {random_numbers}.")


# Более простой вариант с заранее указанной последовательностью чисел

random_numbers = [81, 65, 37, 25, 11, 11]
user_number = int(input('Type in any natural number.'))

for num, val in enumerate(random_numbers):
    if user_number > val:
        user_number = str(user_number)
        random_numbers.insert(num, user_number)
        break

    if num + 1 == len(random_numbers):
        user_number = str(user_number)
        random_numbers.append(user_number)
        break

print(f"Here is your new list with added number: {random_numbers}.")


