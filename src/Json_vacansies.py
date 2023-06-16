import json


class Json_server:
    def __init__(self, file_name):
        self.file_name = file_name

    def insert_vacansies(self, data):
        data_dict = [vacancy.__dict__ for vacancy in data]
        with open(self.file_name, 'w') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=6)
