__author__ = 'Зелепукин Алексей Юрьевич'

import os
import hw05_easy

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def my_utility():
    print('\n')
    print('*' * 32 + ' BEGIN ' + '*' * 32)
    print('\n')
    ans = None
    while ans != 5:
        print('Текущая папка: ' + os.path.basename(os.getcwd()))
        ans = int(input('Выберите действие (введите число):\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n'))
        if ans == 5:
            print('\n')
            print('*' * 32 + ' END ' + '*' * 32)
            print('\n')
            break
        elif ans == 1:
            path_name = input('Введите название папки для перехода: ')
            if hw05_easy.change_dir(path_name):
                print(f'Успешный переход в папку {os.path.basename(path_name)}')
            else:
                print(f'Не удалось перейти в папку {os.path.basename(path_name)}')
        elif ans == 2:
            print(f'Содержимое текущей папки: {hw05_easy.list_dir(mode="a")}')
        elif ans == 3:
            name = input('Введите название удаляемой папки: ')
            if hw05_easy.remove_dir(name):
                print(f'Папка {name} успешно удалена')
            else:
                print(f'Не удалось удалить папку {name}')
        elif ans == 4:
            name = input('Введите название новой папки: ')
            if hw05_easy.make_dir(name):
                print(f'Папка {name} успешно создана')
            else:
                print(f'Не удалось создать папку {name}')
        else:
            print('Неверный ввод. Попробуйте еще раз.')
        print('\n')


my_utility()
