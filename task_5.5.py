
from random import randint
# создание списка рандомных длинны и набора чисел + запись его в файл с пробелами между числами в одну строку
with open('text_5.txt', 'w') as f:
    rand_list = [randint(1, 100) for i in range(randint(1, 20))]
    f.writelines(str(rand_list).replace(", ", " ")[1:-1])
# чтение из файла и подсчет суммы
with open('text_5.txt', 'r') as f:
    numbers_line = list(f.read().split())
    numbers_line = [int(i) for i in numbers_line]
    print(f'All the numbers in list summed up equal: {sum(numbers_line)}')

