# Task 6.5
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.title)
        print('Launching drawing.')

obj = Stationery('Unknown object.')
obj.draw()

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Working on an {self.title}.')
        print('Writing a word.')

gel_black_pen = Pen('essay')
gel_black_pen.draw()

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Working on a {self.title}.')
        print('Drawing a thin line.')

sharp_pencil = Pencil('portret')
sharp_pencil.draw()

class Marker(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Working on a {self.title}.')
        print('Highlighting important info.')

red_thick_marker = Marker('summary')
red_thick_marker.draw()