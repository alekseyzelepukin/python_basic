# !/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

import numpy as np
import random


class Bag:
    def __init__(self, number=90):
        self._counter = number
        self._barrels = self._generate_bag()

    def _generate_bag(self):
        barrels = [x for x in range(1, self._counter + 1)]
        random.shuffle(barrels)
        return barrels

    def get_barrel(self):
        self._counter -= 1
        for barrel in self._barrels:
            print(f'Новый бочонок: {barrel} (осталось {self._counter})')
            yield barrel

    @property
    def barrels_left(self):
        return self._counter


class Card():
    def __init__(self, player_card=True):
        self._player_card = player_card
        self._card = self._generate_card()
        self._digits_left = 15

    @staticmethod
    def _generate_card():
        card = np.array(sorted(random.sample(range(1, 91), 15))).reshape(3, -1).tolist()
        for row in card:
            for _ in range(4):
                row.insert(random.randint(0, 4), ' ')
        return card

    def update_card(self, barrel):
        for i, row in enumerate(self._card):
            for j, item in enumerate(row):
                if item == barrel:
                    self._card[i][j] = '-'
                    self._digits_left -= 1

    def check_card(self, barrel):
        result = False
        for row in self._card:
            for item in row:
                if item == barrel:
                    result = True
        return result

    @property
    def digits_left(self):
        return self._digits_left

    def show_card(self):
        if self._player_card:
            print('------ Ваша карточка -----')
        else:
            print('-- Карточка компьютера ---')
        prototype = ' '.join(['{:>2}' for i in range(9)])
        card = [prototype.format(*row) for row in self._card]
        for row in card:
            for item in row:
                print(item, end='')
            print()
        print('--------------------------')


def game():
    print('*' * 32, 'START GAME', '*' * 32)

    bag = Bag()
    player_card, computer_card = Card(player_card=True), Card(player_card=False)
    user_input = None

    while True:

        if user_input == 'q':
            break

        if bag.barrels_left == 0:
            break

        barrel = next(bag.get_barrel())

        player_card.show_card()
        computer_card.show_card()

        user_input = input('Зачеркнуть цифру? (y/n) / Выйти из игры? (q):')

        print('\n')

        if computer_card.check_card(barrel):
            computer_card.update_card(barrel)

        if user_input == 'y':
            if player_card.check_card(barrel):
                player_card.update_card(barrel)
            else:
                print('Такой цифры на карточке нет. Вы проиграли!')
                break
                pass
        elif user_input == 'n':
            if player_card.check_card(barrel):
                print('Такая цифра есть на карточке. Вы проиграли!')
                break
                pass
        else:
            while user_input not in ['y', 'n', 'q']:
                user_input = input('Зачеркнуть цифру? (y/n) / Выйти из игры? (q)')

        player_digits_left = player_card.digits_left
        computer_digits_left = computer_card.digits_left

        if player_digits_left == 0 and computer_digits_left == 0:
            print('Ничья!')
        elif player_digits_left == 0:
            print('Вы выиграли!')
        elif computer_digits_left == 0:
            print('Компьютер выиграл!!')
        else:
            continue

    print('*' * 33, 'END GAME', '*' * 33)


game()
