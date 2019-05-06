__author__ = 'Зелепукин Алексей Юрьевич'

import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dir(name):
    path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(path)
        return True
    except FileExistsError:
        return False


def remove_dir(name):
    path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(path)
        return True
    except FileExistsError:
        return False


# names = ['dir_' + str(i) for i in range(1, 10)]
# print(os.listdir(os.getcwd()))
# for name in names:
#     make_dir(name)
# print(os.listdir(os.getcwd()))
# for name in names:
#     remove_dir(name)
# print(os.listdir(os.getcwd()))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir(path=os.getcwd(), mode='d'):
    output_list = []
    content = os.listdir(path)
    if mode == 'a':
        output_list = content
    elif mode == 'd':
        for item in content:
            if os.path.isdir(item):
                output_list.append(item)
    elif mode == 'f':
        for item in content:
            if os.path.isfile(item):
                output_list.append(item)
    else:
        output_list = content
    return output_list


# print(list_dir())
# for name in names:
#     make_dir(name)
# print(list_dir())
# for name in names:
#     remove_dir(name)
# print(list_dir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file(file_path=os.path.realpath(__file__)):
    i = 1
    file_name = os.path.basename(file_path)
    copy_name = 'copy' + '0' + str(i) + '_' + file_name if i < 10 else 'copy' + str(i) + '_' + file_name
    while os.path.isfile(copy_name):
        i += 1
        copy_name = 'copy' + '0' + str(i) + '_' + file_name if i < 10 else 'copy' + str(i) + '_' + file_name
    else:
        shutil.copy(os.path.join(os.path.dirname(file_path), file_name),
                    os.path.join(os.path.dirname(file_path), copy_name))
        return True


# copy_file()


def change_dir(path):
    try:
        os.chdir(path)
        return True
    except FileNotFoundError:
        return False


