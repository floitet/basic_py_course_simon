
user_age = int(input('How old are you?'))
user_name = input("What's your name?")
user_car_check = input('Do you have a car? Type "Y" for "Yes and "N" for "No"')
user_car = None
user_car_exp = None

if user_car_check == "Y":
    user_car = input('What is it? Type in its brand and model')
    user_car_exp = input('How much do you spend monthly on maintaining your car?')
    if user_car_exp.count(",") != 0:
        user_car_exp = user_car_exp.replace(",", ".")
    user_car_exp = float(user_car_exp)

car_survey = [user_age, user_name, user_car, user_car_exp]
for i in car_survey:
    if i == None:
        car_survey.remove(i)
    else:
        print(i)
        print(type(i))
