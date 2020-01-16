message = input("It is online account manager script.\n"
                "It will provide you with some info on your company's cash flow.\n"
                "Press Enter to continue.")
income = int(input("Type in your company's income."))
outcome = int(input("Type in your company's outcome."))

if income > outcome:
    message = input('Your company is making some profit here. Great job!\n'
                    'Let me count your Return on Revenue rate in %.\n'
                    'Press Enter to continue.')
    return_on_revenue = income / outcome * 100
    if return_on_revenue >= 200:
        print(f"Your Return on Revenue rate is {return_on_revenue}%.\n"
              "You did a good job, it is highly acceptable result!")
    elif return_on_revenue >= 150:
        print(f"Your Return on Revenue rate is {return_on_revenue}%. It's not that bad, but could be higher.")
    else:
        print(f"Your Return on Revenue rate is {return_on_revenue}%. It's not that well.\n"
              "But at least you are running a profitable business!")
    employees = int(input("How many employees do work for your company?"))
    income_on_emp = income / employees
    print(f'OK, great! Your average income on one employee equals {income_on_emp}$.')

if outcome > income:
    print('Your company suffers some losses. You need to take some steps to resolve it!')
