from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy
import requests
import pprint
from src.Json_vacansies import Json_server


class Engine(ABC):
    """ абстрактный класс для работы с API сайтов с вакансиями """

    # def __init__(self):
    #     self.url = "https://api.hh.ru/vacancies"

    @abstractmethod
    def get_requests(self, url):
        pass
        # self.url = "https://api.hh.ru/vacancies"

    @abstractmethod
    def get_vacancies(self, key_word):
        pass


class HeadHunterAPI(Engine):
    """
    Класс для работы с API HeadHunter
    """

    def get_requests(self, text):
        headers = {"User-Agent": "Vacancies_ParserApp/1.0"}
        params = {
            "text": text.lower(),
            "area": 1
        }
        url = "https://api.hh.ru/vacancies"
        response_hh = requests.get(url, headers=headers, params=params)
        return response_hh

    def get_vacancies(self, text: str):

        data = self.get_requests(text).json()['items']

        vacancies_hh = []
        for vacancy in data:

            name = vacancy['name']
            url = vacancy['alternate_url']
            if vacancy['salary']:
                salary_min = vacancy['salary']['from']
                salary_max = vacancy['salary']['to']
            else:
                salary_min = None
                salary_max = None
            description = vacancy['name']
            vacancies_hh.append(Vacancy(name, url, description, salary_min, salary_max))
        return vacancies_hh
        #print(vacancies_hh)


class SuperJobAPI(Engine):
    """
    Класс для работы с API SuperJob
    """

    # def __init__(self, url):
    #     self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, keyword: str):

        headers = {
            "X-Api-App-Id": 'v3.r.131353004.e21dd97ef97560b801e7271bf8905da1c7a47507.49f112449b3e8ab49b088918966d1feb87cbac16'
        }
        params = {
            "keywords": keyword.lower(),
            "town": 4
        }

        response_sj = requests.get(self.url, headers=headers, params=params)
        data = response_sj.json()
        return data


# hh_api = HeadHunterAPI()
# vacansis = hh_api.get_vacancies('Python')
# for vacancy in vacansis:
#    print(vacancy)
# json_save = Json_server('vacansis.json')
# json_save.insert_vacansies(vacansis)
# #pprint.pprint(hh_api.get_vacancies('python'))

# class SuperJobAPI(Engine):
#     pass
#
#
# def get_requests(self):
#
#     response = requests.get(self.url, headers=self.headers, params=self.params)
#     if response.status_code != 200:
#         raise PermissionError(f"Ошибка получения вакансий!")
#     return response.json()
#     print(response.json())
#
# get_requests()



   # def get_vacancies_lis
# sj_api = SuperJobAPI("https://api.superjob.ru/2.0/vacancies/")
# pprint.pprint(sj_api.get_vacancies('python'))


print("""
    def get_requests(self, text):
        headers = {"User-Agent": "Vacancies_ParserApp/1.0"}
        params = {
            "text": text.lower(),
            "area": 1
        }
        url = "https://api.hh.ru/vacancies"
        response_hh = requests.get(url, headers=headers, params=params)
        return response_hh""")