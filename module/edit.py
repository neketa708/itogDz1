from abc import ABC

import tabulate

from module.menu import Menu


class Edit(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input('введите номер заметки ->'))
        print(tabulate.tabulate([['id', 'имя', 'описание', 'дата изменений'], notes[key].to_list()]))
        if input('редактировать Y/N?').lower() == 'y':
            name, body = input('введите новое имя заметки ->'), input('введите новое описание ->')
            notes[key].__set__(name, body)
            print('отредактировано')
        else:
            print('отмена')
        return notes