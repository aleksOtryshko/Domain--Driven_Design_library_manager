class UserInterface:
    @staticmethod
    def show_menu() -> str:
        """
        Отображает главное меню и запрашивает выбор пользователя.
        :return: Выбранный пункт меню
        """
        print(
            "\nМеню:\n"
            "1. Добавить книгу\n"
            "2. Удалить книгу\n"
            "3. Поиск книги\n"
            "4. Отобразить все книги\n"
            "5. Изменить статус книги\n"
            "6. Выход\n"
        )
        return input("Выберите действие: ")

    @staticmethod
    def get_input(prompt: str) -> str:
        """
        Запрашивает ввод от пользователя.
        :param prompt: Текст запроса
        :return: Введенное значение
        """
        return input(prompt).strip()

    @staticmethod
    def display_message(message: str) -> None:
        """
        Отображает сообщение пользователю.
        :param message: Текст сообщения
        """
        print(message)

    @staticmethod
    def display_books(books: list) -> None:
        """
        Отображает список книг.
        :param books: Список объектов Book
        """
        if not books:
            print("Библиотека пуста.")
        else:
            for book in books:
                print(book)

