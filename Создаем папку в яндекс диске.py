"""

Подключаемся к ЯНДЕКС ДИСКУ
и создаем папку импользуея метод PUT

"""
import json
import requests


# Получаем токен для активации на яндекс диске.
with open('tok_yan.json')as file:
    token = json.load(file)


class New_catalog:
    def __init__(self, tok, path):
        # Заполняем Заголовки и параметры.
        self.header = tok  # Токен авторизации.
        self.param = {'path': path}  # Имя создаваемого каталога.
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources?'
        self.accomplishment()

    def accomplishment(self):
        # Отпарвляем команду на выполнение.
        answer = requests.put(url=self.url, headers=self.header, params=self.param)
        if answer.status_code == 201:  # Команда выполнена успешно.
            print('Папка создана.')
        else:
            print(answer.json()["message"])


if __name__ == '__main__':
    New_catalog(token, 'pyt')