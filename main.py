from src.Json_vacansies import Json_server
from src.classes import HeadHunterAPI, SuperJobAPI

# hh_api = HeadHunterAPI()
# vacansis = hh_api.get_vacancies('Python')
# for vacancy in vacansis:
#     print(vacancy)
# json_save = Json_server('vacansis.json')
# json_save.insert_vacansies(vacansis)


superjob_api = SuperJobAPI()
vacansis = hh_api.get_vacancies('Python')
for vacancy in vacansis:
    print(vacancy)
json_save = Json_server('vacansis.json')
json_save.insert_vacansies(vacansis)





