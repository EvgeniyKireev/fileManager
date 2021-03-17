import os
import shutil
import pathlib
from typing import Dict
class PathStorage:
    """Хранение информации о пути"""

    def __init__(self, sep : str) -> None:
        self.sep = sep
        self.__storage = ["storage"]

    def add_path(self, path: str) -> None:
        """Добавляет файл в иерархию каталогов"""
        # Если хотим выйти на уровень выше
        if ".." in path and len(self.__storage) != 1:
            self.__storage.pop(-1)
        # Если хотим выйти за пределы выдуманного мира
        elif ".." in path:
            print("Вы хотите выйти за пределы песочницы!")
        # Значит хотим перейти на уровень ниже
        else:
            self.__storage.append(path)

    def file2path(self, file_name: str) -> str:
        """Возвращает указанный файл в текущей иерархии каталогов"""
        locale_storage = self.__storage.copy()
        locale_storage.append(file_name)
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(locale_storage)

    @property
    def path(self):
        """Возвращает текущую иерархию каталогов"""
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(self.__storage)

    @property
    def upper_path(self):
        """Возвращает директорию выше текущей"""
        abs_path = pathlib.Path(__file__).parent.absolute()
        print(self.__storage[1:])
        return str(abs_path) + self.sep + self.sep.join(self.__storage[:1])