
# решение только через list

user_input_month = int(input('Type in month of your birth in mm format.'))
list_seasons = [['winter', 12, 1, 2], ['spring', 3, 4, 5], ['summer', 6, 7, 8], ['fall', 9, 10, 11]]

for i in list_seasons:
    if user_input_month in list_seasons[list_seasons.index(i)]:
        print(f'You were born in {list_seasons[list_seasons.index(i)][0]}')
        break


# решение через list + dict

user_input_month = int(input('Type in month of your birth in mm format.'))
seasons_months = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'fall': [9, 10, 11]
}

for key, val in seasons_months.items():
    if user_input_month in val:
        print(f'You were born in {key}.')
        break


