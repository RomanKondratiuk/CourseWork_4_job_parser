import json
import os.path


class Json_server:
    """ Класс для записи вакансий в json файл"""
    def __init__(self, file_name):
        self.file_name = file_name

    def insert_vacancies(self, data):

        file_path = os.path.join('src', self.file_name)

        data_dict = [vacancy.__dict__ for vacancy in data]
        with open(file_path, 'w') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=6)
