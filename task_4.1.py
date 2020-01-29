from sys import argv

try:
    script_name, employees_name, amount_hours, hour_rate, bonus = argv
    for i in employees_name:
        if i.isdigit():
            raise ValueError
    print(f"{employees_name}'s salary for this month equals {(int(amount_hours) * int(hour_rate)) + int(bonus)}")
except ValueError:
    print('First parameter should be name and 3 other should be numbers.')


