class Film:
    """ Базовый класс фильм.
    Продолжительность фильма указывается в минутах"""
    def __init__(self, name: str, length: int):
        self._name = name  # Название не должно подвергаться изменениям
        self.length = length

    def __str__(self):
        return f"Название {self._name}. Время просмотра {self.length}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, length={self.length!r})"

    def advertising(self) -> int:
        "Определяет количество рекламных пауз для фильма"
        return int(self.length / 20)

    def hours(self) -> float:
        "Переводит время просмотра всего фильма в часы"
        i = self.length / 60
        return round(i, 2)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        self._name = name

    @property
    def length(self) -> int:
        return self.length

    @length.setter
    def length(self, length: int) -> None:
        if not isinstance(length, int):
            raise TypeError
        if length <= 0:
            raise ValueError
        self.length = length


class Serial(Film):
    """ Сериал (серийный фильм). """
    def __init__(self, name: str, length: int, number_of_series: int):
        super().__init__(name, length)
        self.number_of_series = number_of_series

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self.length!r}), number_of_series={self.number_of_series!r})"

    def hours(self) -> float:
        "Переводит время просмотра всего фильма в часы. Для сериала необходимо учесть количество всех серий."
        i = self.length * self.number_of_series / 60
        return round(i, 2)

    @property
    def number_of_series(self) -> int:
        return self.number_of_series

    @number_of_series.setter
    def number_of_series(self, number_of_series: int) -> None:
        if not isinstance(number_of_series, int):
            raise TypeError
        if number_of_series <= 0:
            raise ValueError
        self.number_of_series = number_of_series


if __name__ == "__main__":
    # Write your solution here
    pass
# end
