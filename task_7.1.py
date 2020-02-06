# Task 7.1
import random

# можно менять количество строк и рядов
# скрипт будет создавать два списка списков с рандомными числами в нужном количестве


lines = 10
num_in_line = 10
sample_list = [random.sample(range(100), num_in_line) for i in range(lines)]
sample_list2 = [random.sample(range(100), num_in_line) for i1 in range(lines)]


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):

        for i in self.matrix_list:
            line = f'| '
            for k in i:
                line += f'{str(k):3} '
            line += ' |'
            print(line)

        return f'Here is your matrix.'

    # при суммировании матриц создается новая переменная,
    # с помощью которой затем создается новый экземпляр класса Matrix
    # суммирование происходит с помощью двух генераторов в одну строчку

    def __add__(self, other):
        new_matrix = [[x + y for x, y in zip(i, k)] for i, k in zip(self.matrix_list, other.matrix_list)]
        return Matrix(new_matrix)


a = Matrix(sample_list)
b = Matrix(sample_list2)
print(a.matrix_list)
print(b.matrix_list)
print(a)
print(b)
c = (a + b)
print(c)
