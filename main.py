from src.Json_vacansies import Json_server
from src.classes import HeadHunterAPI, SuperJobAPI

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()


def user_interaction():
    """ Функция для взаимодействия с пользователем через консоль"""

    filter_vacancies = str(input('Введите ключевое слово для фильтрации вакансий: '))
    platform_selection = input('Выберите платформу для поиска вакансий: 1 = "HeadHunter" или 2 = "SuperJob": ')
    print("Загрузка вакансий...")
    if platform_selection == '1':
        vacancies_from_head_hunter = hh_api.get_vacancies(filter_vacancies)
        list_count = []
        for vacancies in vacancies_from_head_hunter:

            json_save = Json_server('vacancies_from_head_hunter.json') # сохранение вакансий в json файл
            json_save.insert_vacancies(vacancies_from_head_hunter)

            list_count.append(vacancies)
            print(vacancies)

        print(f"Предсталено {len(list_count)} вакансий!")
    elif platform_selection == '2':
        vacancies_from_super_job = superjob_api.get_vacancies(filter_vacancies)
        list_count = []
        for vacancies in vacancies_from_super_job:

            json_save = Json_server('vacancies_from_super_job.json') # сохранение вакансий в json файл
            json_save.insert_vacancies(vacancies_from_super_job)

            list_count.append(vacancies)
            print(vacancies)
        print(f"Предсталено {len(list_count)} вакансий!")
    else:
        print("Эта платформа не представлена в списке доступных!")


if __name__ == "__main__":
    user_interaction()

