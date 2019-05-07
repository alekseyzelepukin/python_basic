__author__ = 'Зелепукин Алексей Юрьевич'

import os
import sys
import shutil

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создать копию указанного файла")
    print("rm <file_name> - удалить указанный файл")
    print("cd <full_path or relative_path> - изменить текущую директорию на указанную")
    print("ls - отобразить полный путь текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir_name)
    split_text = os.path.splitext(file_path)
    if os.path.isfile(file_path):
        shutil.copy(file_path, os.path.join(os.getcwd(), '{}_copy{}'\
                    .format(split_text[0], split_text[1])))
        print('Файл {} успешно скопирован'.format(dir_name))
    else:
        print('Копируемый объект не является файлом')


def rm():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), dir_name)
    if os.path.isfile(file_path):
        user_input = input('Вы уверенны, что хотите удалить файл "{}"? [Y/N]'.format(dir_name))
        if user_input == 'Y':
            os.remove(file_path)
            print('Файл {} успешно удален'.format(dir_name))
        elif user_input == 'N':
            print('Операци удаления файла {} отменена'.format(dir_name))
            return
        else:
            print('Неверный ввод')
            return
    else:
        print('Удаляемый объект не является файлом')


def cd():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir_name)
    try:
        os.chdir(dir_path)
        print('Успешный переход в директорию {}'.format(dir_name))
    except FileNotFoundError:
        print('Директории {} не существует'.format(dir_name))


def print_path():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": print_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
