from abc import ABC

import tabulate

from module.menu import Menu


class Delete(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input('введите номер заметки ->'))
        print(tabulate.tabulate([['id', 'имя', 'описание', 'дата изменений'], notes[key].to_list()]))
        if input('удалить Y/N?').lower() == 'y':
            notes.pop(key)
            print('удалено')
        else:
            print('отмена')
        return notes