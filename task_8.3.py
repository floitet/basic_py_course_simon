# Task 8.3
class MyIntError(Exception):
    def __init__(self, text):
        self.text = text


user_list = []
while True:
    try:
        user_says = input('Type in any number or "stop" to quit.')
        if user_says == 'stop':
            print(user_list)
            break
        if user_says.isalpha():
            raise MyIntError('You typed in a symbol instead of number. Try again.')

    except MyIntError as err:
        print(err)

    else:
        user_list.append(int(user_says))
        print(f'You added {user_says} to the list.')
