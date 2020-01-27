
import random
from itertools import cycle, count
from sys import argv

# совокупность

script_name, line_start, line_finish, repeat = argv

orig_list = []
for el in count(int(line_start), 1):
    if el > int(line_finish):
        break
    else:
        orig_list.append(el)

c = 0
for el in cycle(orig_list):
    print(el)

    if orig_list.index(el) + 1 == len(orig_list):
        c += 1
    if c == int(repeat):
        break


# ******************************************************************************************************************
# тоже самое + shuffle


# script_name, line_start, line_finish, repeat = argv
#
# orig_list = []
# for el in count(int(line_start), 1):
#     if el > int(line_finish):
#         break
#     else:
#         orig_list.append(el)
#
# c = 0
# operating_list = []
# for el in cycle(orig_list):
#     operating_list.append(el)
#     if orig_list.index(el) + 1 == len(orig_list):
#         c += 1
#     if c == int(repeat):
#         break
# print(operating_list)
# random.shuffle(operating_list)
# print(operating_list)