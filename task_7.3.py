# Task 7.3
class Cell:
    def __init__(self, cellule):
        try:
            self.cellule = int(cellule)
            if cellule <= 0 or isinstance(cellule, float):
                raise ValueError

        except ValueError:
            print('This parameter should be positive integer number.')

    def make_order(self, cell, num_in_row):
        new_line = f''
        cell = cell.cellule
        while cell > 0:
            if cell > num_in_row:
                new_line += f'{"*" * num_in_row}\n'
                cell -= num_in_row
            else:
                new_line += f'{"*" * cell}\n'
                cell -= num_in_row
        return new_line

    def __add__(self, other):
        adding = self.cellule + other.cellule
        return Cell(adding)

    def __sub__(self, other):
        try:
            subtracting = self.cellule - other.cellule
            if self.cellule <= other.cellule:
                raise ValueError
            return Cell(subtracting)

        except ValueError:
            print('First attribute should be higher than second.\n'
                  'Biological cell can not occupy less than 1 cellule.')

    def __mul__(self, other):
        multiplying = self.cellule * other.cellule
        return Cell(multiplying)

    def __truediv__(self, other):
        truedivision = int(self.cellule / other.cellule)
        return Cell(truedivision)


try:
    a = Cell(11)
    b = Cell(5)
    c = (b + a)
    print(f'The new cell after summing up occupies {c.cellule} cellules.')
    d = (a - b)
    print(f'The new cell after subtracting occupies {d.cellule} cellules.')
    e = (a * b)
    print(f'The new cell after multiplying occupies {e.cellule} cellules.')
    f = (a / b)
    print(f'The new cell after division occupies {f.cellule} cellules.')
    print(b.make_order(a, 6))

except ZeroDivisionError:
    print('One of the parameters you typed in was "0".\n'
          'There were multiple mistakes in running the code.')

except AttributeError:
    print('One of the mathematical operations went wrong.')
