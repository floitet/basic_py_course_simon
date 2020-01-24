# вариант с вводом чисел внутри функции


def divide():
    try:
        num1 = int(input('Type in first number'))
        num2 = int(input('Type in second number'))
        return num1 / num2
    except ZeroDivisionError:
        return "You can't divide by zero"

print(divide())


# **************************************************************************************************************
# вариант с вводом чисел пользователем при вызове функции


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "You can't divide by zero"


print(divide(int(input('Type in first number')), int(input('Type in second number'))))



