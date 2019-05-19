# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число, компьютер сообщают о количестве «быков» и «коров»
# в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».


import random


class Game:
    def __init__(self):
        self._number = self._guess_number()
        self._score = {'Bulls': 0, 'Cows': 0}
        self._counter = 0
        self._result = False

    def __str__(self):
        return str(self._score)

    @staticmethod
    def info():
        print(
            'Правила:\n\
            Компьютер загадывает четырехзначное число, все цифры которого различны\n\
            (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.\n\
            Игрок вводит четырехзначное число, компьютер сообщают о количестве «быков» и «коров»\n\
            в названном числе\n\
            «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,\n\
                  что и в задуманном числе\n\
            «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,\n\
                  что и в задуманном числе\n'
            )

    @staticmethod
    def _guess_number():
        n = random.randint(1000, 9999)
        while True:
            if len(set(str(n))) == 4:
                break
            n = random.randint(1000, 9999)
        return n

    @property
    def guessed_number(self):
        return self._number

    def _update_score(self, bulls, cows):
        self._score['Bulls'] = bulls
        self._score['Cows'] = cows

    def _check_bulls(self, bulls):
        result = False
        if bulls == 4:
            result = True
        self._result = result

    def check_number(self, number):
        self._counter += 1
        bulls, cows = 0, 0
        suggested_number, guessed_number = str(number), str(self.guessed_number)
        for i, j in zip(suggested_number, guessed_number):
            if i == j:
                bulls += 1
            elif i in guessed_number:
                cows += 1
        self._update_score(bulls, cows)
        self._check_bulls(bulls)

    @property
    def move_number(self):
        return self._counter

    @property
    def game_result(self):
        return self._result


class InputChecker():
    def __init__(self):
        pass

    @staticmethod
    def check_number(number):
        result = False
        if number.isdecimal() is not True:
            result = False
        elif int(number) < 1000 or int(number) > 9999:
            result = False
        else:
            result = True
        return result


def play():
    print('*' * 64)
    print(' ' * ((64 - len('START OF THE GAME')) // 2) + 'START OF THE GAME')
    print('*' * 64)

    new_game = Game()
    checker = InputChecker()
    result = None

    new_game.info()

    while True:
        user_input = input('Введите четырехзначное число, все цифры которого различны: ')
        print(f'Вы ввели: {user_input}')
        while checker.check_number(user_input) is not True:
            print('Введенное число не соответствует формату, поробуйте еще раз!')
            user_input = input('Введите четырехзначное число, все цифры которого различны: ')
            print(f'Вы ввели: {user_input}')
        user_number = int(user_input)
        new_game.check_number(user_number)
        print(f'Ход {new_game.move_number}, счет: {new_game}')
        result = new_game.game_result
        if result:
            print('Поздравляю, Вы выиграли!')
            print(f'Количество ходов: {new_game.move_number}')
            print('Хотите еще партию? [y/n]: ')
            user_answer = str(input())
            if str.upper(user_answer) == 'Y':
                play()
            else:
                print('*' * 64)
                print(' ' * ((64 - len('END OF THE GAME')) // 2) + 'END OF THE GAME')
                print('*' * 64)


play()