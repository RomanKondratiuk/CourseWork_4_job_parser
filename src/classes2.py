from abc import ABC, abstractmethod
import json
import requests
from src.func import get_currencies


class Engine(ABC):
    pass


    @abstractmethod
    def get_requests(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunder(Engine):

    url = "https://api.hh.ru/vacancies"

    def __init__(self, key_word):
        self.params = {
            'per_page': 100,
            'page': None,
            'text': key_word,
            'archived': False,
        }
        #
        self.headers = {
            'User-Agent': 'My importantApp 1.0'
        }
        self.vacancies = []

    def get_requests(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise PermissionError(f"Ошибка получения вакансий!")
        return response.json()
        print(response.json())


hh = HeadHunder('Python')
print(hh)

    # def get_formatted_vacancies(self):
    #     formatted_vacancies = []
    #     currencies = get_currencies()
    #
    #     for vacancy in self.vacancies:
    #         formatted_vacancy = {
    #             "employer": vacancy['employer']["name"],
    #
    #
    #         }