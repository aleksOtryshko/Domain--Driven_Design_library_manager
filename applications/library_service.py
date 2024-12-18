from domain.book import Book
from infrastructure.file_manager import FileManager
from infrastructure.user_interface import UserInterface

class LibraryService:
    def __init__(self):
        self.books = FileManager.read_books()

    def show_menu(self):
        while True:
            choice = UserInterface.show_menu()
            match choice:
                case "1":
                    self.add_book()
                case "2":
                    self.remove_book()
                case "3":
                    self.search_books()
                case "4":
                    self.display_books()
                case "5":
                    self.update_status_menu()
                case "6":
                    UserInterface.display_message("Выход из программы.")
                    exit()
                case _:
                    UserInterface.display_message("Некорректный выбор. Попробуйте снова.")

    def add_book(self):
        title = self.validate_input("Введите название книги: ")
        author = self.validate_input("Введите автора книги: ")
        year = self.validate_year("Введите год издания: ")
        new_id = max((book.id for book in self.books), default=0) + 1
        book = Book(new_id, title, author, year)
        self.books.append(book)
        FileManager.write_books(self.books)
        UserInterface.display_message(f"Книга '{title}' добавлена с ID {new_id}.")

    def remove_book(self):
        book_id = int(UserInterface.get_input("Введите ID книги для удаления: "))
        book = self.find_book_by_id(book_id)
        if not book:
            UserInterface.display_message("Книга не найдена!")
            return
        self.books.remove(book)
        FileManager.write_books(self.books)
        UserInterface.display_message(f"Книга с ID {book_id} удалена.")

    def search_books(self):
        query = UserInterface.get_input("Введите строку для поиска (по названию, автору или году): ")
        results = [book for book in self.books if query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or query.lower() in book.year]
        if results:
            UserInterface.display_books(results)
        else:
            UserInterface.display_message("Книги не найдены.")

    def display_books(self):
        UserInterface.display_books(self.books)

    def update_status_menu(self):
        book_id = int(UserInterface.get_input("Введите ID книги для изменения статуса: "))
        book = self.find_book_by_id(book_id)
        if not book:
            UserInterface.display_message("Книга не найдена!")
            return

        UserInterface.display_message("\nВыберите новый статус:")
        UserInterface.display_message("1. В наличии")
        UserInterface.display_message("2. Выдана")

        status_choice = UserInterface.get_input("Ваш выбор: ")
        status = {
            "1": "в наличии",
            "2": "выдана"
        }.get(status_choice)

        if not status:
            UserInterface.display_message("Некорректный выбор статуса.")
            return

        book.status = status
        FileManager.write_books(self.books)
        UserInterface.display_message(f"Статус книги с ID {book_id} изменен на '{status}'.")

    def find_book_by_id(self, book_id: int) -> Book | None:
        return next((book for book in self.books if book.id == book_id), None)

    def validate_input(self, prompt: str) -> str:
        while True:
            value = UserInterface.get_input(prompt)
            if value:
                return value
            UserInterface.display_message("Поле не может быть пустым. Попробуйте снова.")

    def validate_year(self, prompt: str) -> str:
        while True:
            year = UserInterface.get_input(prompt)
            if year.isdigit() and 868 <= int(year) <= 2024:
                return year
            UserInterface.display_message("Год должен быть числом в пределах от 868 до 2024. Пожалуйста, попробуйте снова.")

