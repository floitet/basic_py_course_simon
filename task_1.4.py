number = int(input("Enter positive natural number "))
biggest_digit = 0
num = number
while number:
    temp = num % 10
    num = num // 10
    if temp > biggest_digit:
        biggest_digit = temp
    if biggest_digit == 9:
        break
print(f"Biggest digit in the {number} is: {biggest_digit}")
