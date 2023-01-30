from typing import Optional

from pydantic import BaseModel, conint

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
    Создание и подготовка к работе объекта "Книга"

    :param id_: Идентификатор книги
    :param name: Название книги
    :param pages: Количество страниц в книге
    """
    name: str
    id_: int
    pages: conint(gt=0)


class Library(BaseModel):
    """
    Создание и подготовка к работе объекта "Библиотека"

    :param books: Список книг
    """
    books: Optional[list]

    def get_next_book_id(self) -> int:
        """
        Функция которая возвращает идентификатор для добавления новой книги в библиотеку

        :return: int
        """
        if self.books is None:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Функция которая возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса

        :return: int
        """
        for i, key in enumerate(self.books):
            if key.id_ == id_:
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
# end
