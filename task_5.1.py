
# вариант с записью в файл по одной строке
with open('text_1.txt', 'w') as f:
    announce = input('This script allows you to write text lines into a file.\n'
                     'To END this script leave your input line EMPTY.')
    while True:
        user_writes = input('Your line of text:')
        f.write(f"{user_writes}\n")
        if bool(user_writes) is False:
            break

# вариант с созданием списка и дальнейшей записью этого списка в файл
user_writes_list = []
announce = input('This script allows you to write text lines into a file.\n'
                 'To END this script leave your input line EMPTY.')
while True:
    user_writes = input('Your line of text:')
    if bool(user_writes) is False:
        break
    else:
        user_writes += '\n'
        user_writes_list.append(user_writes)

with open('text_1.txt', 'w') as f:
    f.writelines(user_writes_list)

