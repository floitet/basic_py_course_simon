
# Task 5.2
# скрипт находит именно слова, отбрасывая числа и знаки препинания вроде "-"
# + записывает все данные в словарь для дальнейшей работы
with open('text_1.txt', 'r') as f:
    lines = f.readlines()
    dict_info = {}
    print(f'Your file contains {len(lines)} lines in total.')
    for line in lines:
         for i in line.split():
           words_list = [i for i in line.split() if i.isalpha()]
         print(f'Line #{lines.index(line) + 1} contains {len(words_list)} word(s).')
         dict_info[f'Line {lines.index(line) +1}'] = len(words_list)
    print(f'Here is your dictionary with all the info:\n{dict_info}.\nYou can work with this data later on.')

