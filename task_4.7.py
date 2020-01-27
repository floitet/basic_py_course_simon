
# вывод всех чисел и их факториалов до числа переданного параметром в функцию


def fact(n):
    result = 1
    yield f"For {result} factorial equals {result}"
    for i in range(1, n):
        result = result * (i + 1)
        yield f"For {i + 1} factorial equals {result}"


for el in fact(int(input('Last number of your factorial sequence.'))):
    print(el)

# ******************************************************************************************************************
# вывод всех чисел до предпоследнего и последний результат отельно


def fact(n):
    result = 1
    yield f"For {result} factorial equals {result}"
    for i in range(1, n):
        result = result * (i + 1)
        if (i + 1) != n:
            yield f"For {i + 1} factorial equals {result}"
        else:
            pass
    yield f"So the final result, factorial of {i + 1}, is {result}."


for el in fact(int(input('Last number of your factorial sequence.'))):
    print(el)




