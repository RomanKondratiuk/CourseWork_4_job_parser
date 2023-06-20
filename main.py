from src.Json_vacansies import Json_server
from src.classes import HeadHunterAPI, SuperJobAPI

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()


def user_interaction():
    filter_vacancies = str(input('Введите ключевое слово для фильтрации вакансий: '))
    platform_selection = input('Выберите платформу для поиска вакансий: 1 = "HeadHunter" или 2 = "SuperJob": ')
    print("Загрузка вакансий...")
    if platform_selection == '1':
        vacancies_hh = hh_api.get_vacancies(filter_vacancies)
        for vacancies in vacancies_hh:
            print(vacancies)
    elif platform_selection == '2':
        vacancies_sj = superjob_api.get_vacancies(filter_vacancies)
        for vacancies in vacancies_sj:
            print(vacancies)
    else:
        print("Эта платформа не представлена в списке доступных!")


if __name__ == "__main__":
    user_interaction()

# hh_api = HeadHunterAPI()
# vacansies = hh_api.get_vacancies('python')
# for vacancy in vacansies:
#     print(vacancy)
# json_save = Json_server('vacansis.json')
# json_save.insert_vacansies(vacansies)

#
# superjob_api = SuperJobAPI()
# vacancies = superjob_api.get_vacancies('Python')
# for vacancy in vacancies:
#     print(vacancy)
#
# json_save = Json_server('vacancies.json')
# json_save.insert_vacansies(vacancies)
#
#
#
#
#
