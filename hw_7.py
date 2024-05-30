"""Homework_7"""
import random

# # # Быки и коровы # # #
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное
# 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами,
# сообщаемое противнику. Противник сообщает в ответ,
# сколько цифр угадано без совпадения с их позициями в тайном числе
# (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе
# (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой,
# пока не отгадает всю последовательность.
# Ваша задача реализовать программу,
# против которой можно сыграть в "Быки и коровы"
# Пример
# Загадано
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!
# pylint: disable=invalid-name
# pylint: disable=line-too-long


def computer_number_check(computer_number):
    """Проверка сгенерированного компьютером числа на уникальность цифр"""
    computer_number_list = list(str(computer_number))
    if len(set(computer_number_list)) == 4:
        return True
    return False


# Генерация случайного 4-х значного числа
comp_numb_gen = 0  # число загаданное компьютером
while not computer_number_check(comp_numb_gen):
    comp_numb_gen = random.randint(1000, 9999)
# print(f"Computer number: {comp_numb_gen}")
# just debug print
print("Computer generated a number for you. Try to guess!")


def player_number_check():
    """Проверка ответа пользователя на уникальность цифр"""
    player_number = int(input("Enter your number "
                              "(should contain only uniq digits): "))
    player_number_list = list(str(player_number))
    if len(set(player_number_list)) == 4:
        return player_number
    return player_number_check()


def bulls_cows_counter(computer_number, player_number, bulls=0, cows=0):
    """Подсчет быков и коров"""
    computer_number_list = list(str(computer_number))
    player_number_list = list(str(player_number))
    for n in range(len(player_number_list)):
        if player_number_list[n] == computer_number_list[n]:
            bulls += 1
        elif player_number_list[n] in computer_number_list:
            cows += 1
    return bulls, cows


# 1-й вызов функции проверки ввденного игроком числа
pl_num_attempt = player_number_check()
# 1-й вызов функции подсчета быков и коров
bulls_guess, cows_guess = bulls_cows_counter(comp_numb_gen, pl_num_attempt)
print("You guessed", bulls_guess, "bull(s) and", cows_guess, "cow(s).")

# Цикл повтора вышеуказанных функций пока количество быков не станет == 4
while bulls_cows_counter(comp_numb_gen, pl_num_attempt) != (4, 0):
    print("    Try one more time!")
    pl_num_attempt = player_number_check()
    bulls_guess, cows_guess = bulls_cows_counter(comp_numb_gen, pl_num_attempt)
    print("You guessed", bulls_guess, "bull(s) and", cows_guess, "cow(s).")
print("Congratulation!", pl_num_attempt, "is the correct answer :)")


# # # Пирамида # # #
# Мы можем визуализировать художественную пирамиду ASCII с N уровнями,
# напечатав N рядов звездочек,
# где верхний ряд имеет одну звездочку в центре,
# а каждый последующий ряд имеет две дополнительные звездочки с каждой стороны.
# Вот как это выглядит, когда N равно 3.
#   *
#  ***
# *****
# Вот как это выглядит, когда N равно 5.
#     *
#    ***
#   *****
#  *******
# *********
# Необходимо написать программу,
# которая генерирует такую пирамиду со значением N, равным 10

pyramid = int(input("Enter pyramid level: "))
# for level in range(pyramid):
for level in range(pyramid):
    print(' ' * (pyramid-level-1) + '*' * (level*2+1))


# # # Статуи # # #
# Вы получили в подарок на день рождения статуи разных размеров,
# каждая статуя имеет неотрицательный целочисленный размер.
# Поскольку Вам нравится доводить вещи до совершенства,
# то необходимо расположить их от меньшего к большему,
# чтобы каждая статуя была больше предыдущей ровно на 1.
# Для этого Вам могут понадобиться дополнительные статуи.
# Определите количество отсутствующих статуй.
# Пример
# Для статуй = [6, 2, 3, 8] результат должен быть = 3.
# Иными словами, у Вас отсутствуют статуи размеров 4, 5 и 7.

gift = [6, 2, 3, 8]
new_gift = list(range(min(gift), max(gift)+1))
# print(new_gift)
missed_elements_count = 0
missed_elements = []
for i in new_gift:
    if i not in gift:
        missed_elements_count += 1
        missed_elements.append(i)
print(missed_elements_count, 'missing statues with numbers', missed_elements)
