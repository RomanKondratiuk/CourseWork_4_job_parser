

class Vacancy:
    def __init__(self, title, url, description, salary_min, salary_max):
        self.title = title
        self.url = url
        self.description = description
        self.salary_min = salary_min
        self.salary_max = salary_max

    def __repr__(self):
        return f""" ------------
Название: {self.title},
Ссылка: {self.url},
Должность: {self.description},
Минимальная зарплата: {self.salary_min},
Максимальная запрлата: {self.salary_max}
"""


