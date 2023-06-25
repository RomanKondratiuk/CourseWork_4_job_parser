import json

from src.Json_vacansies import Json_server
from src.classes import HeadHunterAPI, SuperJobAPI
from src.filter_vacancies import filtered_vacancies_by_salary

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()


def user_interaction():
    """ Функция для взаимодействия с пользователем через консоль"""

    filter_vacancies = str(input('Введите ключевое слово для фильтрации вакансий: '))
    platform_selection = input('Выберите платформу для поиска вакансий: 1 = "HeadHunter", 2 = "SuperJob":  ')
    print("Загрузка вакансий...")
    if platform_selection == '1':

        vacancies_from_head_hunter = hh_api.get_vacancies(filter_vacancies)

        json_save = Json_server('vacancies_from_head_hunter.json')  # сохранение вакансий в json файл
        json_save.insert_vacancies(vacancies_from_head_hunter)

        list_count = []
        for vacancies in vacancies_from_head_hunter:

            list_count.append(vacancies)
            print(vacancies)

        print(f"Предсталено {len(list_count)} вакансий!")

        print("Если хотите отсортировать данные по зарплате и вывести топ 5 вакансий нажмите: 1, если нет: 2")
        user_input = int(input())
        if user_input == 1:
            filtered_data = filtered_vacancies_by_salary('vacancies_from_head_hunter.json')
            print(filtered_data)
        else:
            return

    elif platform_selection == '2':
        vacancies_from_super_job = superjob_api.get_vacancies(filter_vacancies)

        json_save = Json_server('vacancies_from_super_job.json')  # сохранение вакансий в json файл
        json_save.insert_vacancies(vacancies_from_super_job)

        list_count = []
        for vacancies in vacancies_from_super_job:
            list_count.append(vacancies)
            print(vacancies)
        print(f"Предсталено {len(list_count)} вакансий!")

        print("Если хотите отсортировать данные по зарплате и вывести топ 5 вакансий нажмите: 1, если нет: 2")
        user_input = int(input())
        if user_input == 1:
            filtered_data = filtered_vacancies_by_salary('vacancies_from_super_job.json')
            print(filtered_data)
        else:
            return
    else:
        raise PermissionError(f"Эта платформа не представлена в списке доступных!")


if __name__ == "__main__":
    user_interaction()