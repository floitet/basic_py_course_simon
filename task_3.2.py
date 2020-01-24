# вариант с вводом инфы пользователем при вызове функции.


def user_info(name, birth_year, current_city, email, phone_number):
    try:
        # обработка исключений для всех переменных сразу
        for i1 in name:
            if i1.isdigit():
                raise ValueError

        for i2 in birth_year:
            if i2.isalpha():
                raise ValueError

        for i3 in current_city:
            if i3.isdigit():
                raise ValueError

        if email.count("@") == 0:
            raise ValueError

        for i4 in phone_number:
            if i4.isalpha():
                raise ValueError

        print(f"Your name is {name}, you were born in year {birth_year} and now you are living in {current_city}."
              f" In the mean time your email is {email} and phone number is {phone_number}")
    except ValueError:
        print('Some of your info was not filled in correct. Try again.')


user_info(birth_year=input('Type in your birth year'),
          email=input('And your email'),
          name=input('And your name of course))'),
          current_city=input('It would also be useful if you told us where is it you are living now'),
          phone_number=input('And the very last thing is your phone number'))


# **************************************************************************************************************
# вариант с обработкой исключений и вводом пользователя вне вызова фунции.


def user_info(name, birth_year, current_city, email, phone_number):
    """организуем вывод инфы внутри функции в одну строку"""
    print(f"Your name is {name}, you were born in the year {birth_year} and now you are living in {current_city}."
          f" In the mean time your email is {email} and phone number is {phone_number}")


# обработка исключений для переменной name

while True:
    try:
        name = input('Your name')

        for i in name:
            if i.isdigit():
                raise ValueError
        break
    except ValueError:
        print('Please, type in correct name. No digits.')

# обработка исключений для переменной birth_year

while True:

    try:
        birth_year = input('Your birth year')
        for i in birth_year:
            if i.isalpha():
                raise ValueError
        break
    except ValueError:
        print('Please, type in correct year. No letters.')

# обработка исключений для переменной current_city

while True:
    try:
        current_city = input('Current city')
        for i in current_city:
            if i.isdigit():
                raise ValueError
        break
    except ValueError:
        print('Please, type in existing city. No digits.')

# обработка исключений для переменной email

while True:

    try:
        email = input('And your email')
        if email.count("@") == 0:
            raise ValueError
        break
    except ValueError:
        print('Please, type in existing email. Must include "@" sign.')

# обработка исключений для переменной phone number

while True:

    try:
        phone_number = input('And the very last thing is your phone number')
        for i in phone_number:
            if i.isalpha():
                raise ValueError
        break
    except ValueError:
        print('Please, type in correct year. No letters.')

# вызов функции с именованными аргументами

user_info(name=name, email=email, current_city=current_city, phone_number=phone_number, birth_year=birth_year)


