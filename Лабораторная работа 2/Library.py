from pydantic import BaseModel, conint, constr
from typing import List, Optional
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book(BaseModel):
    """
    Объект "Книга"
    :param id_: уникальный номер книги
    :param name: название книги
    :param pages: количество страниц
    """
    id_: conint(gt=0) # говорит о том, что атрибут id для всех эекземпляров должен быть типа int,  больше 0
    name: constr(min_length=1) # говорит о том, что атрибут name для всех эекземпляров должен быть типа str, а его длина больше одного знака
    pages: conint(gt=0) # говорит о том, что атрибут pages для всех эекземпляров должен быть типа int, больше 0

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library(BaseModel):
    """
    Объект "Библиотека"
    :param books: список книг, созданный из классов Book
    """
    books: Optional[List[Book]] = []

    def get_next_book_id(self) -> int:
        """
        Для получения идентификатора книги
        """
        if len(self.books) <= 0:
            return 1
        return self.books[-1].id_ + 1 # прибавляем +1 к ID элемента с конца

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Для поиска книги с нужным индексом
        """
        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
