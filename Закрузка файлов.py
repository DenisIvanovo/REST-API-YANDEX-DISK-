"""
Подключаемся к яндекс диску
Получаем url ссылку для загрузки файла
после по полученой ссылке,методом put загружаем файл.
"""

import json
import requests

# Получаем токен для активации на яндекс диске.
with open('tok_yan.json')as file:
    token = json.load(file)


class Loading_url:
    def __init__(self, tok, path, path_download_file):
        # Заполняем Заголовки и параметры.
        self.download_file = path_download_file  # Загружаемый файл.
        self.download_link = ''  # Ссылка на загрузку файла.
        self.header = tok  # Токен авторизации.
        self.param = {'path': path}  # Указываем путь куда загрузить файл и указываем имя файла.
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.accomplishment()

    def accomplishment(self):
        # Отпарвляем команду на выполнение.
        answer = requests.get(url=self.url, headers=self.header, params=self.param)
        if answer.status_code == 200:  # Команда выполнена успешно.
            # Получаем ссылку для загрузки файла.
            self.download_link = answer.json()['href']
            # Вызываем функцию загрузки.
            self.uploading_a_file()
        else:
            # Ответ о возникшей ошибке.
            print(answer.json()["message"])

    def uploading_a_file(self):
        headers = {'Content-type': 'image/jpeg'}
        # Отправляем команду на выполнение.
        files = requests.put(self.download_link, data=open(self.download_file, 'rb'), headers=headers)
        if files.status_code == 201:  # Команда выполнена успешно.
            print('Файл загружен успешно.')
        else:
            print(files.json()["message"])


if __name__ == '__main__':
    # указываем путь на диске
    specify_the_path_on_the_disk = ''  # ''- Корневая папка диска.
    # Имя файла и формат.
    file = 'denis.jpg'
    # Указываем что хотим загрузить.
    download_file = '/Users/dEniS/Downloads/ppp.jpg'
    Loading_url(token, f'{specify_the_path_on_the_disk}/{file}', download_file)
