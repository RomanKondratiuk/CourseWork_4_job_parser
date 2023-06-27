import json
from src.vacancy import Vacancy


def filtered_vacancies_by_salary(file_path):
    with open(file_path) as file:
        data = json.load(file)
        filtered_data = sorted(
            (item for item in data if item.get('salary_max') is not None and item.get('salary_max') != 0),
            key=lambda x: x['salary_max'],
            reverse=True
        )

        top_5_vacancies = filtered_data[:5]
        top_5_vacancies_filter = []

        for i, vacancy in enumerate(top_5_vacancies, start=1):

            name = vacancy['title']
            url = vacancy['url']
            salary_min = vacancy['salary_min']
            salary_max = vacancy['salary_max']

            top_5_vacancies_filter.append(f"Топ {i} вакансия: зарплата = {vacancy['salary_max']}!")
            top_5_vacancies_filter.append(Vacancy(name, url, salary_min, salary_max))

        return top_5_vacancies_filter





