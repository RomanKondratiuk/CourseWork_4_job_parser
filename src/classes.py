from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy
import requests
import pprint
from src.Json_vacansies import Json_server


class Engine(ABC):
    """ абстрактный класс для работы с API сайтов с вакансиями """

    @abstractmethod
    def get_requests(self, url):
        pass

    @abstractmethod
    def get_vacancies(self, key_word):
        pass


class HeadHunterAPI(Engine):
    """
    Класс для работы с API HeadHunter
    """

    def get_requests(self, text):
        # headers = {"User-Agent": "Vacancies_ParserApp/1.0"}
        headers = {"User-Agent": "MyApp/1.0"}
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
            #description = vacancy['name']
            vacancies_hh.append(Vacancy(name, url, salary_min, salary_max))
        return vacancies_hh


class SuperJobAPI(Engine):
    """
    Класс для работы с API SuperJob
    """

    def get_requests(self, text):
        headers = {
            "X-Api-App-Id": 'v3.r.131353004.e21dd97ef97560b801e7271bf8905da1c7a47507.49f112449b3e8ab49b088918966d1feb87cbac16'
        }
        params = {
            "text": text.lower(),
            # "area": 2,
            # "town": 5
        }
        url = "https://api.superjob.ru/2.0/vacancies/"

        response_sj = requests.get(url, headers=headers, params=params)
        return response_sj

    def get_vacancies(self, text: str):
        data = self.get_requests(text).json()['objects']
        # d = []
        # for i in data:
        #     print(i)
        #     d.append(i)
        #     print("---------")
        # print(len(d))

        vacancies_sj = []

        for vacancy in data:

            name = vacancy['profession']
            url = vacancy['link']
            salary_min = vacancy['payment_from']
            salary_max = vacancy['payment_to']
            vacancies_sj.append(Vacancy(name, url, salary_min, salary_max))
        return vacancies_sj

