import doctest


class LightBulb:
    def __init__(self, type_of_lighting: str, colour_temperature: str):
        """
        Создание и подготовка к работе объекта "Лампочка"
        :param type_of_lighting: Тип источника света
        :param colour_temperature: Цветовая температура
        Примеры:
        >>> light_bulb = LightBulb("Светодиодная", "Теплый белый")  # инициализация экземпляра класса
        """
        if not isinstance(type_of_lighting, str):
            raise TypeError("Тип источника света должен быть типа str")
        self.type_of_lighting = type_of_lighting

        if not isinstance(colour_temperature, str):
            raise TypeError("Цветовая температура должна быть типа str")
        self.colour_temperature = colour_temperature

    def smart_lump(self) -> bool:
        """
        Функция, которая проверяет, является ли лампочка умной
        :return: Умная ли лампочка
        Примеры:
        >>> light_bulb = LightBulb("Светодиодная", "Теплый белый")
        >>> light_bulb.smart_lump()
        """
        ...

    def lamp_price(self, max_price: (int, float)) -> None:
        """
        Устанавливаем ограничение по максимальному ценовому диапазону
        :max_price: Максимальная цена
        :raise ValueError: Вызов ошибки при превышении максимальной цены
        Примеры:
        >>> light_bulb = LightBulb("Светодиодная", "Теплый белый")
        >>> light_bulb.lamp_price(400)
        """
        if not isinstance(max_price, (int, float)):
            raise TypeError("Максимальная цена должна быть типа int или float")
        if max_price< 0:
            raise ValueError("Максимальная цена должна положительным числом")
        ...


class Window:
    def __init__(self, material: str, opened: bool):
        """
        Создание и подготовка к работе объекта "Окно"
        :param material: Материал рамы окна
        :param opened: Окно открыто (True) или закрыто (False)
        Примеры:
        >>> window = Window("Дерево", False)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал рамы окна должен быть типа str")
        self.material = material

        if not isinstance(opened, bool):
            raise TypeError("Характеристика (открыто/закрыто) должна быть типа bool")
        self.opened = opened

    def check_opened(self) -> bool:
        """
        Функция, которая проверяет, является ли окно открытым
        :return: Открыто ли окно
        Примеры:
        >>> window = Window("Дерево", False)
        >>> window.check_opened()
        """
        ...

    def pb_material(self, safe_material: str) -> None:
        """
        Функция, которая проверяет, является ли материал рамы окна пожаробезопасным
        :safe_material: Пожаробезопасный материал
        :return: Подходит ли материал рамы окна по пожарной безопасности
        Примеры:
        >>> window = Window("Дерево", False)
        >>> window.pb_material("Алюминевый каркас")
        """
        if not isinstance(safe_material, str):
            raise TypeError("Пожаробезопасный материал должен быть типа str")
        ...


class Oceanarium:
    def __init__(self, area: int, water_volume: (int, float), fish_population: int):
        """
        Создание и подготовка к работе объекта "Океанариум"
        :param area: Площадь океанариума, м^2
        :param water_volume: Общий объем воды , млн литров
        :param fish_population: Кол-во обитамемых экземпляров, шт
        Примеры:
        >>> spb_oceanarium = Oceanarium(5000, 1.5, 4500)  # инициализация экземпляра класса
        """
        if not isinstance(area, int):
            raise TypeError("Площадь океанариума должна быть типа int")
        if area <= 0:
            raise ValueError("Площадь океанариума должна быть положительным числом")
        self.area = area

        if not isinstance(water_volume, (int, float)):
            raise TypeError("Объем океанариума должен быть типа int или float")
        if water_volume <= 0:
            raise ValueError("Объем океанариума должен быть положительным числом")
        self.water_volume = water_volume

        if not isinstance(fish_population, int):
            raise TypeError("Кол-во экземпляров должно быть типа int")
        if fish_population < 1:
            raise ValueError("Кол-во экземпляров должно быть положительным числом")
        self.fish_population = fish_population

    def top_volume_of_world(self) -> bool:
        """
        Функция, которая проверяет, входит ли океанариум в топ-10 мира по общему литражу обслуживаемой воды
        :return: Входит ли океанариум в топ-10 мира по общему литражу
        Примеры:
        >>> spb_oceanarium = Oceanarium(5000, 1.5, 4500)
        >>> spb_oceanarium.top_volume_of_world()
        """
        ...

    def fish_population_growth(self, fish_population_growth: int) -> None:
        """
        Прирост кол-ва экземпляров рыб за год
        :fish_population_growth: Прирост кол-ва экземпляров рыб за год
        :return: Общее кол-во обитателей океанариума
        Примеры:
        >>> spb_oceanarium = Oceanarium(5000, 1.5, 4500)
        >>> spb_oceanarium.fish_population_growth(150)
        """
        if not isinstance(fish_population_growth, int):
            raise TypeError("Прирост кол-ва экземпляров рыб за год должен быть типа int")
        # нет проверки отрицательности вводимого числа по причине наличия вероятности "отрицательного прироста"
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
