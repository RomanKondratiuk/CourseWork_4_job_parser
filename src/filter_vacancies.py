import json


def filtered_vacancies_by_salary(file_path):
    with open(file_path) as file:
        data = json.load(file)
        filtered_data = sorted(
            (item for item in data if item.get('salary_max') is not None and item.get('salary_max') != 0),
            key=lambda x: x['salary_max'],
            reverse=True
        )

        return filtered_data[:5]


# print(filtered_vacancies_by_salary())
#
# json_file_path = "vacancies_from_head_hunter.json"
# filtered_data = filtered_vacancies_by_salary(json_file_path)


# count_list = 0
#
# for item in filtered_data:
#     print(item['salary_max'])
#     count_list += 1
#
# print(f"количество вакансий: {count_list}")
