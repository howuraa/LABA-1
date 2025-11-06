from typing import List, Optional, Dict, Any
from datetime import datetime

class LibraryException(Exception):
    """Базовое исключение для всех ошибок библиотеки."""
    pass

class Author:
    """Класс автора книги"""
    
    def __init__(self, author_id: str, name: str, birth_year: Optional[int] = None):
        if not name.strip():
            raise LibraryException("Имя автора обязательно")
        self.author_id = author_id
        self.name = name
        self.birth_year = birth_year

class Genre:
    """Класс жанра книги"""
    
    def __init__(self, name: str, description: str = ""):
        if not name.strip():
            raise LibraryException("Название жанра обязательно")
        self.name = name
        self.description = description

class Publisher:
    """Класс издателя книги"""
    
    def __init__(self, publisher_id: str, name: str, location: Optional[str] = None):
        if not name.strip():
            raise LibraryException("Имя издателя обязательно")
        self.publisher_id = publisher_id
        self.name = name
        self.location = location

class Book:
    """Класс книги"""
    
    def __init__(self, isbn: str, title: str, authors: List[Author], genre: Genre,
                 publisher: Publisher, year: int, pages: Optional[int] = None):
        if not isbn.strip():
            raise LibraryException("ISBN обязателен")
        if not title.strip():
            raise LibraryException("Название книги обязательно")
        if not authors:
            raise LibraryException("Книга должна иметь авторов")
            
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.genre = genre
        self.publisher = publisher
        self.year = year
        self.pages = pages

class User:
    """Класс пользователя библиотеки"""
    
    def __init__(self, user_id: str, name: str):
        if not user_id.strip():
            raise LibraryException("ID пользователя обязателен")
        if not name.strip():
            raise LibraryException("Имя пользователя обязательно")
            
        self.user_id = user_id
        self.name = name
        self.borrowed_books: List[Book] = []

class BorrowRecord:
    """Класс записи о заимствовании книги"""
    
    def __init__(self, record_id: str, book: Book, user: User, 
                 borrow_date: datetime, due_date: datetime):
        self.record_id = record_id
        self.book = book
        self.user = user
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date: Optional[datetime] = None

class Library:
    """Главный класс-менеджер библиотеки"""
    
    def __init__(self, name: str):
        if not name.strip():
            raise LibraryException("Название библиотеки обязательно")
            
        self.name = name
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        self.borrow_records: Dict[str, BorrowRecord] = {}
    
    def add_book(self, book: Book) -> None:
        """Добавляет книгу в библиотеку"""
        if book.isbn in self.books:
            raise LibraryException(f"Книга с ISBN {book.isbn} уже существует")
        self.books[book.isbn] = book
    
    def add_user(self, user: User) -> None:
        """Добавляет пользователя"""
        if user.user_id in self.users:
            raise LibraryException(f"Пользователь с ID {user.user_id} уже существует")
        self.users[user.user_id] = user
    
    def borrow_book(self, user_id: str, isbn: str, due_date: datetime) -> BorrowRecord:
        """Выдает книгу пользователю"""
        user = self.users.get(user_id)
        book = self.books.get(isbn)
        
        if not user:
            raise LibraryException(f"Пользователь с ID {user_id} не найден")
        if not book:
            raise LibraryException(f"Книга с ISBN {isbn} не найдена")
        
        record_id = f"br_{len(self.borrow_records) + 1}"
        record = BorrowRecord(record_id, book, user, datetime.now(), due_date)
        
        self.borrow_records[record_id] = record
        user.borrowed_books.append(book)
        
        return record

