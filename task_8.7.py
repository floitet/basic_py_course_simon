# Task 8.7

class ComplexNumber:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        adding_complex = self.complex_num + other.complex_num
        return ComplexNumber(adding_complex)

    def __mul__(self, other):
        multiplying_complex = self.complex_num * other.complex_num
        return ComplexNumber(multiplying_complex)


a = ComplexNumber(10 + 7j)
print(type(a.complex_num))
print(a.complex_num)
b = ComplexNumber(complex(15, 2e-2))
print(type(b.complex_num))
print(b.complex_num)
c = a + b
d = a * b
print(c.complex_num)
print(d.complex_num)
