__author__ = 'Зелепукин Алексей Юрьевич'

import random

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

current_list = [1, 2, 4, 0]
new_list = [x**2 for x in current_list]

print(current_list)
print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_1 = ['банан', 'апельсин', 'яблоко', 'груша']
fruit_list_2 = ['киви', 'банан', 'персик', 'яблоко']

fruit_list_3 = [fruit for fruit in fruit_list_1 if fruit in fruit_list_2]

print(fruit_list_1)
print(fruit_list_2)
print(fruit_list_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a, b = -100, 100
n = 10
numbers = [random.randint(a, b) for _ in range(n)]
new_numbers = [x for x in numbers if x % 3 == 0 and x > 0 and x % 4 != 0]

print(numbers)
print(new_numbers)