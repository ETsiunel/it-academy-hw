"""Homework_12"""
# # # Конвертер валют # # #
# Расширьте функционал класса Bank из домашней работы #11.
# Добавьте новый класс Currency,
# который умеет конвертировать различные валюты(USD, EUR, ...)
# в заданную валюту.
# bank = Bank(..)
# vasya = Person('USD', 10)
# petya = Person('EUR', 5)
# # Если валюта не задана, то конвертация происходит в BYN:
# assert bank.exchange_currency(vasya.currency, vasya.amount)
#   == (32.69, "BYN"), <error message>
# assert bank.exchange_currency(petya.currency, petya.amount)
#   == (35.20, "BYN"), <error message>
# # Конвертация в заданную валюту BYN:
# assert bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')
#   == (9.29, "EUR"), <error message>
# assert bank.exchange_currency(petya.currency, petya.amount, 'USD')
#   == (10.76, "USD"), <error message>


class Person:
    """Определение пользователя"""
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


class Bank:
    """Определение класса Bank"""
    def __init__(self):
        self.deposits = []

    def exchange_currency(self, from_currency, amount, to_currency='BYN'):
        return Currency.convert(from_currency, amount, to_currency)


class Currency:
    """Определение класса Currency"""
    exchange_rates = {
        ('USD', 'BYN'): 3.269,
        ('EUR', 'BYN'): 7.04,
        ('USD', 'EUR'): 0.87,
        ('EUR', 'USD'): 1 / 0.87
    }

    @classmethod
    def convert(cls, from_currency, amount, to_currency='BYN'):
        """Конвертер валюты"""
        if from_currency == to_currency:
            return round(amount, 2), to_currency
        if (from_currency, to_currency) in cls.exchange_rates:
            rate = cls.exchange_rates[(from_currency, to_currency)]
            return round(amount * rate, 2), to_currency
        if (to_currency, from_currency) in cls.exchange_rates:
            rate = cls.exchange_rates[(to_currency, from_currency)]
            return round(amount / rate, 2), to_currency
        raise ValueError(f"Конвертация из {from_currency} "
                         f"в {to_currency} невозможна")


bank = Bank()
vasya = Person('USD', 10)
petya = Person('EUR', 5)

assert (bank.exchange_currency(vasya.currency, vasya.amount)
        == (32.69, "BYN")), "Ошибка конвертации USD в BYN"
assert (bank.exchange_currency(petya.currency, petya.amount)
        == (35.20, "BYN")), "Ошибка конвертации EUR в BYN"
assert (bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')
        == (8.7, "EUR")), "Ошибка конвертации USD в EUR"
assert (bank.exchange_currency(petya.currency, petya.amount, 'USD')
        == (5.75, "USD")), "Ошибка конвертации EUR в USD"
