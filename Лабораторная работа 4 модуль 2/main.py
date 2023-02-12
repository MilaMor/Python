class Shoes:
    def __init__(self, brand: str, gender: str, size: int, price: int):
        """
            Создание и подготовка к работе объекта "Обувь"
            :param brand: Определение производителя
            :param gender: Определение гендерной принадлежности: муж/жен
            :param size: Размер обуви
            :param price: Цена обуви
            Примеры:
            >>> shoes = Shoes("Tamaris", "женская", 38, 5600)  # инициализация экземпляра класса
        """
        self._brand = brand
        self.gender = gender
        self.size = size
        self.price = price

    @property
    # Т.к атрибут brand пользователь не меняет ( пусть он находится на сайте одного бренда),
    # то закрепляем его свойством getter
    def brand(self) -> str:
        return self._brand

    def __str__(self):
        return f"Обувь бренда {self.brand}. Гендер {self.gender}. Размер {self.size}. Цена {self.price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, gender={self.gender!r}, size={self.size}, price={self.price})"

    def shoe_size(self, need_size: int) -> None:
        """
        Функция, проверяющая соответствие обуви требуему размеру
        :conv_size: Необходимый размер
        :return: Подходит ли одежда
        Примеры:
        >>> shoes = Shoes("Tamaris", "женская", 38, 5600)
        >>> shoes.shoe_size(39)
        """
        ...

    def shoes_price(self, max_price: (int, float)) -> None:
        """
        Устанавливаем ограничение по максимальному ценовому диапазону
        :max_price: Максимальная цена
        :raise ValueError: Вызов ошибки при превышении максимальной цены
        Примеры:
        >>> shoes = Shoes("Tamaris", "женская", 38, 5600)
        >>> shoes.shoes_price(6000)
        """
        ...

class Chelsea(Shoes):
    def __init__(self, brand: str, gender: str, size: int, price: int, promo_code: str):
        """
            Челси - дочерний класс Обуви.
            :param promo_code: Возможность ввода помокода для реализации сезонной скидки
        """
        super().__init__(brand, gender, size, price)
        self.promo_code = promo_code

    #Перегружаем методы __str__ и __repr__  так как в них добавили новый параметр - промокод (который не учитывается в данных методах, но используется дальше).
    def __str__(self) -> str:
        return f"Обувь бренда {self.brand}. Гендер {self.gender}. Размер {self.size}. Цена {self.price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, gender={self.gender!r}, size={self.size}, price={self.price})"

    # Метод shoe_size может унаследоваться

    def shoes_price(self, max_price: (int, float)) -> None:
        """
        Устанавливаем ограничение по максимальному ценовому диапазону, но при наличии
        промокода следует произвести пересчет цены
        :max_price: Максимальная цена
        :raise ValueError: Вызов ошибки при превышении максимальной цены
        Примеры:
        >>> chelsea = Chelsea("Tamaris", "женская", 38, 5600, "TSALE20")
        >>> chelsea.shoes_price(6000)
        """
        ...

if __name__ == "__main__":
    shoes = Shoes("Tamaris", "женская", 38, 5600)
    chelsea = Chelsea("Tamaris", "женская", 38, 5600, "TSALE20")

    print(shoes)
    print(chelsea)
    print(book3)

    print(shoes.__repr__())
    print(chelsea.__repr__())
    pass
