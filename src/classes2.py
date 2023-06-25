import json
import pprint

# with open('vacansis.json') as file:
#     data = json.load(file)
#
#     # print(data)
#
#     value = data[1]['title']
#     print(value)


with open('vacancies_from_head_hunter.json') as file:
    data = json.load(file)

    print(data[1]['title'])

