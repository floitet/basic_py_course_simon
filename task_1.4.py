user_number = int(input('Type in any number from 1 to 9,999.'))
highest_digit = 0

if user_number < 100:
    num1 = user_number // 10
    num2 = user_number % 10
    while True:
        if num1 != highest_digit:
            highest_digit += 1
        else:
            break
        if highest_digit == 9:
            break
    while num2 > highest_digit:
        highest_digit += 1
        if highest_digit == 9:
            break
    print(f"The highest digit in your number is {highest_digit}")

if 100 <= user_number < 1000:
    num1 = user_number // 100
    num2 = (user_number // 10) % 10
    num3 = user_number % 10
    while True:
        if num1 != highest_digit:
            highest_digit += 1
        else:
            break
        if highest_digit == 9:
            break
    while num2 > highest_digit:
        highest_digit += 1
        if highest_digit == 9:
            break
    while num3 > highest_digit:
        highest_digit += 1
        if highest_digit == 9:
            break
    print(f"The highest digit in your number is {highest_digit}")

if 1000 <= user_number < 10000:
    num1 = user_number // 1000
    num2 = (user_number // 100) % 10
    num3 = (user_number// 10) % 10
    num4 = user_number % 10

    while True:
        if num1 != highest_digit:
            highest_digit += 1
        else:
            break
        if highest_digit == 9:
            break
    while num2 > highest_digit:
        highest_digit += 1
        if highest_digit == 9:
            break
    while num3 > highest_digit:
        highest_digit += 1
        if highest_digit == 9:
            break
    while num4 > highest_digit:
        highest_digit += 1
        if highest_digit == 9:
            break
    print(f"The highest digit in your number is {highest_digit}")
