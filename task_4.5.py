
# с помощью функции reduce

from functools import reduce


orig_list = [el for el in range(100, 1001) if el % 2 == 0]
print(orig_list)


def multiply(prev_el, el):
    return prev_el * el


result = reduce(multiply, orig_list)
print(result)

# ******************************************************************************************************************
# вариант без функции reduce

result = 1
for el in range(len(orig_list)):
        result = result * orig_list[el]

print(result)

