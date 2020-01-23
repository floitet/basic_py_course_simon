
# ******************************************************************************************************************
# вариант без ввода пользователя + c использованием оператора **


def powering(x, y):
    try:
        if x <= 0:
            raise ValueError
    except ValueError:
        print('We need positive number here.')

    try:
        if y >= 0:
            raise ValueError
        print(f'Your "x" raised to power by "y" equals {x ** y}')
    except ValueError:
        print('We need negative integer here.')


powering(86, -2)

# ******************************************************************************************************************
# вариант без ввода пользователя + c использованием цикла и обычного умножения


def powering(x, y):
    try:
        if x <= 0:
            raise ValueError
    except ValueError:
        print('We need positive number here.')
    try:
        if y >= 0:
            raise ValueError
        x = 1 / x
        for i in range(abs(y) - 1):
            x = (x * x)
        print(f'Your "x" raised to power by "y" equals {x}')
    except ValueError:
        print('We need negative integer here.')


powering(86, -2)


# ******************************************************************************************************************
# вариант с вводом пользователя внутри функции + c использованием оператора **

def powering():
    while True:
        try:
            x = float(input('Any real positive number.'))
            if x <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('We need positive number here.')

    while True:
        try:
            y = int(input('Any negative integer number.'))
            if y >= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('We need negative integer here.')

    print(f'Your "x" raised to power by "y" equals {x ** y}')


powering()


