# Domain--Driven_Design_library_manager

---

Библиотечное приложение на Python

Описание

Это приложение для управления библиотекой, реализованное с использованием принципов SOLID, DRY, KISS и DDD. Приложение позволяет выполнять операции с книгами, такие как добавление, удаление, поиск, отображение всех книг и изменение их статуса. Все данные хранятся в обычном текстовом файле, что позволяет легко управлять информацией без необходимости использования базы данных.

Используемые принципы разработки:

SOLID — набор принципов объектно-ориентированного программирования, которые обеспечивают гибкость, расширяемость и поддержку кода.

DRY (Don't Repeat Yourself) — избегание дублирования кода, что улучшает его поддерживаемость.

KISS (Keep It Simple, Stupid) — стремление к простоте в решениях, избегание излишней сложности.

DDD (Domain-Driven Design) — фокус на разработке программных решений, ориентированных на бизнес-логику.



---

Основные возможности

1. Добавление книги: Введите название, автора и год издания книги, чтобы добавить её в библиотеку.


2. Удаление книги: Удалите книгу по уникальному ID.


3. Поиск книги: Найдите книгу по названию, автору или году издания.


4. Отображение всех книг: Просмотр всех книг, находящихся в библиотеке.


5. Изменение статуса книги: Изменение статуса книги на "в наличии" или "выдана".


6. Валидация ввода: Все введенные данные проходят проверку на корректность.




---

Установка и запуск

Требования:

Python 3.10+

Зависимости: Нет дополнительных зависимостей для работы приложения, только стандартная библиотека Python.


Инструкция по запуску:

1. Клонируйте репозиторий:

git clone https://github.com/aleksOtryshko/Domain--Driven_Design_library_manager.git


2. Перейдите в директорию проекта:

cd <директория проекта>


3. Убедитесь, что текстовый файл для хранения данных о книгах существует и доступен в директории приложения.


4. Запустите приложение:

python main.py




---

Структура проекта

Приложение использует подход Domain-Driven Design (DDD), разделяя логику на несколько слоев:

1. Домен (Domain): Содержит бизнес-логику и сущности, такие как книги.


2. Инфраструктура (Infrastructure): Взаимодействует с внешними системами, такими как файловая система для хранения данных.


3. Приложение (Application): Обрабатывает запросы пользователя, управляет жизненным циклом данных и выполняет операции с книгами.




---

Принципы разработки

SOLID: Приложение разделяет ответственность между классами и интерфейсами, поддерживая принцип открытости/закрытости (OCP) и принцип единой ответственности (SRP).

DRY: Код не содержит дублирования, и все повторяющиеся логические блоки вынесены в отдельные методы.

KISS: Логика приложения проста и ясна, операции с книгами не перегружены дополнительной сложностью.

DDD: Структура приложения ориентирована на доменные сущности, такие как книги и операции с ними.



---

Тестирование

Для запуска тестов используйте инструмент pytest.

1. Убедитесь, что у вас установлен pytest:

pip install pytest


2. Запустите тесты:

pytest



Тесты покрывают основные функции приложения, включая добавление, удаление, поиск книг и валидацию ввода.


---

Пример использования

1. После запуска приложения, вам будет предложено выбрать действие:

Введите 1 для добавления книги.

Введите 2 для удаления книги по ID.

Введите 3 для поиска книги.

Введите 4 для отображения всех книг.

Введите 5 для изменения статуса книги.

Введите 6 для выхода из приложения.



2. Приложение будет взаимодействовать с вами через командную строку, запрашивая необходимые данные, такие как название книги, автор и год.




---

Заключение

Данное приложение демонстрирует использование принципов SOLID, DRY, KISS и DDD в реальной задаче. Оно простое, легко расширяемое и поддерживаемое, с четким разделением ответственности и ясной логикой взаимодействия с пользователем и данными.




---

Library Application in Python

Description

This is a library management application developed in Python, utilizing SOLID, DRY, KISS, and DDD principles. The application allows you to perform operations on books such as adding, removing, searching, displaying all books, and updating their status. All data is stored in a plain text file, making it easy to manage the information without the need for a database.

Development Principles Used:

SOLID — A set of object-oriented programming principles that ensure code flexibility, scalability, and maintainability.

DRY (Don't Repeat Yourself) — Avoiding code duplication to improve code maintainability.

KISS (Keep It Simple, Stupid) — Striving for simplicity in solutions and avoiding unnecessary complexity.

DDD (Domain-Driven Design) — Focusing on developing software solutions centered around business logic.



---

Main Features

1. Add a book: Enter the title, author, and publication year of the book to add it to the library.


2. Remove a book: Delete a book by its unique ID.


3. Search books: Search for a book by title, author, or publication year.


4. Display all books: View all books in the library.


5. Update book status: Change the status of a book to "available" or "borrowed".


6. Input validation: All input data is validated for correctness.




---

Installation and Running

Requirements:

Python 3.10+

Dependencies: No external dependencies, only the standard Python library.


Instructions:

1. Clone the repository:

git clone https://github.com/aleksOtryshko/Domain--Driven_Design_library_manager.git


2. Navigate to the project directory:

cd <project directory>


3. Ensure that the text file for storing book data exists and is accessible in the project directory.


4. Run the application:

python main.py




---

Project Structure

The application uses Domain-Driven Design (DDD), separating the logic into several layers:

1. Domain: Contains business logic and entities such as books.


2. Infrastructure: Interacts with external systems, such as the file system for data storage.


3. Application: Handles user requests, manages the lifecycle of data, and performs operations on books.




---

Development Principles

SOLID: The application separates responsibilities between classes and interfaces, supporting the Open/Closed Principle (OCP) and the Single Responsibility Principle (SRP).

DRY: The code is free from duplication, and all repeated logical blocks are extracted into separate methods.

KISS: The application logic is simple and clear, and operations on books are not overloaded with unnecessary complexity.

DDD: The application's structure is oriented around domain entities, such as books and operations related to them.



---

Testing

To run tests, use the pytest tool.

1. Ensure that pytest is installed:

pip install pytest


2. Run the tests:

pytest



The tests cover the main functionalities of the application, including adding, removing, searching books, and input validation.


---

Example Usage

1. After launching the application, you will be prompted to choose an action:

Enter 1 to add a book.

Enter 2 to remove a book by ID.

Enter 3 to search for a book.

Enter 4 to display all books.

Enter 5 to change the book's status.

Enter 6 to exit the application.



2. The application will interact with you through the command line, asking for necessary data such as book title, author, and year.




---

Conclusion

This application demonstrates the use of SOLID, DRY, KISS, and DDD principles in a real-world task. It is simple, easily extensible, and maintainable, with a clear separation of concerns and straightforward logic for user interaction and data handling.


