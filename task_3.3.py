# вариант с вводом трех аргументов пользователем + обработкой исключения


def max_sum(num1, num2, num3):
    try:
        max_2 = []
        all_nums = [num1, num2, num3]
        for i in range(2):
            max_2.append(max(all_nums))
            all_nums.pop(all_nums.index(max(all_nums)))

        return sum(max_2)
    except ValueError:
        return "Error. You can add only numbers"


announce = input('Now you will be given three prompt messages asking you to insert number\n.'
                 'Press "Enter" to continue')
print(max_sum(int(input("Any number 1")), int(input("Any number 2")), int(input("Any number 3"))))


# ******************************************************************************************************************
# вариант с любым кол-вом аргументов вводимых пользователем + обработкой исключения (ввод в вызове функции)


def max_two_sum(*args):
    try:
        max_2 = []
        operating_list = []
        for i in args:
            operating_list = i
        operating_list = [int(i) for i in operating_list]
        for i in range(2):
            max_2.append(max(operating_list))
            operating_list.pop(operating_list.index(max(operating_list)))
        return sum(max_2)
    except ValueError:
        return "Error. You can add only numbers"


print(max_two_sum((input('Type in any amount of numbers divided by space').split(" "))))

# ******************************************************************************************************************
# вариант с любым кол-вом аргументов вводимых пользователем + обработкой исключения
# (ввод в список, который потом вставляется в функцию)

user_num_seq = input('Type in any amount of numbers divided by space').split(" ")


def max_two_sum(*operating_list):
    try:
        max_2 = []
        operating_list = [int(i) for i in operating_list]
        for i in range(2):
            max_2.append(max(operating_list))
            operating_list.pop(operating_list.index(max(operating_list)))
        return sum(max_2)
    except ValueError:
        return "Error. You can add only numbers"


print(max_two_sum(*user_num_seq))


