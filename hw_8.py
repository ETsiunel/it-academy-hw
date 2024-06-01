"""Homework_8"""

# # # Последовательность # # #
# Дана последовательность целых чисел в виде массива.
# Определите, можно ли получить строго возрастающую последовательность,
# удалив из массива не более одного элемента.
# Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
# если a0 < a1 < ... < an.
# Последовательность, содержащая только один элемент, также считается строго возрастающей.
# Примеры
# Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.
# В этом массиве нет ни одного элемента, который можно было бы удалить,
# чтобы получить строго возрастающую последовательность.
# Для последовательности = [1, 3, 2] вывод должен быть = True.
# Вы можете удалить 3 из массива,
# чтобы получить строго возрастающую последовательность [1, 2].
# Альтернативно можно убрать 2,
# чтобы получить строго возрастающую последовательность [1, 3].
#
# solution([1, 2, 3])
# solution([1, 2, 1, 2])
# solution([1, 3, 2, 1])
# solution([1, 2, 3, 4, 5, 3, 5, 6])
# solution([40, 50, 60, 10, 20, 30])


def sequence_check(sequence):
    """Проверка последовательности на возрастание"""
    list_sequence = list(set(sequence))
    if len(sequence) - len(list_sequence) >= 2:
        return False

    list_sequence.sort()

    if len(sequence) - len(list_sequence) == 0:
        delete_count = 0
    else:
        delete_count = 1

    # Проверяем, можно ли получить строго возрастающую последовательность
    for i in range(len(list_sequence)):
        if sequence[i] != list_sequence[i]:
            if sequence[i] < list_sequence[i]:
                delete_count += 1
                if delete_count > 1:
                    return False
            else:
                if i == 0 or sequence[i] <= list_sequence[i - 1]:
                    return False
    return True


sequence = [1, 3, 2, 1]
print(sequence_check(sequence))


# # # Число напротив # # #
# Рассмотрим целые числа от 0 до n-1, записанные по окружности так,
# чтобы расстояние между любыми двумя соседними числами было одинаковым
# (обратите внимание, что 0 и n-1 тоже являются соседними).
# Учитывая n и first_number, найдите число,
# которое написано в радиально противоположной позиции от first_number.
# Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7.

def opposite_number(n, first_number):
    """Поиск числа напротив"""
    if (n/2 + first_number) >= n:
        a = int(n/2 + first_number - n)
    else:
        a = int(n/2 + first_number)
    return a


n = int(input("Enter n: "))
while n % 2 == 1:
    print("n must be even number")
    n = int(input("Enter n: "))
print("Your circle:", list(range(0, n)))

first_number = int(input("Enter first_number: "))
while first_number > n-1:
    print("First number can not be >= n")
    first_number = int(input("Enter first_number: "))
print("Opposite number is", opposite_number(n, first_number))


# # # Validate # # #
# Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным). И проверяющей может ли такая карта существовать.
# Предусмотреть защиту от ввода букв, пустой строки и т.д.
# Примечания Алгоритм Луна
# Примеры
# validate(4561261212345464) #=> False
# validate(4561261212345467) #=> True
#
# Для проверки: https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm

card = input("Enter a card number: ")
summ = 0


def card_checker(card):
    """Проверка карты на пустой ввод, буквы"""
    if len(card) == 0 or card.isalpha() or not card.isdigit():
        print("Incorrect card number")
        return False
    return True


def luna(summ):
    """Проверка карты по алгоритму Луна"""
    card_list = list(map(int, card[::-1]))
    for index, number in enumerate(card_list):
        if index % 2 == 1:
            a = number * 2
            if a > 9:
                a -= 9
            summ += a
        else:
            summ += number
    return summ


while not card_checker(card):
    card = input("Enter a card number: ")
print('Card is valid' if luna(summ) % 10 == 0 else 'Card does not exist')
