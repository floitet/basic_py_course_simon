# Task 6.3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position):
        income = {
            "Simon Troyanovskiy": [150000, 30000],
            "Jason Statham": [300000, 12000],
            "Chris Moneymaker": [100000, 80000]
        }

        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        global full_name
        full_name = f"{self.name} {self.surname}"
        return full_name

    def income(self):
        return f"This employees' total wage equals {sum(self._income[full_name])}."


b = Position('Jason', 'Statham', 'Actor')
print(b.get_full_name())
print(b.income())
