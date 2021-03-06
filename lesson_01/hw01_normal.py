__author__ = 'Зелепукин Алексей Юрьевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# while
x = 58375

print(x)

max_num = 0

while x > 0:
    n = x % 10
    if n > max_num:
        max_num = n
    x //= 10

print(max_num)

# for
x = 58375

print(x)

max_num = 0

for i in str(x):
    n = int(i)
    if n > max_num:
        max_num = n

print(max_num)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# math
a = int(input('Введите число: '))
b = int(input('Введите число: '))

print(f'a = {a}, b = {b}')

a = a - b
b = a + b
a = -a + b

print(f'a = {a}, b = {b}')

# python tuples
a = int(input('Введите число: '))
b = int(input('Введите число: '))

print(f'a = {a}, b = {b}')

a, b = b, a

print(f'a = {a}, b = {b}')

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

print(f'a = {a}, b = {b}, c = {c}')

D = b ** 2 - 4 * a * c

if D < 0:
    print('Дискриминант меньше нуля, действительных корней нет')
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
