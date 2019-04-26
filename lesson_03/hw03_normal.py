__author__ = 'Зелепукин Алексей Юрьевич'

import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    numbers = []
    a, b = 0, 1
    for _ in range(m):
        numbers.append(b)
        a, b = b, a + b
    return numbers[n:m]


print(fibonacci(0, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    if len(origin_list) < 2:
        return origin_list
    n = 1
    while n < len(origin_list):
        swap_counter = 0
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                swap_counter += 1
        if swap_counter == 0:
            break
        n += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, iterable):
    return type(iterable)([item for item in iterable if func(item)])


print(my_filter(lambda x: x > 0, [2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def check_points(A, B, C, D):

    # Противолежащие стороны параллелограмма равны
    # Сумма квадратов диагоналей параллелограмма равна удвоенной сумме квадратов его двух смежных сторон
    # Диагонали параллелограмма пересекаются, и точка пересечения делит их пополам

    result_dict = {
        True: 'Точки являются вершинами параллелограмма',
        False: 'Точки не являются вершинами параллелограмма'
    }

    check_1, check_2, check_3 = False, False, False

    def vector_length(X, Y):
        return math.sqrt((Y[0] - X[0]) ** 2 + (Y[1] - X[1]) ** 2)

    AB = vector_length(A, B)
    BC = vector_length(B, C)
    CD = vector_length(C, D)
    AD = vector_length(A, D)

    if AB == CD and BC == AD:
        check_1 = True

    AC = vector_length(A, C)
    BD = vector_length(B, D)

    if AC ** 2 + BD ** 2 == 2 * (AB ** 2 + BC ** 2):
        check_2 = True

    O1 = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    O2 = ((B[0] + D[0]) / 2, (B[1] + D[1]) / 2)

    if O1 == O2:
        check_3 = True

    return result_dict[check_1 & check_2 & check_3]


# A1, A2, A3, A4 = (1, 2), (3, 4), (5, 6), (7, 8)
A1, A2, A3, A4 = (2, 3), (0, 2), (4, 1), (6, 2)

print(check_points(A1, A2, A3, A4))
