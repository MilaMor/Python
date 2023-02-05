class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property # Т.к атрибут name пользователь не меняет, то закрепляем его свойством getter
    def name(self) -> str:
        return self._name

    @property  # Т.к атрибут author пользователь не меняет, то закрепляем его свойством getter
    def author(self) -> str:
        return self._author

    def __str__(self): # для других классов метод был убран из соображений, что название и автор остается одинаков для всех
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter  # В свойстве setter организовываем проверку по типу и допустимым значениям
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Кол-во страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Кол-во страниц не может быть меньше или равно нулю")
        self._pages = pages
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter  # В свойстве setter организовываем проверку по типу и допустимым значениям
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность не может быть меньше или равно нулю")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration}h)"

if __name__ == '__main__':
    book1 = Book("Гордость и Предубеждение", "Джейн Остин")
    book2 = PaperBook("Гордость и Предубеждение", "Джейн Остин", 200)
    book3 = AudioBook("Гордость и Предубеждение", "Джейн Остин", 11.2)

    print(book1)
    print(book2)
    print(book3)

    print(book1.__repr__())
    print(book2.__repr__())
    print(book3.__repr__())