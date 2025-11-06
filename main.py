from typing import List, Optional, Dict, Any
from datetime import datetime

class LibraryException(Exception):
    """Базовое исключение для всех ошибок библиотеки."""
    pass

class Author:
    """Класс автора книги"""

    def __init__(self, author_id: str, name: str, birth_year: Optional[int] = None,
                 country: Optional[str] = None) -> None:
        if not name or not name.strip():
            raise LibraryException("Имя автора обязательно и не может быть пустым")
        if not author_id or not author_id.strip():
            raise LibraryException("ID автора обязательно и не может быть пустым")
        self._author_id = author_id.strip()
        self._name = name.strip()
        current_year = datetime.now().year
        if birth_year is not None and (birth_year < 0 or birth_year > current_year):
            raise LibraryException("Год рождения некорректен")
        self._birth_year = birth_year
        self._country = country

    @property
    def author_id(self) -> str:
        return self._author_id

    @author_id.setter
    def author_id(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("ID автора обязательно и не может быть пустым")
        self._author_id = value.strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("Имя автора обязательно и не может быть пустым")
        self._name = value.strip()

    @property
    def birth_year(self) -> Optional[int]:
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value: Optional[int]) -> None:
        current_year = datetime.now().year
        if value is not None and (value < 0 or value > current_year):
            raise LibraryException("Год рождения некорректен")
        self._birth_year = value

    @property
    def country(self) -> Optional[str]:
        return self._country

    @country.setter
    def country(self, value: Optional[str]) -> None:
        self._country = value

class Genre:
    """Класс жанра книги"""

    def __init__(self, name: str, description: str = "") -> None:
        if not name.strip():
            raise LibraryException("Название жанра не может быть пустым")
        self._name = name.strip()
        self._description = description.strip() if description else ""

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("Название жанра не может быть пустым")
        self._name = value.strip()

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value.strip() if value else ""

class Publisher:
    """Класс издателя книги"""

    def __init__(self, publisher_id: str, name: str, location: Optional[str] = None) -> None:
        if not name or not name.strip():
            raise LibraryException("Имя издателя обязательно и не может быть пустым")
        if not publisher_id or not publisher_id.strip():
            raise LibraryException("ID издателя обязательно и не может быть пустым")
        self._publisher_id = publisher_id.strip()
        self._name = name.strip()
        self._location = location

    @property
    def publisher_id(self) -> str:
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("ID издателя обязательно и не может быть пустым")
        self._publisher_id = value.strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("Имя издателя обязательно и не может быть пустым")
        self._name = value.strip()

    @property
    def location(self) -> Optional[str]:
        return self._location

    @location.setter
    def location(self, value: Optional[str]) -> None:
        self._location = value

class Book:
    def __init__(self, isbn: str, title: str, authors: List[Author], genre: Genre,
                 publisher: Publisher, year: int, pages: Optional[int] = None) -> None:
        if not isbn or not isbn.strip():
            raise LibraryException("ISBN обязателен")
        if not title or not title.strip():
            raise LibraryException("Название книги обязательно")
        if not authors or not all(isinstance(a, Author) for a in authors):
            raise LibraryException("Список авторов должен содержать хотя бы одного автора")
        if not isinstance(genre, Genre):
            raise LibraryException("Жанр должен быть объектом Genre")
        if not isinstance(publisher, Publisher):
            raise LibraryException("Издатель должен быть объектом Publisher")
        if year < 0 or year > datetime.now().year:
            raise LibraryException("Год издания некорректен")
        if pages is not None and pages <= 0:
            raise LibraryException("Количество страниц должно быть положительным")

        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.genre = genre
        self.publisher = publisher
        self.year = year
        self.pages = pages

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("ISBN обязателен")
        self._isbn = value.strip()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("Название книги обязательно")
        self._title = value.strip()

    @property
    def authors(self) -> List[Author]:
        return self._authors

    @authors.setter
    def authors(self, value: List[Author]) -> None:
        if not value or not all(isinstance(a, Author) for a in value):
            raise LibraryException("Список авторов должен содержать хотя бы одного автора")
        self._authors = value

    @property
    def genre(self) -> Genre:
        return self._genre

    @genre.setter
    def genre(self, value: Genre) -> None:
        if not isinstance(value, Genre):
            raise LibraryException("Жанр должен быть объектом Genre")
        self._genre = value

    @property
    def publisher(self) -> Publisher:
        return self._publisher

    @publisher.setter
    def publisher(self, value: Publisher) -> None:
        if not isinstance(value, Publisher):
            raise LibraryException("Издатель должен быть объектом Publisher")
        self._publisher = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if value is None or value < 0 or value > datetime.now().year:
            raise LibraryException("Год издания некорректен")
        self._year = value

    @property
    def pages(self) -> Optional[int]:
        return self._pages

    @pages.setter
    def pages(self, value: Optional[int]) -> None:
        if value is not None and value <= 0:
            raise LibraryException("Количество страниц должно быть положительным числом")
        self._pages = value

class User:
    """Класс пользователя библиотеки"""

    def __init__(self, user_id: str, name: str) -> None:
        if not user_id or not user_id.strip():
            raise LibraryException("ID пользователя обязателен")
        if not name or not name.strip():
            raise LibraryException("Имя пользователя обязательно и не может быть пустым")
        self._user_id = user_id.strip()
        self._name = name.strip()
        self._borrowed_books: List[Book] = []

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("ID пользователя обязателен и не может быть пустым")
        self._user_id = value.strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("Имя пользователя обязательно и не может быть пустым")
        self._name = value.strip()

    @property
    def borrowed_books(self) -> List[Book]:
        return self._borrowed_books

    @borrowed_books.setter
    def borrowed_books(self, value: List[Book]) -> None:
        if not isinstance(value, list) or not all(isinstance(b, Book) for b in value):
            raise LibraryException("borrowed_books должен быть списком объектов Book")
        self._borrowed_books = value

class BorrowRecord:
    """Класс записи о заимствовании книги"""

    def __init__(self, record_id: str, book: Book, user: User,
                 borrow_date: datetime, due_date: datetime) -> None:

        if not record_id or not record_id.strip():
            raise LibraryException("ID записи обязателен")
        if not isinstance(book, Book):
            raise LibraryException("Книга должна быть объектом Book")
        if not isinstance(user, User):
            raise LibraryException("Пользователь должен быть объектом User")
        if due_date <= borrow_date:
            raise LibraryException("Дата возврата должна быть позже даты выдачи")

        self._record_id = record_id.strip()
        self._book = book
        self._user = user
        self._borrow_date = borrow_date
        self._due_date = due_date
        self._return_date: Optional[datetime] = None

    @property
    def record_id(self) -> str:
        return self._record_id

    @record_id.setter
    def record_id(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("ID записи обязателен")
        self._record_id = value.strip()

    @property
    def book(self) -> Book:
        return self._book

    @book.setter
    def book(self, value: Book) -> None:
        if not isinstance(value, Book):
            raise LibraryException("Книга должна быть объектом Book")
        self._book = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        if not isinstance(value, User):
            raise LibraryException("Пользователь должен быть объектом User")
        self._user = value

    @property
    def borrow_date(self) -> datetime:
        return self._borrow_date

    @borrow_date.setter
    def borrow_date(self, value: datetime) -> None:
        if value >= self._due_date:
            raise LibraryException("Дата выдачи должна быть раньше срока возврата")
        self._borrow_date = value

    @property
    def due_date(self) -> datetime:
        return self._due_date

    @due_date.setter
    def due_date(self, value: datetime) -> None:
        if value <= self._borrow_date:
            raise LibraryException("Срок возврата должен быть позже даты выдачи")
        self._due_date = value

    @property
    def return_date(self) -> Optional[datetime]:
        return self._return_date

    @return_date.setter
    def return_date(self, value: Optional[datetime]) -> None:
        if value and value < self._borrow_date:
            raise LibraryException("Дата возврата не может быть раньше даты выдачи")
        self._return_date = value

class Library:
    """Главный класс-менеджер библиотеки"""

    def __init__(self, name: str) -> None:
        if not name or not name.strip():
            raise LibraryException("Название библиотеки обязательно")

        self._name = name.strip()
        self._books: Dict[str, Book] = {}
        self._users: Dict[str, User] = {}
        self._borrow_records: Dict[str, BorrowRecord] = {}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise LibraryException("Название библиотеки обязательно")
        self._name = value.strip()

    @property
    def books(self) -> Dict[str, Book]:
        return self._books

    @property
    def users(self) -> Dict[str, User]:
        return self._users

    @property
    def borrow_records(self) -> Dict[str, BorrowRecord]:
        return self._borrow_records
