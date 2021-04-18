"""
Подключаемся к ЯНДЕКС ДИСКУ
заггужаем файлы в пределеную папку по URL

"""

import json
import requests


# Получаем токен для активации на яндекс диске.
with open('tok_yan.json')as file:
    token = json.load(file)


class Loading_url:
    def __init__(self, tok, path, yyyy):
        # Заполняем Заголовки и параметры.
        self.header = tok  # Токен авторизации.
        self.param = {'path': path,  # Путь для загрузки
                      'url': yyyy}  # URL файл для загрузки.
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?'
        self.accomplishment()

    def accomplishment(self):
        # Отпарвляем команду на выполнение.
        answer = requests.post(url=self.url, headers=self.header, params=self.param)
        if answer.status_code == 202:  # Команда выполнена успешно.
            print('Файл загружен успешно.')
        else:
            print(answer.json()["message"])


if __name__ == '__main__':
    ooo = 'https://vvphoto.ru/wp-content/uploads/2015/03/n14_4751.jpg'
    Loading_url(token, '/d.jpg', ooo)