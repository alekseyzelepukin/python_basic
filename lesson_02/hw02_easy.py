from random import seed, randint

__author__ = 'Зелепукин Алексей Юрьевич'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

for idx, fruit in enumerate(fruits, start=1):
    print('{0:}. {1:>6}'.format(idx, fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = list(range(10))
second_list = list(range(0, 10, 2))

print(first_list)
print(second_list)

for item in first_list:
    if item in second_list:
        first_list.remove(item)

print(first_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

n = 10

seed(42)
numbers = [randint(0, 99) for _ in range(n)]

print(numbers)

new_numbers = []

for number in numbers:
    if number % 2 == 0:
        new_numbers.append(number / 4)
    else:
        new_numbers.append(number * 2)

print(new_numbers)
