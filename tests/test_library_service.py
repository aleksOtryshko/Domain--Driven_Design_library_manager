import pytest
from unittest.mock import patch, MagicMock
from applications.library_service import LibraryService
from domain.book import Book


@pytest.fixture
def library_service():
    with patch("applications.library_service.FileManager") as mock_file_manager, \
         patch("applications.library_service.UserInterface") as mock_user_interface:
        mock_file_manager.read_books.return_value = [
            Book(1, "Book One", "Author One", "2001"),
            Book(2, "Book Two", "Author Two", "2002")
        ]
        yield LibraryService()


def test_add_book(library_service):
    with patch("applications.library_service.UserInterface.get_input", side_effect=["New Book", "New Author", "2020"]), \
         patch("applications.library_service.FileManager.write_books") as mock_write_books, \
         patch("applications.library_service.UserInterface.display_message") as mock_display_message:
        library_service.add_book()

        assert len(library_service.books) == 3
        assert library_service.books[-1].title == "New Book"
        mock_write_books.assert_called_once()
        mock_display_message.assert_called_with("Книга 'New Book' добавлена с ID 3.")


def test_remove_book(library_service):
    with patch("applications.library_service.UserInterface.get_input", return_value="1"), \
         patch("applications.library_service.FileManager.write_books") as mock_write_books, \
         patch("applications.library_service.UserInterface.display_message") as mock_display_message:
        library_service.remove_book()

        assert len(library_service.books) == 1
        mock_write_books.assert_called_once()
        mock_display_message.assert_called_with("Книга с ID 1 удалена.")


def test_search_books(library_service):
    with patch("applications.library_service.UserInterface.get_input", return_value="Book"), \
         patch("applications.library_service.UserInterface.display_books") as mock_display_books, \
         patch("applications.library_service.UserInterface.display_message") as mock_display_message:
        library_service.search_books()

        mock_display_books.assert_called_once()
        mock_display_message.assert_not_called()


def test_display_books(library_service):
    with patch("applications.library_service.UserInterface.display_books") as mock_display_books:
        library_service.display_books()

        mock_display_books.assert_called_once_with(library_service.books)


def test_update_status_menu(library_service):
    with patch("applications.library_service.UserInterface.get_input", side_effect=["1", "1"]), \
         patch("applications.library_service.FileManager.write_books") as mock_write_books, \
         patch("applications.library_service.UserInterface.display_message") as mock_display_message:
        library_service.update_status_menu()

        assert library_service.books[0].status == "в наличии"
        mock_write_books.assert_called_once()
        mock_display_message.assert_called_with("Статус книги с ID 1 изменен на 'в наличии'.")


def test_find_book_by_id(library_service):
    book = library_service.find_book_by_id(1)
    assert book is not None
    assert book.title == "Book One"

    book = library_service.find_book_by_id(99)
    assert book is None


def test_validate_input(library_service):
    with patch("applications.library_service.UserInterface.get_input", side_effect=["", "Valid Input"]), \
         patch("applications.library_service.UserInterface.display_message") as mock_display_message:
        result = library_service.validate_input("Enter something:")

        assert result == "Valid Input"
        mock_display_message.assert_called_once_with("Поле не может быть пустым. Попробуйте снова.")


def test_validate_year(library_service):
    with patch("applications.library_service.UserInterface.get_input", side_effect=["abcd", "1500"]), \
         patch("applications.library_service.UserInterface.display_message") as mock_display_message:
        result = library_service.validate_year("Enter year:")

        assert result == "1500"
        mock_display_message.assert_called_once_with("Год должен быть числом в пределах от 868 до 2024. Пожалуйста, попробуйте снова.")

