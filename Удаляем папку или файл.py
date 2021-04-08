"""
Подклбчаемся к ЯНДЕКС ДИСКУ и
удаляем папку или файл.
Чтобы удалить ресурс не помещая в корзину, следует указать параметр permanently=true.
"""

import json
import requests


# Получаем токен для активации на яндекс диске.
with open('tok_yan.json')as file:
    token = json.load(file)


class Delete_file_catalog:
    def __init__(self, tok, path):
        # Заполняем Заголовки и параметры.
        self.header = tok
        self.param = {'path': path,  # Папка или файл который нужно удалить
                      'permanently': True}  # Чтобы удалить ресурс не помещая в корзину
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources?'
        self.accomplishment()

    def accomplishment(self):
        # Отпарвляем команду на выполнение.
        answer = requests.delete(url=self.url, headers=self.header, params=self.param)
        if answer.status_code == 204:  # Команда выполнена успешно.
            print('Элемент удален')
        else:
            print(answer.json()["message"])


if __name__ == '__main__':
    Delete_file_catalog(token, '/pyt')