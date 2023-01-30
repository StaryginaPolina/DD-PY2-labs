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

    def __str__(self) -> str:
        """
        Функция которая возвращает строку с названием книги

        :return: Книга "Название книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Функция которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.

        :return: [Book(id_=..., name='...', pages=...)]
        """
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
# end
