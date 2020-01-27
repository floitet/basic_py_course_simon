# вариант с вводом пользователя, составлением рандомного списка и обработкой исключений,
# само решение через генератор в одну строку

from random import randint
try:
    amount_num = int(input('How many numbers do you want in this testing list?'))
    range_num = input('In what range do you want them to be? Your range should not be longer than 10 numbers.').split()
    range_num = [int(i) for i in range_num]
    for i in range_num:
        if range_num.index(i) > 1:
            raise TypeError
        if i <= 0:
            raise TypeError
        if range_num[1] - range_num[0] > 10:
            raise AttributeError
        if range_num[0] >= range_num[1]:
            raise AttributeError
    orig_list = [randint(range_num[0], range_num[1]) for el in range(amount_num)]
    print(orig_list)
except ValueError:
    print('Need numbers. Try again.')
except TypeError:
    print('Need only two numbers. And they should be > 0. Really sorry, '
          'but we can not build range from negative numbers or 0 as well as range for 3 numbers.')
except AttributeError:
    print('We need the range to be no longer than 10. And number 1 should be < than number 2.')

try:
    new_list = [el for el in orig_list if orig_list.count(el) == 1]
    print(new_list)
except NameError:
    pass


