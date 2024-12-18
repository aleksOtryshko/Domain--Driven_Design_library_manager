import json
from domain.book import Book

class FileManager:
    FILE_NAME = "library.json"

    @staticmethod
    def read_books():
        """
        Считывает список книг из JSON-файла.
        :return: Список объектов Book
        """
        try:
            with open(FileManager.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    @staticmethod
    def write_books(books):
        """
        Записывает список книг в JSON-файл.
        :param books: Список объектов Book
        """
        with open(FileManager.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([book.__dict__ for book in books], file, ensure_ascii=False, indent=4)

