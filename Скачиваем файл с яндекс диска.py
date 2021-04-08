"""
Подключаемся к яндекс диску
Получаем ссылку на скачивание файла и скачиваем его.

"""

import json
import requests


# Получаем токен для активации на яндекс диске.
with open('tok_yan.json')as file:
    token = json.load(file)


class Download_file:
    def __init__(self, tok, path):
        # Заполняем Заголовки и параметры.
        self.header = tok  # Токен авторизации.
        self.param = {'path': path}  # Указываем путь где находиться файл
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/download?'
        self.accomplishment()

    def accomplishment(self):
        # Отпарвляем команду на выполнение.
        answer = requests.get(url=self.url, headers=self.header, params=self.param)
        if answer.status_code == 200:  # Команда выполнена успешно.
            self.image_url = answer.json()['href']  # Получаем ссылку на скачавание.
            self.download_path = '/Users/dEniS/Downloads/'  # Указываем путь для сохранения файла.
            self.saving_a_file()  # Вызываем метод
        else:
            print(answer.json()["message"])

    def saving_a_file(self):
        # Сохраняем полученый файл.
        try:
            resource = requests.get(self.image_url)  # Получаем картинку.
            with open(f'{self.download_path}/{name_file}', 'wb')as file:  # Указываем путь для загрузки.
                file.write(resource.content)  # Записывает и закрываем файл.
                print('Файл удачно скачан')
        except ValueError:
            pass


if __name__ == '__main__':
    # Укажите, какой файл мы хотим загрузить, и ,
    # указанное имя файла и формат мы используем для его сохранения.
    name_file = 'd.jpg'
    Download_file(token, f'/pyt/{name_file}')