class Book:
    def __init__(self, book_id, title, author, year, status="в наличии"):
        """
        Инициализация объекта книги.
        :param book_id: Уникальный ID книги
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :param status: Статус книги ("в наличии" или "выдана")
        """
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        """
        Возвращает строковое представление объекта книги.
        """
        return f"[ID: {self.id}] {self.title} by {self.author}, {self.year} - {self.status}"

