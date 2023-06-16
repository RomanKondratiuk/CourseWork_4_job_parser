import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    # атрибуты класса
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        # инициализатор класса
        self._channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        dictionary = self.channel
        self.id = dictionary['items'][0]['id']
        self.title = dictionary['items'][0]['snippet']['title']
        self.description = dictionary['items'][0]['snippet']['description']
        self.url = dictionary['items'][0]['snippet']['thumbnails']['high']['url']
        self.subscriberCount = dictionary['items'][0]['statistics']['subscriberCount']
        self.video_count = dictionary['items'][0]['statistics']['videoCount']
        self.viewCount = dictionary['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f" {self.title}, ({self.url})"

    def __add__(self, other):
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        return int(self.subscriberCount) - int(other.subscriberCount)
        return int(other.subscriberCount) - int(self.subscriberCount)

    def __gt__(self, other):
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __ge__(self, other):
        return int(self.subscriberCount) >= int(other.subscriberCount)

    def __lt__(self, other):
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __le__(self, other):
        return int(self.subscriberCount) <= int(other.subscriberCount)

    def __eq__(self, other):
        return int(self.subscriberCount) == int(other.subscriberCount)



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """метод to_json(), сохраняющий в файл значения атрибутов экземпляра Channel"""
        data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriberCount,
            "video_count": self.video_count,
            "viewCount": self.viewCount
        }
        with open(file_name, "w") as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            return data

    @classmethod
    def get_service(cls):
        """класс-метод возвращающий объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    @property
    def channel_id(self):
        return self._channel_id

#d = {'kind': 'youtube#videoListResponse', 'etag': 'k8hB_aVqirfJl-rvRpoOv0-_KwU', 'items': [{'kind': 'youtube#video', 'etag': '4ys_pYZ1xq17YAqAGgwrw576Fy4', 'id': 'udsgzdZw5zU', 'snippet': {'publishedAt': '2023-05-31T16:03:36Z', 'channelId': 'UC9XJvt8OT-9_8QHDBdqocaw', 'title': 'Сергей Орлов vs SQWOZ BAB - Кто заберёт ФЕРРАРИ? 5 выпуск', 'description': 'Зови друзей и получай по 1000 ₽ — https://tinkoffbank.onelink.me/1923863684/1dfmpr0g\n\nСмотри эксклюзивные шоу с топовыми блогерами на любые тематики. Открывай новое в Дзене! https://vk.cc/cotief\n\nЗа машиной иди на Дром\nhttps://drom.ru/s/lW9 🚗\nИ найдешь там любую тачку!\n\nРеклама. АО "Тинькофф Банк", erid: Kra23kPMv\nРеклама. ООО "Дзен.Платформа". ИНН: 7704431373. токен 2VtzqvLF3tuс\nРеклама. ООО "АМАЯМА АВТО, erid: Kra23dMTz\n\nПо вопросам рекламы, сотрудничества: DubrovskiySyndicate@mail.ru\n\nПОПАСТЬ К НАМ НА ШОУ:\nhttps://youtu.be/wIZdWFt57Jg\n\nАренда авто: https://dubrovskiy-syndicate.com/rent\n---\nВКонтакте: http://vk.com/zheki444\nТелеграм: https://t.me/dubrovskiy_444\n---\nОсновной канал: http://youtube.com/c/ЖекичДубровский\nАвтосалон: http://youtube.com/c/АвтосалонСиндиката\nМастерская: http://youtube.com/c/МастерскаяСиндиката\nДжентльмены: http://youtube.com/c/ДжентльменыСиндиката\nДевчонки: http://youtube.com/c/ДевчонкиСиндиката\nВертикальный: http://youtube.com/c/ВертикальныйСиндикат\nИгры: http://youtube.com/c/ИгрыСиндиката\nФОРСАЖ: https://www.youtube.com/@forsazh\n---\nМузыка из видео: https://vk.com/motorheartstudio\n\n#ДубровскийСиндикат', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/udsgzdZw5zU/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/udsgzdZw5zU/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/udsgzdZw5zU/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/udsgzdZw5zU/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/udsgzdZw5zU/maxresdefault.jpg', 'width': 1280, 'height': 720}}, 'channelTitle': 'Жекич Дубровский', 'categoryId': '2', 'liveBroadcastContent': 'none', 'localized': {'title': 'Сергей Орлов vs SQWOZ BAB - Кто заберёт ФЕРРАРИ? 5 выпуск', 'description': 'Зови друзей и получай по 1000 ₽ — https://tinkoffbank.onelink.me/1923863684/1dfmpr0g\n\nСмотри эксклюзивные шоу с топовыми блогерами на любые тематики. Открывай новое в Дзене! https://vk.cc/cotief\n\nЗа машиной иди на Дром\nhttps://drom.ru/s/lW9 🚗\nИ найдешь там любую тачку!\n\nРеклама. АО "Тинькофф Банк", erid: Kra23kPMv\nРеклама. ООО "Дзен.Платформа". ИНН: 7704431373. токен 2VtzqvLF3tuс\nРеклама. ООО "АМАЯМА АВТО, erid: Kra23dMTz\n\nПо вопросам рекламы, сотрудничества: DubrovskiySyndicate@mail.ru\n\nПОПАСТЬ К НАМ НА ШОУ:\nhttps://youtu.be/wIZdWFt57Jg\n\nАренда авто: https://dubrovskiy-syndicate.com/rent\n---\nВКонтакте: http://vk.com/zheki444\nТелеграм: https://t.me/dubrovskiy_444\n---\nОсновной канал: http://youtube.com/c/ЖекичДубровский\nАвтосалон: http://youtube.com/c/АвтосалонСиндиката\nМастерская: http://youtube.com/c/МастерскаяСиндиката\nДжентльмены: http://youtube.com/c/ДжентльменыСиндиката\nДевчонки: http://youtube.com/c/ДевчонкиСиндиката\nВертикальный: http://youtube.com/c/ВертикальныйСиндикат\nИгры: http://youtube.com/c/ИгрыСиндиката\nФОРСАЖ: https://www.youtube.com/@forsazh\n---\nМузыка из видео: https://vk.com/motorheartstudio\n\n#ДубровскийСиндикат'}, 'defaultAudioLanguage': 'ru'}, 'contentDetails': {'duration': 'PT55M36S', 'dimension': '2d', 'definition': 'hd', 'caption': 'false', 'licensedContent': True, 'contentRating': {}, 'projection': 'rectangular'}, 'statistics': {'viewCount': '1032699', 'likeCount': '68493', 'favoriteCount': '0', 'commentCount': '2419'}, 'topicDetails': {'topicCategories': ['https://en.wikipedia.org/wiki/Lifestyle_(sociology)', 'https://en.wikipedia.org/wiki/Vehicle']}}], 'pageInfo': {'totalResults': 1, 'resultsPerPage': 1}}

