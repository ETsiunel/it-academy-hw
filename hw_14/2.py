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
# 1 / 2 + 2 * 2
# 2 / 2 ** 3 - 1

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

    def to_rpn(parts):
        """Функция преобразования выражения в обратную польскую запись (RPN)"""
        # # каюсь честно подсмотрела в интернетах это решение
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

        output = []
        stack = []

        for part in parts:
            if part.isdigit() or (part[0] == '-' and part[1:].isdigit()):
                output.append(float(part))
            elif part in operations:
                while (stack and stack[-1] in operations and
                       precedence[part] <= precedence[stack[-1]]):
                    output.append(stack.pop())
                stack.append(part)
            elif part == '(':
                stack.append(part)
            elif part == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
        while stack:
            output.append(stack.pop())

        return output

    def evaluate_rpn(rpn_parts):
        stack = []

        for part in rpn_parts:
            if isinstance(part, float):
                stack.append(part)
            elif part in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[part](a, b))

        return stack[0]

    rpn_parts = to_rpn(parts)
    result = evaluate_rpn(rpn_parts)
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
