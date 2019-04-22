__author__ = 'Зелепукин Алексей Юрьевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    m = 10 ** ndigits
    number = number * m
    fractional = number % 1
    number //= 1
    if fractional < 0.5:
        round_number = number / m
    else:
        round_number = (number + 1) / m
    return round_number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    s1, s2 = 0, 0
    if 100000 <= ticket_number <= 999999:
        for i in range(6):
            if i < 3:
                s1 += ticket_number % 10
                ticket_number //= 10
            else:
                s2 += ticket_number % 10
                ticket_number //= 10
        if s1 == s2:
            return 'Lucky ticket'
        else:
            return 'Unlucky ticket'
    else:
        return 'Unlucky ticket'


# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
