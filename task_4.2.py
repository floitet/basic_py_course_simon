# вариант с вводом пользователя, составлением рандомного списка и обработкой исключений,
# само решение через генератор в одну строку

from random import randint


try:
    amount_num = int(input('How many numbers do you want in this testing list?'))
    range_num = input('In what range do you want them to be? Type in 2 numbers.').split()
    range_num = [int(i) for i in range_num]
    for i in range_num:
        if range_num.index(i) > 1:
            raise TypeError
        if i <= 0:
            raise TypeError
        if range_num[0] >= range_num[1]:
            raise AttributeError
    orig_list = [randint(range_num[0], range_num[1]) for el in range(amount_num)]
    print(orig_list)
except ValueError:
    print('Need numbers. Try again.')
except TypeError:
    print('Need only two numbers. And they should be > 0. Really sorry, '
          'but we can not build a range starting from negative number or 0 '
          'as well as range for 3 numbers is impossible.')
except AttributeError:
    print('Number 1 should be < than number 2. Please, try again.')
try:
    new_list = [el for el in orig_list if el > orig_list[(orig_list.index(el) - 1)] and orig_list.index(el) > 0]
    print(new_list)
except NameError:
    pass


