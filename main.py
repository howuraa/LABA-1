from typing import List, Optional, Dict, Any
from datetime import datetime,timedelta

current_year = datetime.now().year


class LibraryException(Exception):
    """Базовое исключение для всех ошибок библиотеки."""
    pass

class AuthorError(LibraryException):
    """Базовое исключение для ошибок автора."""
    pass

class InvalidAuthorNameError(AuthorError):
    """Имя автора пустое или некорректное."""
    pass

class InvalidAuthorIDError(AuthorError):
    """ID автора пустой или некорректный."""
    pass

class InvalidBirthYearError(AuthorError):
    """Некорректный год рождения автора."""
    pass

class GenreError(LibraryException):
    """Базовое исключение для ошибок жанра."""
    pass

class InvalidGenreNameError(GenreError):
    """Название жанра пустое или некорректное."""
    pass

class InvalidGenreDescriptionError(GenreError):
    """Описание жанра некорректное."""
    pass

class PublisherError(LibraryException):
    """Базовое исключение для ошибок издателя."""
    pass

class InvalidPublisherNameError(PublisherError):
    """Имя издателя пустое или некорректное."""
    pass

class InvalidPublisherIDError(PublisherError):
    """ID издателя пустой или некорректный."""
    pass

class InvalidLocationError(PublisherError):
    """Локация издателя некорректная."""
    pass

class BookError(LibraryException):
    """Базовое исключение для ошибок книги."""
    pass

class InvalidBookTitleError(BookError):
    """Название книги пустое или некорректное."""
    pass

class InvalidISBNError(BookError):
    """ISBN книги пустой или некорректный."""
    pass

class BookAuthorsListError(BookError):
    """Список авторов книги пустой или некорректный."""
    pass

class InvalidBookPublisherError(BookError):
    """Издатель книги некорректный."""
    pass

class InvalidBookGenreError(BookError):
    """Жанр книги некорректный."""
    pass

class InvalidBookYearError(BookError):
    """Год издания книги некорректный."""
    pass

class InvalidBookPagesError(BookError):
    """Количество страниц должно быть положительным числом."""
    pass

class UserError(LibraryException):
    """Базовое исключение для ошибок пользователя."""
    pass

class InvalidUserNameError(UserError):
    """Имя пользователя пустое или некорректное."""
    pass

class InvalidUserIDError(UserError):
    """ID пользователя пустой или некорректный."""
    pass

class InvalidBorrowedBooksError(UserError):
    """Список заимствованных книг некорректный."""
    pass

class BorrowRecordError(LibraryException):
    """Базовое исключение для ошибок записей о заимствовании."""
    pass

class InvalidRecordIDError(BorrowRecordError):
    """ID записи пустой или некорректный."""
    pass

class InvalidBookReferenceError(BorrowRecordError):
    """Ссылка на книгу некорректная."""
    pass

class InvalidUserReferenceError(BorrowRecordError):
    """Ссылка на пользователя некорректная."""
    pass

class InvalidBorrowDateError(BorrowRecordError):
    """Дата выдачи некорректная."""
    pass

class InvalidDueDateError(BorrowRecordError):
    """Срок возврата некорректный."""
    pass

class InvalidReturnDateError(BorrowRecordError):
    """Дата возврата некорректная."""
    pass

class DateConsistencyError(BorrowRecordError):
    """Несоответствие дат (например, возврат раньше выдачи)."""
    pass

class FineError(LibraryException):
    """Базовое исключение для ошибок штрафов."""
    pass

class InvalidFineIDError(FineError):
    """ID штрафа пустой или некорректный."""
    pass

class InvalidFineAmountError(FineError):
    """Сумма штрафа некорректная."""
    pass

class InvalidFineReasonError(FineError):
    """Причина штрафа пустая или некорректная."""
    pass

class InvalidFineReferenceError(FineError):
    """Ссылка на запись о заимствовании некорректная."""
    pass

class ReservationError(LibraryException):
    """Базовое исключение для ошибок резервирования."""
    pass

class InvalidReservationIDError(ReservationError):
    """ID резервирования пустой или некорректный."""
    pass

class InvalidReservationDateError(ReservationError):
    """Дата резервирования некорректная."""
    pass

class InvalidExpiryDateError(ReservationError):
    """Дата истечения резервирования некорректная."""
    pass

class ReservationDateConsistencyError(ReservationError):
    """Несоответствие дат резервирования."""
    pass

class ExpireDateConsistencyError(ReservationError):
    """Несоответствие дат резервирования."""
    pass

class ReviewError(LibraryException):
    """Базовое исключение для ошибок отзывов."""
    pass

class InvalidReviewIDError(ReviewError):
    """ID отзыва пустой или некорректный."""
    pass

class InvalidRatingError(ReviewError):
    """Рейтинг некорректный (должен быть от 1 до 5)."""
    pass

class InvalidReviewCommentError(ReviewError):
    """Комментарий отзыва некорректный."""
    pass

class InvalidReviewDateError(ReviewError):
    """Дата отзыва некорректная."""
    pass

class LibrarianError(LibraryException):
    """Базовое исключение для ошибок библиотекаря."""
    pass

class InvalidEmployeeIDError(LibrarianError):
    """ID сотрудника пустой или некорректный."""
    pass

class InvalidDepartmentError(LibrarianError):
    """Отдел библиотекаря некорректный."""
    pass

class LibraryManagementError(LibraryException):
    """Базовое исключение для ошибок управления библиотекой."""
    pass

class DuplicateItemError(LibraryManagementError):
    """Попытка добавить дублирующий элемент."""
    pass

class ItemNotFoundError(LibraryManagementError):
    """Элемент не найден."""
    pass

class LibraryOperationError(LibraryManagementError):
    """Ошибка выполнения операции в библиотеке."""
    pass

class InvalidLibraryNameError(LibraryManagementError):
    """Название библиотеки пустое или некорректное."""
    pass


class Author:
    """Класс автора книги"""

    def __init__(self, author_id: str, name: str, birth_year: Optional[int] = None,
                 country: Optional[str] = None) -> None:
        if not name or not name.strip():
            raise InvalidAuthorNameError("Имя автора обязательно и не может быть пустым")
        if not author_id or not author_id.strip():
            raise InvalidAuthorNameError("ID автора обязательно и не может быть пустым")
        self._author_id = author_id.strip()
        self._name = name.strip()
        current_year = datetime.now().year
        if birth_year is not None and (birth_year < 0 or birth_year > current_year):
            raise InvalidBirthYearError("Год рождения некорректен")
        self._birth_year = birth_year
        self._country = country

    @property
    def author_id(self) -> str:
        return self._author_id

    @author_id.setter
    def author_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidAuthorIDError("ID автора обязательно и не может быть пустым")
        self._author_id = value.strip()
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidAuthorNameError("Имя автора обязательно и не может быть пустым")
        self._name = value.strip()

    @property
    def birth_year(self) -> Optional[int]:
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value: Optional[int]) -> None:
        current_year = datetime.now().year
        if value is not None and (value < 0 or value > current_year):
            raise InvalidBirthYearError("Год рождения некорректен")
        self._birth_year = value

    @property
    def country(self) -> Optional[str]:
        return self._country

    @country.setter
    def country(self, value: Optional[str]) -> None:
        self._country = value

     
    def get_age(self) -> Optional[int]:
        """Возвращает возраст автора (если известен год рождения)"""
        if self._birth_year is None:
            return None
        return datetime.now().year - self._birth_year

    def is_modern_author(self) -> bool:
        """Проверяет, является ли автор современным (родился после 1900)"""
        return self._birth_year is not None and self._birth_year > 1900


     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "author_id": self._author_id,
            "name": self._name,
            "birth_year": self._birth_year,
            "country": self._country
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            author_id=data["author_id"],
            name=data["name"],
            birth_year=data.get("birth_year"),
            country=data.get("country")
        )

    def __str__(self) -> str:
        lines = [f"ID: {self._author_id}"]
        if self._name:
            lines.append(f"Имя: {self._name}")
        if self._birth_year:
            lines.append(f"Год рождения: {self._birth_year}")
        if self._country:
            lines.append(f"Страна: {self._country}")
        return "\n".join(lines)


class Genre:
    """Класс жанра книги"""

    def __init__(self, name: str, description: str = "") -> None:
        if not name.strip():
            raise InvalidGenreNameError("Название жанра не может быть пустым")
        self._name = name.strip()
        self._description = description.strip() if description else ""

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidGenreNameError("Название жанра не может быть пустым")
        self._name = value.strip()

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value.strip() if value else ""

    def has_description(self) -> bool:
        """Проверяет, есть ли описание у жанра"""
        return bool(self._description.strip())

     
    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "description": self._description
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Genre":
        return cls(
            name=data["name"],
            description=data.get("description", "")
        )

    def __str__(self) -> str:
        return f"{self._name} — {self._description or 'описание отсутствует'}"


class Publisher:
    """Класс издателя книги"""

    def __init__(self, publisher_id: str, name: str, location: Optional[str] = None) -> None:
        if not name or not name.strip():
            raise InvalidPublisherNameError("Имя издателя обязательно и не может быть пустым")
        if not publisher_id or not publisher_id.strip():
            raise InvalidPublisherIDError("ID издателя обязательно и не может быть пустым")
        self._publisher_id = publisher_id.strip()
        self._name = name.strip()
        self._location = location

    @property
    def publisher_id(self) -> str:
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidPublisherIDError("ID издателя обязательно и не может быть пустым")
        self._publisher_id = value.strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidPublisherNameError("Имя издателя обязательно и не может быть пустым")
        self._name = value.strip()

    @property
    def location(self) -> Optional[str]:
        return self._location

    @location.setter
    def location(self, value: Optional[str]) -> None:
        self._location = value

     
    def has_location(self) -> bool:
        """Проверяет, указана ли локация издателя"""
        return self._location is not None and bool(self._location.strip())

     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "publisher_id": self._publisher_id,
            "name": self._name,
            "location": self._location
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            publisher_id=data["publisher_id"],
            name=data["name"],
            location=data.get("location")
        )

    def __str__(self) -> str:
        lines = [f"ID: {self._publisher_id}", f"Имя: {self._name}"]
        if self._location:
            lines.append(f"Локация: {self._location}")
        return "\n".join(lines)


class Book:
    def __init__(self, isbn: str, title: str, authors: List[Author], genre: Genre,
                 publisher: Publisher, year: int, pages: Optional[int] = None) -> None:
        if not isbn or not isbn.strip():
            raise InvalidISBNError("ISBN обязателен")
        if not title or not title.strip():
            raise InvalidBookTitleError("Название книги обязательно")
        if not authors or not all(isinstance(a, Author) for a in authors):
            raise BookAuthorsListError("Список авторов должен содержать хотя бы одного автора")
        if not isinstance(genre, Genre):
            raise InvalidBookGenreError("Жанр должен быть объектом Genre")
        if not isinstance(publisher, Publisher):
            raise InvalidBookPublisherError("Издатель должен быть объектом Publisher")
        if year < 0 or year > datetime.now().year:
            raise InvalidBookYearError("Год издания некорректен")
        if pages is not None and pages <= 0:
            raise InvalidBookPagesError("Количество страниц должно быть положетельным")

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
            raise InvalidISBNError("ISBN обязателен")
        self._isbn = value.strip()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidBookTitleError("Название книги обязательно")
        self._title = value.strip()

    @property
    def authors(self) -> List[Author]:
        return self._authors

    @authors.setter
    def authors(self, value: List[Author]) -> None:
        if not value or not all(isinstance(a, Author) for a in value):
            raise BookAuthorsListError("Список авторов должен содержать хотя бы одного автора и быть объектами Author")
        self._authors = value

    @property
    def genre(self) -> Genre:
        return self._genre

    @genre.setter
    def genre(self, value: Genre) -> None:
        if not isinstance(value, Genre):
            raise InvalidBookGenreError("Жанр должен быть объектом Genre")
        self._genre = value

    @property
    def publisher(self) -> Publisher:
        return self._publisher

    @publisher.setter
    def publisher(self, value: Publisher) -> None:
        if not isinstance(value, Publisher):
            raise InvalidBookPublisherError("Издатель должен быть объектом Publisher")
        self._publisher = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if value is None or value < 0 or value > datetime.now().year:
            raise InvalidBookYearError("Год издания некорректен")
        self._year = value

    @property
    def pages(self) -> Optional[int]:
        return self._pages

    @pages.setter
    def pages(self, value: Optional[int]) -> None:
        if value is not None and value <= 0:
            raise InvalidBookPagesError("Количество страниц должно быть положительным числом")
        self._pages = value

     
    def add_author(self, author: Author) -> None:
        """Добавляет автора к книге"""
        if not isinstance(author, Author):
            raise InvalidAuthorNameError("Автор должен быть объектом Author")
        if author not in self._authors:
            self._authors.append(author)

    def remove_author(self, author: Author) -> None:
        """Удаляет автора из книги"""
        if author in self._authors:
            self._authors.remove(author)
        if not self._authors:
            raise BookAuthorsListError("Книга должна иметь хотя бы одного автора")

     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "isbn": self._isbn,
            "title": self._title,
            "authors": [a.to_dict() for a in self._authors],
            "genre": self._genre.to_dict(),
            "publisher": self._publisher.to_dict(),
            "year": self._year,
            "pages": self._pages
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        authors = [Author.from_dict(a) for a in data["authors"]]
        genre = Genre.from_dict(data["genre"])
        publisher = Publisher.from_dict(data["publisher"])
        return cls(
            isbn=data["isbn"],
            title=data["title"],
            authors=authors,
            genre=genre,
            publisher=publisher,
            year=data["year"],
            pages=data.get("pages")
        )

    def __str__(self) -> str:
        authors_str = ", ".join([a.name for a in self._authors])
        lines = [
            f"ISBN: {self._isbn}",
            f"Название: {self._title}",
            f"Авторы: {authors_str}",
            f"Жанр: {self._genre.name}",
            f"Издатель: {self._publisher.name}",
            f"Год: {self._year}"
        ]
        if self._pages:
            lines.append(f"Страниц: {self._pages}")
        return "\n".join(lines)


class User:
    """Класс пользователя библиотеки"""

    def __init__(self, user_id: str, name: str) -> None:
        if not user_id or not user_id.strip():
            raise InvalidUserIDError("ID пользователя обязателен")
        if not name or not name.strip():
            raise InvalidUserNameError("Имя пользователя обязательно и не может быть пустым")
        self._user_id = user_id.strip()
        self._name = name.strip()
        self._borrowed_books: List[Book] = [] 
    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidUserIDError("ID пользователя обязателен и не может быть пустым")
        self._user_id = value.strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidUserNameError("Имя пользователя обязательно и не может быть пустым")
        self._name = value.strip()

    @property
    def borrowed_books(self) -> List[Book]:
        return self._borrowed_books

    @borrowed_books.setter
    def borrowed_books(self, value: List[Book]) -> None:
        if not isinstance(value, list) or not all(isinstance(b, Book) for b in value):
            raise UserError("borrowed_books должен быть списком объектов Book")
        self._borrowed_books = value

     
    def borrow_book(self, book: Book) -> None:
        """Добавляет книгу в список заимствованных"""
        if book not in self._borrowed_books:
            self._borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        """Удаляет книгу из списка заимствованных"""
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)

     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self._user_id,
            "name": self._name,
            "borrowed_books": [b.isbn for b in self._borrowed_books] 
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any], books_dict: Dict[str, Book] = None) -> "User":
        """
        books_dict: словарь ISBN -> Book, чтобы восстановить ссылки на объекты книг
        """
        user = cls(user_id=data["user_id"], name=data["name"])
        if books_dict and "borrowed_books" in data:
            for isbn in data["borrowed_books"]:
                if isbn in books_dict:
                    user.borrow_book(books_dict[isbn])
        return user

    def __str__(self) -> str:
        borrowed = ", ".join([b.title for b in self._borrowed_books]) or "нет книг"
        return f"ID: {self._user_id}\nИмя: {self._name}\nЗаимствованные книги: {borrowed}"

class BorrowRecord:
    """Класс записи о заимствовании книги"""

    def __init__(self,
                 record_id: str,
                 book: Book,
                 user: User,
                 borrow_date: datetime,
                 due_date: datetime,
                 return_date: Optional[datetime] = None) -> None:

        if not record_id or not record_id.strip():
            raise InvalidRecordIDError("ID записи обязателен")
        if not isinstance(book, Book):
            raise InvalidBookReferenceError("Книга должна быть объектом Book")
        if not isinstance(user, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        if due_date <= borrow_date:
            raise DateConsistencyError("Дата возврата должна быть позже даты выдачи")

        self._record_id = record_id.strip()
        self._book = book
        self._user = user
        self._borrow_date = borrow_date
        self._due_date = due_date
        self._return_date = return_date


    @property
    def record_id(self) -> str:
        return self._record_id

    @record_id.setter
    def record_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidRecordIDError("ID записи обязателен")
        self._record_id = value.strip()

    @property
    def book(self) -> Book:
        return self._book

    @book.setter
    def book(self, value: Book) -> None:
        if not isinstance(value, Book):
            raise InvalidBookReferenceError("Книга должна быть объектом Book")
        self._book = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        if not isinstance(value, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        self._user = value

    @property
    def borrow_date(self) -> datetime:
        return self._borrow_date

    @borrow_date.setter
    def borrow_date(self, value: datetime) -> None:
        if value >= self._due_date:
            raise DateConsistencyError("Дата выдачи должна быть раньше срока возврата")
        self._borrow_date = value

    @property
    def due_date(self) -> datetime:
        return self._due_date

    @due_date.setter
    def due_date(self, value: datetime) -> None:
        if value <= self._borrow_date:
            raise DateConsistencyError("Срок возврата должен быть позже даты выдачи")
        self._due_date = value

    @property
    def return_date(self) -> Optional[datetime]:
        return self._return_date

    @return_date.setter
    def return_date(self, value: Optional[datetime]) -> None:
        if value and value < self._borrow_date:
            raise InvalidReturnDateError("Дата возврата не может быть раньше даты выдачи")
        self._return_date = value

     
    def is_overdue(self) -> bool:
        """Проверяет, просрочена ли книга"""
        current_date = datetime.now()
        if self._return_date:
            return self._return_date > self._due_date
        return current_date > self._due_date

    def get_days_overdue(self) -> int:
        """Возвращает количество дней просрочки"""
        if not self.is_overdue():
            return 0

        current_date = datetime.now()
        reference_date = self._return_date if self._return_date else current_date
        return (reference_date - self._due_date).days

    def is_returned(self) -> bool:
        """Проверяет, возвращена ли книга"""
        return self._return_date is not None

     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "record_id": self._record_id,
            "book_isbn": self._book.isbn,
            "user_id": self._user.user_id,
            "borrow_date": self._borrow_date.isoformat(),
            "due_date": self._due_date.isoformat(),
            "return_date": self._return_date.isoformat() if self._return_date else None
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any],
                  books_dict: Dict[str, Book] = None,
                  users_dict: Dict[str, User] = None) -> "BorrowRecord":
        """
        books_dict: словарь ISBN -> Book
        users_dict: словарь user_id -> User
        """
        if not books_dict or data["book_isbn"] not in books_dict:
            raise LibraryException(f"Книга с ISBN {data['book_isbn']} не найдена")
        if not users_dict or data["user_id"] not in users_dict:
            raise LibraryException(f"Пользователь с ID {data['user_id']} не найден")

        book = books_dict[data["book_isbn"]]
        user = users_dict[data["user_id"]]
        borrow_date = datetime.fromisoformat(data["borrow_date"])
        due_date = datetime.fromisoformat(data["due_date"])
        return_date = datetime.fromisoformat(data["return_date"]) if data["return_date"] else None

        return cls(
            record_id=data["record_id"],
            book=book,
            user=user,
            borrow_date=borrow_date,
            due_date=due_date,
            return_date=return_date
        )

    def __str__(self) -> str:
        status = "Возвращена" if self.is_returned() else "На руках"
        overdue = " (ПРОСРОЧЕНО)" if self.is_overdue() else ""
        return_date_str = self._return_date.strftime("%d.%m.%Y") if self._return_date else "не возвращена"

        return (f"ID записи: {self._record_id}\n"
                f"Книга: {self._book.title}\n"
                f"Пользователь: {self._user.name}\n"
                f"Дата выдачи: {self._borrow_date.strftime('%d.%m.%Y')}\n"
                f"Срок возврата: {self._due_date.strftime('%d.%m.%Y')}\n"
                f"Дата возврата: {return_date_str}\n"
                f"Статус: {status}{overdue}")


class Fine:
    """Класс штрафа за различные нарушения"""

    def __init__(self,
                 fine_id: str,
                 user: User,
                 borrow_record: BorrowRecord,
                 amount: float,
                 reason: str,
                 paid: bool = False) -> None:

        if not fine_id or not fine_id.strip():
            raise InvalidFineIDError("ID штрафа обязателен")
        if not isinstance(user, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        if not isinstance(borrow_record, BorrowRecord):
            raise InvalidFineReferenceError("Запись о заимствовании должна быть объектом BorrowRecord")
        if amount <= 0:
            raise InvalidFineAmountError("Сумма штрафа должна быть положительной")
        if not reason or not reason.strip():
            raise InvalidFineReasonError("Причина штрафа обязательна")

        self._fine_id = fine_id.strip()
        self._user = user
        self._borrow_record = borrow_record
        self._amount = amount
        self._reason = reason.strip()
        self._paid = paid

    @property
    def fine_id(self) -> str:
        return self._fine_id

    @fine_id.setter
    def fine_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidFineIDError("ID штрафа обязателен")
        self._fine_id = value.strip()

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        if not isinstance(value, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        self._user = value

    @property
    def borrow_record(self) -> BorrowRecord:
        return self._borrow_record

    @borrow_record.setter
    def borrow_record(self, value: BorrowRecord) -> None:
        if not isinstance(value, BorrowRecord):
            raise InvalidFineReferenceError("Запись о заимствовании должна быть объектом BorrowRecord")
        self._borrow_record = value

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float) -> None:
        if value <= 0:
            raise InvalidFineAmountError("Сумма штрафа должна быть положительной")
        self._amount = value

    @property
    def reason(self) -> str:
        return self._reason

    @reason.setter
    def reason(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidFineReasonError("Причина штрафа обязательна")
        self._reason = value.strip()

    @property
    def paid(self) -> bool:
        return self._paid

    @paid.setter
    def paid(self, value: bool) -> None:
        self._paid = value

     
    def pay_fine(self) -> None:
        """Отмечает штраф как оплаченный"""
        self._paid = True

     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "fine_id": self._fine_id,
            "user_id": self._user.user_id,
            "borrow_record_id": self._borrow_record.record_id,
            "amount": self._amount,
            "reason": self._reason,
            "paid": self._paid,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any],
                  users_dict: Dict[str, User] = None,
                  borrow_records_dict: Dict[str, BorrowRecord] = None) -> "Fine":
        """
        users_dict: словарь user_id -> User
        borrow_records_dict: словарь record_id -> BorrowRecord
        """
        if not users_dict or data["user_id"] not in users_dict:
            raise LibraryException(f"Пользователь с ID {data['user_id']} не найден")
        if not borrow_records_dict or data["borrow_record_id"] not in borrow_records_dict:
            raise LibraryException(f"Запись о заимствовании с ID {data['borrow_record_id']} не найдена")

        user = users_dict[data["user_id"]]
        borrow_record = borrow_records_dict[data["borrow_record_id"]]

        fine = cls(
            fine_id=data["fine_id"],
            user=user,
            borrow_record=borrow_record,
            amount=data["amount"],
            reason=data["reason"],
            paid=data["paid"]
        )
        return fine

    def __str__(self) -> str:
        status = "Оплачен" if self._paid else "Не оплачен"
        return (f"ID штрафа: {self._fine_id}\n"
                f"Пользователь: {self._user.name}\n"
                f"Книга: {self._borrow_record.book.title}\n"
                f"Сумма: {self._amount} руб.\n"
                f"Причина: {self._reason}\n"
                f"Статус: {status}\n")

class Reservation:
    """Класс резервирования книги"""

    def __init__(self,
                 reservation_id: str,
                 user: User,
                 book: Book,
                 reservation_date: datetime,
                 expiry_date: datetime) -> None:

        if not reservation_id or not reservation_id.strip():
            raise InvalidReservationIDError("ID резервирования обязателен")
        if not isinstance(user, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        if not isinstance(book, Book):
            raise InvalidBookReferenceError("Книга должна быть объектом Book")
        if expiry_date <= reservation_date:
            raise ReservationDateConsistencyError("Дата истечения резервирования должна быть позже даты создания")

        self._reservation_id = reservation_id.strip()
        self._user = user
        self._book = book
        self._reservation_date = reservation_date
        self._expiry_date = expiry_date
        self._active = True

     
    @property
    def reservation_id(self) -> str:
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidReservationIDError("ID резервирования обязателен")
        self._reservation_id = value.strip()

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        if not isinstance(value, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        self._user = value

    @property
    def book(self) -> Book:
        return self._book

    @book.setter
    def book(self, value: Book) -> None:
        if not isinstance(value, Book):
            raise InvalidBookReferenceError("Книга должна быть объектом Book")
        self._book = value

    @property
    def reservation_date(self) -> datetime:
        return self._reservation_date

    @reservation_date.setter
    def reservation_date(self, value: datetime) -> None:
        if value >= self._expiry_date:
            raise ExpireDateConsistencyError("Дата резервирования должна быть раньше даты истечения")
        self._reservation_date = value

    @property
    def expiry_date(self) -> datetime:
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value: datetime) -> None:
        if value <= self._reservation_date:
            raise ReservationDateConsistencyError("Дата истечения должна быть позже даты резервирования")
        self._expiry_date = value

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        self._active = value

     
    def cancel_reservation(self) -> None:
        """Отменяет резервирование"""
        self._active = False

    def activate_reservation(self) -> None:
        """Активирует резервирование (если было отменено)"""
        self._active = True

    def is_expired(self) -> bool:
        """Проверяет, истекло ли резервирование"""
        return datetime.now() > self._expiry_date

    def is_active(self) -> bool:
        """Проверяет, активно ли резервирование"""
        return self._active and not self.is_expired()

    def get_days_until_expiry(self) -> int:
        """Возвращает количество дней до истечения резервирования"""
        if not self.is_active():
            return 0
        return (self._expiry_date - datetime.now()).days

     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "reservation_id": self._reservation_id,
            "user_id": self._user.user_id,
            "book_isbn": self._book.isbn,
            "reservation_date": self._reservation_date.isoformat(),
            "expiry_date": self._expiry_date.isoformat(),
            "active": self._active
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any],
                  users_dict: Dict[str, User] = None,
                  books_dict: Dict[str, Book] = None) -> "Reservation":
        """
        users_dict: словарь user_id -> User
        books_dict: словарь ISBN -> Book
        """
        if not users_dict or data["user_id"] not in users_dict:
            raise LibraryException(f"Пользователь с ID {data['user_id']} не найден")
        if not books_dict or data["book_isbn"] not in books_dict:
            raise LibraryException(f"Книга с ISBN {data['book_isbn']} не найдена")

        user = users_dict[data["user_id"]]
        book = books_dict[data["book_isbn"]]
        reservation_date = datetime.fromisoformat(data["reservation_date"])
        expiry_date = datetime.fromisoformat(data["expiry_date"])

        reservation = cls(
            reservation_id=data["reservation_id"],
            user=user,
            book=book,
            reservation_date=reservation_date,
            expiry_date=expiry_date
        )
        reservation._active = data["active"]
        return reservation

    def __str__(self) -> str:
        status = "Активно" if self.is_active() else "Неактивно"
        expired = " (ИСТЕКЛО)" if self.is_expired() else ""
        return (f"ID резервирования: {self._reservation_id}\n"
                f"Книга: {self._book.title}\n"
                f"Пользователь: {self._user.name}\n"
                f"Дата резервирования: {self._reservation_date.strftime('%d.%m.%Y')}\n"
                f"Срок действия: {self._expiry_date.strftime('%d.%m.%Y')}\n"
                f"Статус: {status}{expired}\n"
                f"Дней до истечения: {self.get_days_until_expiry()}")

class Review:
    """Класс отзыва на книгу"""

    def __init__(self,
                 review_id: str,
                 user: User,
                 book: Book,
                 rating: int,
                 comment: str = "",
                 review_date: Optional[datetime] = None) -> None:

        if not review_id or not review_id.strip():
            raise InvalidReviewIDError("ID отзыва обязателен")
        if not isinstance(user, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        if not isinstance(book, Book):
            raise InvalidBookReferenceError("Книга должна быть объектом Book")
        if rating < 1 or rating > 5:
            raise InvalidRatingError("Рейтинг должен быть от 1 до 5")

        self._review_id = review_id.strip()
        self._user = user
        self._book = book
        self._rating = rating
        self._comment = comment.strip()
        self._review_date = review_date or datetime.now()

     
    @property
    def review_id(self) -> str:
        return self._review_id

    @review_id.setter
    def review_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidReviewIDError("ID отзыва обязателен")
        self._review_id = value.strip()

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        if not isinstance(value, User):
            raise InvalidUserReferenceError("Пользователь должен быть объектом User")
        self._user = value

    @property
    def book(self) -> Book:
        return self._book

    @book.setter
    def book(self, value: Book) -> None:
        if not isinstance(value, Book):
            raise InvalidBookReferenceError("Книга должна быть объектом Book")
        self._book = value

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, value: int) -> None:
        if value < 1 or value > 5:
            raise InvalidRatingError("Рейтинг должен быть от 1 до 5")
        self._rating = value

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, value: str) -> None:
        self._comment = value.strip()

    @property
    def review_date(self) -> datetime:
        return self._review_date

    @review_date.setter
    def review_date(self, value: datetime) -> None:
        self._review_date = value

     
    def is_positive(self) -> bool:
        """Проверяет, является ли отзыв положительным (4-5 баллов)"""
        return self._rating >= 4

    def is_negative(self) -> bool:
        """Проверяет, является ли отзыв отрицательным (1-2 балла)"""
        return self._rating <= 2

    def get_summary(self) -> str:
        """Возвращает краткое описание отзыва"""
        sentiment = "Положительный" if self.is_positive() else "Отрицательный" if self.is_negative() else "Нейтральный"
        return f"{sentiment} отзыв ({self._rating}/5): {self._comment[:50]}{'...' if len(self._comment) > 50 else ''}"

     
    def to_dict(self) -> Dict[str, Any]:
        return {
            "review_id": self._review_id,
            "user_id": self._user.user_id,
            "book_isbn": self._book.isbn,
            "rating": self._rating,
            "comment": self._comment,
            "review_date": self._review_date.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any],
                  users_dict: Dict[str, User] = None,
                  books_dict: Dict[str, Book] = None) -> "Review":
        """
        users_dict: словарь user_id -> User
        books_dict: словарь ISBN -> Book
        """
        if not users_dict or data["user_id"] not in users_dict:
            raise LibraryException(f"Пользователь с ID {data['user_id']} не найден")
        if not books_dict or data["book_isbn"] not in books_dict:
            raise LibraryException(f"Книга с ISBN {data['book_isbn']} не найдена")

        user = users_dict[data["user_id"]]
        book = books_dict[data["book_isbn"]]
        review_date = datetime.fromisoformat(data["review_date"])

        return cls(
            review_id=data["review_id"],
            user=user,
            book=book,
            rating=data["rating"],
            comment=data.get("comment", ""),
            review_date=review_date
        )

    def __str__(self) -> str:
        sentiment = "Положительный" if self.is_positive() else "Отрицательный" if self.is_negative() else "Нейтральный"
        return (f"ID отзыва: {self._review_id}\n"
                f"Книга: {self._book.title}\n"
                f"Пользователь: {self._user.name}\n"
                f"Рейтинг: {self._rating}/5 ({sentiment})\n"
                f"Комментарий: {self._comment or 'без комментария'}\n"
                f"Дата: {self._review_date.strftime('%d.%m.%Y %H:%M')}")

class Library:
    """Главный класс-менеджер библиотеки"""

    def __init__(self, name: str) -> None:
        if not name or not name.strip():
            raise InvalidLibraryNameError("Название библиотеки обязательно")

        self._name = name.strip()
        self._books: Dict[str, Book] = {}
        self._users: Dict[str, User] = {}
        self._authors: Dict[str, Author] = {}
        self._genres: Dict[str, Genre] = {}
        self._publishers: Dict[str, Publisher] = {}
        self._borrow_records: Dict[str, BorrowRecord] = {}
        self._fines: Dict[str, Fine] = {}
        self._reservations: Dict[str, Reservation] = {}
        self._reviews: Dict[str, Review] = {}

     
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidLibraryNameError("Название библиотеки обязательно")
        self._name = value.strip()

    @property
    def books(self) -> Dict[str, Book]:
        return self._books

    @property
    def users(self) -> Dict[str, User]:
        return self._users

    @property
    def authors(self) -> Dict[str, Author]:
        return self._authors

    @property
    def genres(self) -> Dict[str, Genre]:
        return self._genres

    @property
    def publishers(self) -> Dict[str, Publisher]:
        return self._publishers

    @property
    def borrow_records(self) -> Dict[str, BorrowRecord]:
        return self._borrow_records

    @property
    def fines(self) -> Dict[str, Fine]:
        return self._fines

    @property
    def reservations(self) -> Dict[str, Reservation]:
        return self._reservations

    @property
    def reviews(self) -> Dict[str, Review]:
        return self._reviews

    def add_book(self, book: Book) -> None:
        """Добавляет книгу в библиотеку"""
        if book.isbn in self._books:
            raise DuplicateItemError(f"Книга с ISBN {book.isbn} уже существует")
        self._books[book.isbn] = book

    def get_book(self, isbn: str) -> Optional[Book]:
        """Возвращает книгу по ISBN"""
        return self._books.get(isbn)

    def update_book(self, isbn: str, new_book: Book) -> None:
        """Обновляет информацию о книге"""
        if isbn not in self._books:
            raise ItemNotFoundError(f"Книга с ISBN {isbn} не найдена")
        self._books[isbn] = new_book

    def delete_book(self, isbn: str) -> None:
        """Удаляет книгу из библиотеки"""
        if isbn not in self._books:
            raise LibraryException(f"Книга с ISBN {isbn} не найдена")
        del self._books[isbn]

    def add_user(self, user: User) -> None:
        """Добавляет пользователя"""
        if user.user_id in self._users:
            raise LibraryException(f"Пользователь с ID {user.user_id} уже существует")
        self._users[user.user_id] = user

    def get_user(self, user_id: str) -> Optional[User]:
        """Возвращает пользователя по ID"""
        return self._users.get(user_id)

    def update_user(self, user_id: str, new_user: User) -> None:
        """Обновляет информацию о пользователе"""
        if user_id not in self._users:
            raise LibraryException(f"Пользователь с ID {user_id} не найден")
        self._users[user_id] = new_user

    def delete_user(self, user_id: str) -> None:
        """Удаляет пользователя"""
        if user_id not in self._users:
            raise LibraryException(f"Пользователь с ID {user_id} не найден")
        del self._users[user_id]

    def add_author(self, author: Author) -> None:
        """Добавляет автора"""
        if author.author_id in self._authors:
            raise LibraryException(f"Автор с ID {author.author_id} уже существует")
        self._authors[author.author_id] = author

    def get_author(self, author_id: str) -> Optional[Author]:
        """Возвращает автора по ID"""
        return self._authors.get(author_id)

    def add_genre(self, genre: Genre) -> None:
        """Добавляет жанр"""
        if genre.name in self._genres:
            raise LibraryException(f"Жанр с названием {genre.name} уже существует")
        self._genres[genre.name] = genre

    def get_genre(self, genre_name: str) -> Optional[Genre]:
        """Возвращает жанр по названию"""
        return self._genres.get(genre_name)

    def add_publisher(self, publisher: Publisher) -> None:
        """Добавляет издателя"""
        if publisher.publisher_id in self._publishers:
            raise LibraryException(f"Издатель с ID {publisher.publisher_id} уже существует")
        self._publishers[publisher.publisher_id] = publisher

    def get_publisher(self, publisher_id: str) -> Optional[Publisher]:
        """Возвращает издателя по ID"""
        return self._publishers.get(publisher_id)

    def add_borrow_record(self, record: BorrowRecord) -> None:
        """Добавляет запись о заимствовании"""
        if record.record_id in self._borrow_records:
            raise LibraryException(f"Запись с ID {record.record_id} уже существует")
        self._borrow_records[record.record_id] = record

    def get_borrow_record(self, record_id: str) -> Optional[BorrowRecord]:
        """Возвращает запись о заимствовании по ID"""
        return self._borrow_records.get(record_id)

    def add_fine(self, fine: Fine) -> None:
        """Добавляет штраф"""
        if fine.fine_id in self._fines:
            raise LibraryException(f"Штраф с ID {fine.fine_id} уже существует")
        self._fines[fine.fine_id] = fine

    def get_fine(self, fine_id: str) -> Optional[Fine]:
        """Возвращает штраф по ID"""
        return self._fines.get(fine_id)

    def add_reservation(self, reservation: Reservation) -> None:
        """Добавляет резервирование"""
        if reservation.reservation_id in self._reservations:
            raise LibraryException(f"Резервирование с ID {reservation.reservation_id} уже существует")
        self._reservations[reservation.reservation_id] = reservation

    def get_reservation(self, reservation_id: str) -> Optional[Reservation]:
        """Возвращает резервирование по ID"""
        return self._reservations.get(reservation_id)

    def add_review(self, review: Review) -> None:
        """Добавляет отзыв"""
        if review.review_id in self._reviews:
            raise LibraryException(f"Отзыв с ID {review.review_id} уже существует")
        self._reviews[review.review_id] = review

    def get_review(self, review_id: str) -> Optional[Review]:
        """Возвращает отзыв по ID"""
        return self._reviews.get(review_id)

    def borrow_book(self, user_id: str, isbn: str, due_date: datetime) -> BorrowRecord:
        """Выдает книгу пользователю"""
        user = self.get_user(user_id)
        book = self.get_book(isbn)

        if not user:
            raise LibraryException(f"Пользователь с ID {user_id} не найден")
        if not book:
            raise LibraryException(f"Книга с ISBN {isbn} не найдена")

        record_id = f"br_{len(self._borrow_records) + 1}"
        record = BorrowRecord(record_id, book, user, datetime.now(), due_date)

        self.add_borrow_record(record)
        user.borrow_book(book)

        return record

    def return_book(self, record_id: str) -> None:
        """Возвращает книгу в библиотеку"""
        record = self.get_borrow_record(record_id)
        if not record:
            raise LibraryException(f"Запись с ID {record_id} не найдена")

        record.return_date = datetime.now()
        record.user.return_book(record.book)

        if record.is_overdue():
            fine_id = f"fine_{len(self._fines) + 1}"
            days_overdue = record.get_days_overdue()
            amount = days_overdue * 10
            fine = Fine(fine_id, record.user, record, amount, f"Просрочка возврата на {days_overdue} дней")
            self.add_fine(fine)

    def search_books(self, title: str = "", author: str = "", genre: str = "") -> List[Book]:
        """Поиск книг по различным критериям"""
        results = []

        for book in self._books.values():
            matches_title = not title or title.lower() in book.title.lower()
            matches_author = not author or any(author.lower() in a.name.lower() for a in book.authors)
            matches_genre = not genre or genre.lower() in book.genre.name.lower()

            if matches_title and matches_author and matches_genre:
                results.append(book)

        return results

    def get_user_fines(self, user_id: str) -> List[Fine]:
        """Возвращает все штрафы пользователя"""
        return [fine for fine in self._fines.values() if fine.user.user_id == user_id and not fine.paid]

    def get_book_reviews(self, isbn: str) -> List[Review]:
        """Возвращает все отзывы на книгу"""
        return [review for review in self._reviews.values() if review.book.isbn == isbn]

    def get_average_book_rating(self, isbn: str) -> Optional[float]:
        """Возвращает средний рейтинг книги"""
        reviews = self.get_book_reviews(isbn)
        if not reviews:
            return None
        return sum(review.rating for review in reviews) / len(reviews)

    def get_statistics(self) -> Dict[str, Any]:
        """Возвращает статистику библиотеки"""
        return {
            "total_books": len(self._books),
            "total_users": len(self._users),
            "total_authors": len(self._authors),
            "active_borrows": len([r for r in self._borrow_records.values() if not r.is_returned()]),
            "overdue_books": len([r for r in self._borrow_records.values() if r.is_overdue()]),
            "active_reservations": len([r for r in self._reservations.values() if r.is_active()]),
            "unpaid_fines": len([f for f in self._fines.values() if not f.paid]),
            "total_reviews": len(self._reviews)
        }

     
    def to_dict(self) -> Dict[str, Any]:
        """Сохраняет всю библиотеку в словарь"""
        return {
            "name": self._name,
            "books": [book.to_dict() for book in self._books.values()],
            "users": [user.to_dict() for user in self._users.values()],
            "authors": [author.to_dict() for author in self._authors.values()],
            "genres": [genre.to_dict() for genre in self._genres.values()],
            "publishers": [publisher.to_dict() for publisher in self._publishers.values()],
            "borrow_records": [record.to_dict() for record in self._borrow_records.values()],
            "fines": [fine.to_dict() for fine in self._fines.values()],
            "reservations": [reservation.to_dict() for reservation in self._reservations.values()],
            "reviews": [review.to_dict() for review in self._reviews.values()]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Library':
        """Загружает всю библиотеку из словаря"""
        library = cls(data["name"])

        for author_data in data.get("authors", []):
            author = Author.from_dict(author_data)
            library.add_author(author)

        for genre_data in data.get("genres", []):
            genre = Genre.from_dict(genre_data)
            library.add_genre(genre)

        for publisher_data in data.get("publishers", []):
            publisher = Publisher.from_dict(publisher_data)
            library.add_publisher(publisher)

        authors_dict = {a.author_id: a for a in library._authors.values()}
        genres_dict = {g.name: g for g in library._genres.values()}
        publishers_dict = {p.publisher_id: p for p in library._publishers.values()}

        for book_data in data.get("books", []):
            book = Book.from_dict(book_data)
            library.add_book(book)

        books_dict = {b.isbn: b for b in library._books.values()}

        for user_data in data.get("users", []):
            user = User.from_dict(user_data, books_dict)
            library.add_user(user)

        users_dict = {u.user_id: u for u in library._users.values()}

        for record_data in data.get("borrow_records", []):
            record = BorrowRecord.from_dict(record_data, books_dict, users_dict)
            library.add_borrow_record(record)

        borrow_records_dict = {r.record_id: r for r in library._borrow_records.values()}

        for fine_data in data.get("fines", []):
            fine = Fine.from_dict(fine_data, users_dict, borrow_records_dict)
            library.add_fine(fine)

        for reservation_data in data.get("reservations", []):
            reservation = Reservation.from_dict(reservation_data, users_dict, books_dict)
            library.add_reservation(reservation)

        for review_data in data.get("reviews", []):
            review = Review.from_dict(review_data, users_dict, books_dict)
            library.add_review(review)

        return library

    def __str__(self) -> str:
        stats = self.get_statistics()
        return (f"Библиотека: {self._name}\n"
                f"Книги: {stats['total_books']}\n"
                f"Пользователи: {stats['total_users']}\n"
                f"Авторы: {stats['total_authors']}\n"
                f"Активные заимствования: {stats['active_borrows']}\n"
                f"Просроченные книги: {stats['overdue_books']}\n"
                f"Активные резервирования: {stats['active_reservations']}\n"
                f"Неоплаченные штрафы: {stats['unpaid_fines']}\n"
                f"Отзывы: {stats['total_reviews']}")

class Librarian(User):
    """Класс библиотекаря - расширенный пользователь с админ-правами"""

    def __init__(self,
                 user_id: str,
                 name: str,
                 employee_id: str,
                 department: str = "") -> None:

        super().__init__(user_id, name)

        if not employee_id or not employee_id.strip():
            raise InvalidEmployeeIDError("ID сотрудника обязателен")

        self._employee_id = employee_id.strip()
        self._department = department.strip()
        self._admin_rights = True

     
    @property
    def employee_id(self) -> str:
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value: str) -> None:
        if not value or not value.strip():
            raise InvalidEmployeeIDError("ID сотрудника обязателен")
        self._employee_id = value.strip()

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        self._department = value.strip()

    @property
    def admin_rights(self) -> bool:
        return self._admin_rights

     
    def add_book_to_library(self, library: Library, book: Book) -> None:
        """Добавляет книгу в библиотеку"""
        library.add_book(book)

    def remove_book_from_library(self, library: Library, isbn: str) -> None:
        """Удаляет книгу из библиотеки"""
        library.delete_book(isbn)

    def manage_fine(self, fine: Fine) -> None:
        """Управляет штрафом (отмечает оплаченным)"""
        fine.pay_fine()

    def cancel_reservation(self, reservation: Reservation) -> None:
        """Отменяет резервирование книги"""
        reservation.cancel_reservation()

    def add_new_user(self, library: Library, user_id: str, name: str) -> User:
        """Добавляет нового пользователя в библиотеку"""
        user = User(user_id, name)
        library.add_user(user)
        return user

    def process_book_return(self, library: Library, record_id: str) -> None:
        """Обрабатывает возврат книги"""
        library.return_book(record_id)

    def get_library_statistics(self, library: Library) -> Dict[str, Any]:
        """Возвращает статистику библиотеки"""
        return library.get_statistics()

     
    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict.update({
            "employee_id": self._employee_id,
            "department": self._department,
            "admin_rights": self._admin_rights
        })
        return base_dict

    @classmethod
    def from_dict(cls, data: Dict[str, Any], books_dict: Dict[str, Book] = None) -> "Librarian":
        """
        books_dict: словарь ISBN -> Book, чтобы восстановить ссылки на объекты книг
        """
        librarian = cls(
            user_id=data["user_id"],
            name=data["name"],
            employee_id=data["employee_id"],
            department=data.get("department", "")
        )

        if books_dict and "borrowed_books" in data:
            for isbn in data["borrowed_books"]:
                if isbn in books_dict:
                    librarian.borrow_book(books_dict[isbn])

        return librarian

    def __str__(self) -> str:
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"ID сотрудника: {self._employee_id}\n"
                f"Отдел: {self._department or 'не указан'}\n"
                f"Админ-права: {'Да' if self._admin_rights else 'Нет'}")
