"""
Подключаемся к ЯНДЕКС ДИСКУ.
Получаем список файлов упорядоченных по алфавиту

"""

import json
import requests

# Получаем токен для активации на яндекс диске.
with open('tok_yan.json')as file:
    token = json.load(file)


class Get_files:
    def __init__(self, tok, path):
        # Заполняем Заголовки и параметры.
        self.header = tok  # Токен авторизации.
        self.param = {'fields': path}  # Каталог по которуму получаем информаци.
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/files?'
        self.accomplishment()

    def accomplishment(self):
        # Отпарвляем команду на выполнение.
        answer = requests.get(url=self.url, headers=self.header, params=self.param)
        if answer.status_code == 200:  # Команда выполнена успешно.
            # Через цикл выводим нужную нам информацию.
            for i in answer.json()['items']:
                print(f'Тип :{i["type"]}, имя: {i["name"]}')


if __name__ == '__main__':
    Get_files(token, '/')