__author__ = 'Зелепукин Алексей Юрьевич'

import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Figure():
    @staticmethod
    def _vector_length(x, y):
        return math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2))


class Triangle(Figure):
    def __init__(self, a, b, c):
        # точки:
        self.a = a
        self.b = b
        self.c = c
        # длины сторон:
        self.__a = super()._vector_length(self.b, self.c)
        self.__b = super()._vector_length(self.a, self.c)
        self.__c = super()._vector_length(self.a, self.b)

    def perimeter(self):
        return round(self.__a + self.__b + self.__c, 4)

    def area(self):
        p = 1/2 * self.perimeter()
        return round(math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)), 4)

    def height(self):
        """
        :return: кортеж высот, проведенных из каждой вершины на противолежащую сторону треугольника
        """
        dbl_area = 2 * self.area()
        sides = [self.__a, self.__b, self.__c]
        return tuple(map(lambda x: round(dbl_area / x, 4), sides))


triangle = Triangle(a=(3, 2), b=(6, 7), c=(0, 12))
print(triangle.area())
print(triangle.height())
print(triangle.perimeter())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium(Figure):
    def __init__(self, a, b, c, d):
        # точки:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        # длины сторон:
        self.__a = super()._vector_length(self.b, self.c)
        self.__b = super()._vector_length(self.a, self.d)
        self.__c = super()._vector_length(self.a, self.b)
        self.__d = super()._vector_length(self.c, self.d)

    def is_isosceles_trapezium(self):
        ac, bd = super()._vector_length(self.a, self.c), super()._vector_length(self.b, self.d)
        result = False
        if ac == bd:
            result = True
        else:
            result = False
        return result

    def side_lengths(self):
        """
        :return: кортеж длин сторон трапеции
        """
        sides = [self.__c, self.__a,  self.__d, self.__b]
        return tuple(map(lambda x: round(x, 4), sides))

    def perimeter(self):
        return round(self.__a + self.__b + self.__c + self.__d, 4)

    def area(self):
        a, b, c, d = self.__a, self.__b, self.__c, self.__d
        m = 1/2 * (a + b)
        r = math.sqrt(c ** 2 - (((b - a) ** 2 + c ** 2 - d ** 2) / (2 * (b - a))) ** 2)
        return round(m * r, 4)


# равнобедренной трапеции

trapezium = Trapezium((3, 2), (6, 7), (12, 7), (15, 2))
print(trapezium.is_isosceles_trapezium())
print(trapezium.side_lengths())
print(trapezium.perimeter())
print(trapezium.area())
