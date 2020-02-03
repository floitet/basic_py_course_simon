
translate_dict = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре"
}

# чтение всего сразу и потом запись с переводом

with open('text_4.txt', 'r') as f:
    oper_list = f.readlines()
with open('text_file_2.1.txt', 'w') as f:
    for i in oper_list:
        f.write(f'{translate_dict[i[:i.find(" ")]]} - {i[i.find(" ") + 3]}\n')

# решение с построчным чтением и тут же переводом + записью в список
with open('text_4.txt', 'r') as numbers_f:
    write_list = [f'{translate_dict[i[:i.find(" ")]]} - {i[i.find(" ") + 3]}\n' for i in numbers_f]
with open('text_file_2.2.txt', 'w') as f:
    f.writelines(write_list)

