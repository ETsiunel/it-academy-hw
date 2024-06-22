"""Homework_14"""
# # # Инженерный калькулятор # # #
# Напишите программу - инженерный калькулятор.
# Предусмотрите возможные ошибки и обработайте их.
# ~ - это предложение ввода.
# Базовые требования:
# Программа считает простые математические выражения:
# ~ 5 + 49
# Программа ожидает от пользователя ввода математического выражения
# и правильно его трактует:
# ~ 10 - 3 + 18
# ~ 2 ** 3 - 17

import re
import operator


def expression(exp):
    """Функция разбора выражения на числа и операторы"""

    parts = re.findall(r'[+-]?\d+(?:\.\d+)?|\*\*|[+\-*/()]', exp)

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow
    }

    result = float(parts[0])

    i = 1
    while i < len(parts) - 1:
        operand = float(parts[i + 1])
        result = operations[parts[i]](result, operand)
        i += 2
    return result


def calculator():
    """Функция вызова калькулятора"""
    print("Введите математическое выражение")

    while True:
        try:
            user_input = input("~ ")
            result = expression(user_input)
            print("Результат:", result)
        except Exception as e:
            print("Ошибка:", e)


calculator()
