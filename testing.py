# n = 10
# g = n
# n = 5
# print(n)
# print(g)
#
# n = [1, 2, 3]
# g = n
# n = [1, 2, 3, 4]
# print(n)
# print(g)
#
# n = [1, 2, 3]
# g = n
# n[1] = 3
# print(n)
# print(g)

# n = [1, 2, 3]
# g = n.copy()
# n[1] = 3
# print(n)
# print(g)

# import copy
# n = [1, 2, 3, [1, 2, 3]]
# g = copy.deepcopy(n)
# n[3][1] = 3
# print(n)
# print(g)

from sys import argv

script_name, first_param, second_param, third_param = argv

print("Script name", script_name)
print("Parameter 1", first_param)
print("Parameter 2", second_param)
print("Parameter 3", third_param)