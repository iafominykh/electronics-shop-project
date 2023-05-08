from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, num_of_sim: int):
        super().__init__(name, price, quantity)
        self.__num_of_sim = num_of_sim

    @property
    def num_of_sim(self):
        return self.__num_of_sim

    @num_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:

            raise ValueError('Количеств физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__num_of_sim = value

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr.split(',')[0]}, {self.price}, {self.quantity}, {self.__num_of_sim})"