
# решение с помощь split и проверки isdigit
import json
with open('text_7.txt', 'r') as f:
    companies_dict = {}
    for line in f:
        op_list = [int(i) for i in line.split() if i.isdigit()]
        summary = op_list[0] - op_list[1]
        companies_dict[line[:line.find(" ")]] = summary
    avg_list = [val for el, val in companies_dict.items() if val > 0]
    profit_dict = dict(avg_profit=sum(avg_list) / len(avg_list))
    final_list = [companies_dict, profit_dict]
with open('task_5.7.json', 'w') as f:
    json.dump(final_list, f)

