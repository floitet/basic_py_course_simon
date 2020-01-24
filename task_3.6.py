# решение работает и для одного слова и для нескольких слов. решение с вводом пользователя в теле функции.


def edit():
    while True:
        try:
            user_word = input('Random word or multiple words divided by space.\n'
                              'All letters should be lower case and no digits.')
            for i in user_word:
                if i.isupper():
                    raise ValueError
                if i.isdigit():
                    raise ValueError
            print(f"Your word or words with the first letter(s) turned into upper case {user_word.title()}")
            break
        except ValueError:
            print('All letters should be lower case. Please, try again.')


edit()


# ******************************************************************************************************************
# решение с ручным вводом при вызове функции. также работает и для одного слова и для нескольких


def edit(user_word):
    try:
        for i in user_word:
            if i.isupper():
                raise ValueError
            if i.isdigit():
                raise ValueError
        print(f"Your word or words with the first letter(s) turned into upper case {user_word.title()}")
    except ValueError:
        print('All letters should be lower case. Please, try again.')


edit('this is sparta')


