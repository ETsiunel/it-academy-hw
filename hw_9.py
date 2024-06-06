"""Homework_9"""

# # # Строки с заданным символом # # #
# Напишите программу, которая бы работала следующим образом -
# находила символ "#" и если этот символ найден -
# удаляла предыдущий символ из строки.
# Ваша задача обработать строки с "#" символом.


def string_modifier(string: str) -> str:
    """Функция замены символа перед #"""
    if "".join(string.split("#")) == "":
        return ""
    parts = string.split("#")
    result = ""
    for part in parts:
        if len(result) == 0:
            result += part
        else:
            result = result[:-1] + part
    return result


assert string_modifier('a#bc#d') == 'bd'
assert string_modifier('abc#d##c') == 'ac'
assert string_modifier('abc##d######') == ''
assert string_modifier('#######') == ''
assert string_modifier('') == ''
assert string_modifier('abcde') == 'abcde'


# # # Свечи # # #
# Когда свеча догорает, остается остаток.
# Остатки можно объединить, чтобы создать новую свечу,
# которая при догорании,
# в свою очередь, оставит еще один остаток.
# У вас есть количество свечей.
# Какое общее количество свечей вы можете сжечь, если предположить,
# что вы создадите новые свечи, как только у вас останется достаточно остатков?
# Пример
# Если у Вас 5(candles_number) свечей,
# и из 2х(make_new) остатков вы можете сделать 1 новую свечу, то ответе будет: 9.
# По шагам, чтобы сжечь 9 свечей:
# сожгите 5 свечей, получите 5 остатков;
# создайте еще 2 свечи, используя 4 остатка (остался 1);
# сожгите 2 свечи, в итоге останется 3 остатка;
# создайте еще одну свечу, используя 2 остатка (остался 1);
# сожгите созданную свечу, что даст еще один остаток (всего 2 остатка);
# создать свечу из оставшихся остатков;
# зажгите последнюю свечу.
# Таким образом, можно сжечь 5+2+1+1=9 свечей, что и является ответом.
new_candles_init = 0
make_new = 0


def burned_candles_counter(new_candles, make_new_candle):
    """Функция подсчета сгоревших свечей"""
    rest_after_new_candles_creation = 0
    burned = 0
    while new_candles != 0:
        burned_candles = new_candles
        rest_after_burning = burned_candles
        common_rest = rest_after_burning + + rest_after_new_candles_creation
        new_candles = common_rest // make_new_candle
        rest_after_new_candles_creation = common_rest - new_candles * make_new_candle
        burned += burned_candles
    return burned


assert burned_candles_counter(5, 2) == 9
assert burned_candles_counter(1, 2) == 1
assert burned_candles_counter(15, 5) == 18
assert burned_candles_counter(12, 2) == 23
assert burned_candles_counter(6, 4) == 7
assert burned_candles_counter(13, 5) == 16
assert burned_candles_counter(2, 3) == 2


# # # Подсчет количества букв # # #
# На вход подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
def counter(a):
    """Функция подсчета символов в строке """
    value = ''
    count = ''
    result = ''
    for i in a:
        if i != value:
            count = '' if count == 1 else str(count)
            result += value + str(count)
            count = 1
            value = i
        else:
            count += 1
    count = '' if count == 1 else str(count)
    result += value + str(count)
    return result


assert counter('cccbba') == 'c3b2a'
assert counter("abeehhhhhccced") == "abe2h5c3ed"
assert counter("aaabbceedd") == "a3b2ce2d2"
assert counter("abcde") == "abcde"
assert counter("aaabbdefffff") == "a3b2def5"
