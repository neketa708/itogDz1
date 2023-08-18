from abc import ABC

import tabulate

from module.menu import Menu


class ShowId(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input('введите номер заметки ->'))
        print(tabulate.tabulate([['id', 'имя', 'описание', 'дата изменений'], notes[key].to_list()]))
        return notes