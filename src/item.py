import csv
from src.Errorex import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)
        self.__class__.all.append(self)
        super().__init__()
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls, url='../src/items.csv'):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        try:
            with open(url, 'r', encoding='windows-1251') as file:
                file_reader = csv.DictReader(file, delimiter=',')
                for value in file_reader:
                    name, price, quantity = value.values()
                    if quantity is None:
                        raise InstantiateCSVError()
                    else:
                        cls(name, cls.string_to_number(price), cls.string_to_number(quantity))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except InstantiateCSVError as error:
            raise InstantiateCSVError('Файл item.csv поврежден')
    @staticmethod
    def string_to_number(number):
        return_number = float(number)
        return int(return_number)


    def __add__(self, other):
        """Метод сложения количества"""
        if not isinstance(other, Item):
            raise Exception("Складывать можно только наследников класса Item.")
        elif not isinstance(self, Item):
            raise Exception("Складывать можно только наследников класса Item.")

        return self.quantity + other.quantity