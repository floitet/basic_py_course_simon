# Task 7.2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, brand, name, size_height):
        self.brand = brand
        self.name = name
        self.size_height = size_height

    @abstractmethod
    def fabric_flow(self):
        pass


class Coat(Clothes):

    @property
    def size_height(self):
        return self.__size_height

    @size_height.setter
    def size_height(self, size_height):
        if size_height > 60:
            self.__size_height = 60
        elif size_height < 44:
            self.__size_height = 44
        else:
            self.__size_height = size_height

    def fabric_flow(self):
        global result1
        result1 = self.size_height / 6.5 + 0.5
        return f"Your coat's size is {self.size_height}." \
               f"The length of fabric required to make {self.name} from {self.brand} equals {result1} meters."
        # return result1

coat = Coat('Armani', 'stylish coat', 65)
print(coat.fabric_flow())


class Suit(Clothes):

    @property
    def size_height(self):
        return self.__size_height

    @size_height.setter
    def size_height(self, size_height):
        if size_height > 220:
            self.__size_height = 220
        elif size_height < 150:
            self.__size_height = 150
        else:
            self.__size_height = size_height

    def fabric_flow(self):
        global result2
        result2 = self.size_height * 2 + 0.3
        return f"Your suit's height is {self.size_height}." \
               f"The length of fabric required to make {self.name} from {self.brand} equals {result2} meters."
        # return result2



    def __add__(self, other):
        return (self.size_height * 2 + 0.3) + (other.size_height / 6.5 + 0.5)


suit = Suit('Versace', 'formal suit', 300)
print(suit.fabric_flow())
# подчет общей суммы можно сделать тремя способами:
# 1) через перегрузку __add__
print(suit + coat)
# 2) сделав переменные из классов глобальными
print(result1 + result2)
# 3) либо просто из метода fabric_flow возвращать переменную и дальше ее использовать в сложении
# print(coat.fabric_flow() + suit.fabric_flow())
