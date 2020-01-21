
# решение без range

items_amount = int(input('How many items do you want to add?'))
my_dict = {}
num = 1
list_amount = []
while num <= items_amount:
    list_amount.append(num)
    num += 1
print(list_amount)
for i in list_amount:
    operating_number = i
    item_name = input(f"Insert #{operating_number} item's name")
    item_cost = int(input(f"Insert #{operating_number} item's cost"))
    item_quantity = int(input(f"Insert #{operating_number} item's quantity"))
    item_metrics = input(f"Insert #{operating_number} item's metrics parameter")
    my_dict[operating_number] = {"Name": item_name, "Price": item_cost, "Quantity": item_quantity,
                                 "Metrics": item_metrics}
items_list = list(my_dict.items())
print(f"Here is the list of items grouped for you in the most convenient way {items_list}")

announce = input('And now you will be given some statistics on the items you uploaded to the databse.\n'
                 'All names, prices, quantities and metrics will be grouped together.\n'
                 'Press "Enter" to continue')
analitics_dict = {
    'Name': [],
    'Price': [],
    'Quantity': [],
    'Metrics': []
}

for i in items_list:
    new = items_list[items_list.index(i)][1]
    analitics_dict['Name'].append(new['Name'])
    analitics_dict['Price'].append(new['Price'])
    analitics_dict['Quantity'].append(new['Quantity'])
    if analitics_dict['Metrics'].count(new['Metrics']):
        pass
    else:
        analitics_dict['Metrics'].append(new['Metrics'])

print(analitics_dict)

# ************************************************************************************************************

# Решение с использованием range

# items_amount = int(input('How many items do you want to add?'))
# my_dict = {}
# for i in range(items_amount):
#     operating_number = i + 1
#     item_name = input(f"Insert #{operating_number} item's name")
#     item_cost = int(input(f"Insert #{operating_number} item's cost"))
#     item_quantity = int(input(f"Insert #{operating_number} item's quantity"))
#     item_metrics = input(f"Insert #{operating_number} item's metrics parameter")
#     my_dict[operating_number] = {"Name": item_name, "Price": item_cost, "Quantity": item_quantity,
#                                  "Metrics": item_metrics}
# items_list = list(my_dict.items())
#
# print(f"Here is the list of items grouped for you in the most convenient way {items_list}")
#
# announce = input('And now you will be given some statistics on the items you uploaded to the databse.\n'
#                  'All names, prices, quantities and metrics will be grouped accordingly.\n'
#                  'Press "Enter" to continue')
# analitics_dict = {
#     'Name': [],
#     'Price': [],
#     'Quantity': [],
#     'Metrics': []
# }
#
# for i in items_list:
#     new = items_list[items_list.index(i)][1]
#     analitics_dict['Name'].append(new['Name'])
#     analitics_dict['Price'].append(new['Price'])
#     analitics_dict['Quantity'].append(new['Quantity'])
#     if analitics_dict['Metrics'].count(new['Metrics']):
#         pass
#     else:
#         analitics_dict['Metrics'].append(new['Metrics'])
#
# print(analitics_dict)