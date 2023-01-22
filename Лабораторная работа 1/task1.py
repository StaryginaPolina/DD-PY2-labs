# TODO Написать 3 класса с документацией и аннотацией типов
class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        """
        ...

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.

        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """


class House:
    def __init__(self, number_of_flors: int, number_of_entrsnces: int):
        """
        Создание и подготовка к работе объекта "Дом"

        :param number_of_flors: Количество этажей
        :param number_of_entrsnces: Количество подъездов

        Примеры:
        >>> house = House(5, 3)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_flors, (int)):
            raise TypeError  # Количество этажей целое
        if number_of_flors < 1:
            raise ValueError  # Количество этажей больше 1
        self.number_of_flors = number_of_flors  # Количество этажей

        if not isinstance(number_of_entrsnces, (int)):
            raise TypeError  # Количество подъездов целое
        if number_of_entrsnces < 1:
            raise ValueError  # Количество подъездов больше 1
        self.number_of_entrsnces = number_of_entrsnces  # Количество подъездов

    def add_flors(self, flors: int) -> None:
        """
        Достраивание этажей

        :param flors: Сколько этажей строим
        :raise ValueError: Если количество этажей не целое или меньше 1

        Примеры:
        >>> house = House(5, 3)
        >>> house.add_flors(2)
        """
        if not isinstance(flors, (int)):
            raise TypeError("Количество этажей целое")
        if flors < 1:
            raise ValueError("Количество этажей меньше 1")
        ...

    def add_entrsnces(self, entrsnces: int) -> None:
        """
        Достраивание подъездов

        :param entrsnces: Сколько этажей строим
        :raise ValueError: Если количество подъездов не целое или меньше 1

        Примеры:
        >>> house = House(6, 8)
        >>> house.add_entrsnces(20)
        """
        if not isinstance(entrsnces, (int)):
            raise TypeError("Количество подъездов целое целое")
        if entrsnces < 1:
            raise ValueError("Количество подъездов целое меньше 1")
        ...


class Telephone_tariff:
    def __init__(self, number_of_minutes: int, number_of_sms: int, number_of_gigabyte: (int, float)):
        """
        Создание и подготовка к работе объекта "Телефонный тариф"

        :param number_of_minutes: Количество минут
        :param number_of_sms: Количество смс
        :param number_of_gigabyte: Количество гигабайт интернета

        Примеры:
        >>> tariff = Telephone_tariff(500, 200, 0)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_minutes, (int)):
            raise TypeError  # Количество минут целое
        if number_of_minutes < 0 or number_of_minutes > 5000:
            raise ValueError  # Количество минут от 0 до 5000
        self.number_of_minutes = number_of_minutes  # Количество минут

        if not isinstance(number_of_sms, (int)):
            raise TypeError  # Количество смс целое
        if number_of_sms < 0 or number_of_sms > 1000:
            raise ValueError  # Количество смс от 0 до 1000
        self.number_of_sms = number_of_sms  # Количество смс

        if not isinstance(number_of_gigabyte, (int, float)):
            raise TypeError  # Количество гигабайт десятичное
        if number_of_gigabyte < 0 or number_of_gigabyte > 100:
            raise ValueError  # Количество гигабайт от 0 до 100
        self.number_of_gigabyte = number_of_gigabyte  # Количество гигабайт

    def add_minutes(self, minutes: (int)):
        """
        Добавим минут в тариф

        :param minutes: Сколько минут добавим
        :raise ValueError: Если количество минут превышает 5000 или меньше 0

        Примеры:
        >>> telephone_tariff = Telephone_tariff(0, 0, 50.2)
        >>> telephone_tariff.add_minutes(5)
        """
        if not isinstance(minutes, (int)):
            raise TypeError("Количество минут целое")
        if minutes < 0:
            raise ValueError("Количество добавляемых не может быть отрицательным")
        ...

    def add_sms(self, sms: (int)):
        """
        Добавим смс в тариф

        :param sms: Сколько смс добавим
        :raise ValueError: Если количество смс превышает 1000 или меньше 0

        Примеры:
        >>> telephone_tariff = Telephone_tariff(700, 600, 20)
        >>> telephone_tariff.add_sms(100)
        """
        ...

    def add_gigabyte(self, gigabyte: (int, float)):
        """
        Добавим гигабайтов в тариф

        :param sms: Сколько гигабайт добавим
        :raise ValueError: Если количество гигабайт превышает 100 или меньше 0

        Примеры:
        >>> telephone_tariff = Telephone_tariff(500, 0, 65)
        >>> telephone_tariff.add_gigabyte(10.5)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
# end
