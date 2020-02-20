# Task 8.2
class MyZeroError(Exception):
    def __init__(self, text):
        self.text = text


try:
    num_1, num_2 = map(int, input('Type in two numbers for subtraction divided by space bar.').split())
    if num_2 == 0:
        raise MyZeroError("Can't divide by zero.")
except MyZeroError as err:
    print(err)
else:
    print(float(f'{float(num_1 / num_2):.3f}'))
