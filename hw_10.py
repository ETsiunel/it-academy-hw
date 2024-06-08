"""Homework_10"""

# # # Положительные аргументы функции # # #
# Напишите декоратор @validate_arguments, который проверяет,
# что все аргументы функции являются положительными числами.
# Если встречается аргумент, не соответствующий этому условию,
# функция должна вывести сообщение об ошибке.
# Вот некоторые подсказки:
# Внутри декоратора, используйте цикл for для перебора аргументов функции.
# Используйте оператор if для проверки,
# является ли аргумент положительным числом.
# Если аргумент не соответствует условию,
# используйте оператор raise для вызова исключения ValueError.


def validate_arguments(function_to_decorate):
    """Декоратор проверки аргументов функции"""
    def validator_wrapper(*args):
        function_to_decorate(*args)
        for i in args:
            if i <= 0:
                raise ValueError("Argument can not be zero or negative."
                                 f" Invalid argument: {i}")
    return validator_wrapper


@validate_arguments
def validator(*args):
    print(*args)


validator(1, 2, 100)


# # # Вернуть число # # #
# Создайте декоратор, который проверяет, является ли результат функции числом
# и выводит сообщение об ошибке, если это не так.
# Вот некоторые подсказки:
# Внутри декоратора, после вызова функции,
# проверьте тип результата с помощью функции isinstance().
# Если тип не является числом,
# выведите сообщение об ошибке с помощью функции print().


def number_check(function_to_decorate):
    """Декоратор проверки результата функции"""
    def number_check_wrapper(res):
        function_to_decorate(res)
        if not isinstance(res, float):
            print("Result is not a number")
    return number_check_wrapper


@number_check
def check(res):
    print(res)


check('weqjkhfg')


# # # Декоратор типов # # #
# Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал


def typed(_type):
    """Декоратор проверки типа параметров функции"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            converted_args = []
            converted_kwargs = {}
            for arg in args:
                try:
                    converted_args.append(_type(arg))
                except ValueError:
                    converted_args.append(arg)
            for k, v in kwargs.items():
                try:
                    converted_kwargs[k] = _type(v)
                except ValueError:
                    converted_kwargs[k] = v
            return func(*converted_args, **converted_kwargs)
        return wrapper
    return decorator


@typed(_type=str)
def add_str(a, b):
    return a + b


@typed(_type=int)
def add_int(a, b, c):
    return a + b + c


@typed(_type=float)
def add_float(a, b, c):
    return a + b + c


# Тестирование функций
assert add_str("3", 5) == "35"
assert add_str(5, 5) == "55"
assert add_str('a', 'b') == "ab"
assert add_int(5, 6, 7) == 18
assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001
