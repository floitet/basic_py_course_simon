

def summ():
    last_result = 0
    announce = input('Now you will be asked to insert a line of numbers.\n'
                     'To end this script you just need to insert any letter or special symbol.\n'
                     'Press "Enter" to continue.')
    while True:
        try:
            global user_numbers
            user_input = (input('Any numbers divided by space').split())
            user_numbers = []
            for i in user_input:
                user_numbers.append(int(i))
            result = sum(user_numbers) + last_result
            print(f'All the numbers summed up equal {result}')
            last_result = result
        except ValueError:
            result = sum(user_numbers) + last_result
            print(f'All the numbers (typed in before letter or special symbol) summed up equal {result}')
            print('End of script.')
            break


summ()

