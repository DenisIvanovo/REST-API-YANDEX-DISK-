"""
Подключаемся к яндекс диску
и получаем метаинформацию о диске
Полученую информацию записываем в текстовый файл
"""

import json
import requests

# Получаем токен для активации на яндекс диске.
with open('tok_yan.json')as file:
    token = json.load(file)


class Metainformation:
    def __init__(self, tok):
        # Заполняем Заголовки и параметры.
        self.header = tok  # Токен авторизации.
        self.url = 'https://cloud-api.yandex.net/v1/disk'
        self.accomplishment()

    def accomplishment(self):
        # Отпарвляем команду на выполнение.
        answer = requests.get(url=self.url, headers=self.header)
        if answer.status_code == 200:  # Команда выполнена успешно.
            self.report_file(answer)
            print(answer.json())
        else:
            print(answer.json()["message"])

    def report_file(self, answer):
        # Полученую информацию записываем в текстовый файл.
        # Получаем нужную нам информацию
        info = {'Отображаемое имя': answer.json()["user"]['display_name'],
                'Максимальный поддерживаемый размер файла': f'{answer.json()["max_file_size"]}'
                                                            f'  байт или {(answer.json()["max_file_size"]/ 1073741824)} '
                                                            f'гигобайт.',
                'Общий объем диска (байт)': f'{answer.json()["total_space"]}'
                                                            f'  байт или {(answer.json()["total_space"]/ 1073741824)} '
                                                            f'гигобайт.',
                'Используемый объем диска (байт)': f'{answer.json()["used_space"]}'
                                                            f'  байт или {(answer.json()["used_space"]/ 1073741824)} '
                                                            f'гигобайт.',
                'Общий размер файлов в Корзине (байт)': f'{answer.json()["trash_size"]}'
                                                            f'  байт или {(answer.json()["trash_size"]/ 1073741824)} '
                                                            f'гигобайт.',
                'Признак наличия купленного места': f'{answer.json()["is_paid"]}'}

        # Записываем в текстовый файл.
        with open('info_disk.txt', 'w')as file:
            for key, value in info.items():
                file.write(f'{key} - {value}\n')


if __name__ == '__main__':
    Metainformation(token)