
# Task 5.3
# решение без словаря, фактически - этот скрипт решает задачу,
# но не дает возможности дальше удобно работать с данными
with open('text_3.txt', 'r') as f:
    lines = f.readlines()
    print('Here is the list of employees with salaries lower than 20k:')
    for i in lines:
        if float(i[i.find(' ') + 1:-1]) < 20000:
            print(i[:i.find(' ')])
    salaries_list_all = [float(i[i.find(' ') + 1:-1]) for i in lines]
    print(f'And here is the average salary for one employee {sum(salaries_list_all) / len(salaries_list_all)}')

# решение со словарем для удобства дальнейшей работы

with open('text_3.txt', 'r') as f:
    lines = f.readlines()
    salaries_dict_all = {i[:i.find(' ')]: float(i[i.find(' ') + 1:-1]) for i in lines}
    print('Here is the list of employees with salaries lower than 20k:')
    for el, val in salaries_dict_all.items():
        if val < 20000:
            print(el)
    print(f'And here is the average salary for one employee '
          f'{sum(salaries_dict_all.values()) / len(salaries_dict_all.values())}')

