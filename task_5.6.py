# Task 5.6
# решение с чтением всего сразу и получением вложенных списков в числами записанными как строки
# - потом переводом элементов вложенных списков в числа - затем генератором словарей

import re
with open('text_6.txt', 'r') as f:
    lines = f.readlines()
    new_list = [re.findall(r'\d+', i) for i in lines]

    def convert_to_integer(l, func=lambda x: int(x)):
        for n, i in enumerate(l):
            if type(i) != list:
                l[n] = func(i)
            else:
                convert_to_integer(i)
        return l

    convert_to_integer(new_list)
    classes_dict = {i[:i.find(':')]: sum(new_list[lines.index(i)]) for i in lines}
    print(classes_dict)

# решение с построчным чтением + сразу же переводом в число + сразу же записью в заранее созданный словарь
with open('text_6.txt', 'r') as f:
    classes_dict = {}
    for line in f:
        oper_list = []
        for i in re.findall(r'\d+', line):
            i = int(i)
            oper_list.append(i)
        classes_dict[line[:line.find(':')]] = sum(oper_list)
print(classes_dict)
