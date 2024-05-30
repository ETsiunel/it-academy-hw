# # # # Быки и коровы # # # #
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе
#   (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
#   При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
#   Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"
# Пример
# Загадано
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!

import random


# Проверка сгенерированного компьютером числа на уникальность цифр
def computer_number_check(computer_number):
    computer_number_list = list(str(computer_number))
    if len(set(computer_number_list)) == 4:
        return True
    return False


# Генерация случайного 4-х значного числа
computer_number = []  # число загаданное компьютером
while not computer_number_check(computer_number):
    computer_number = random.randint(1000, 9999)
# print(f"Computer number: {computer_number}")  # secret information, just debug print
print("Computer generated a number for you. Try to guess!")


# Проверка ответа пользователя на уникальность цифр
def player_number_check():
    player_number = int(input("Enter your number (should contain only uniq digits): "))  # число ответ игрока
    player_number_list = list(str(player_number))
    if len(set(player_number_list)) == 4:
        return player_number
    else:
        return player_number_check()


# Подсчет быков и коров
def bulls_cows_counter(computer_number, player_number, bulls=0, cows=0):
    computer_number_list = list(str(computer_number))
    player_number_list = list(str(player_number))
    for n in range(len(player_number_list)):
        if player_number_list[n] == computer_number_list[n]:
            bulls += 1
        elif player_number_list[n] in computer_number_list:
            cows += 1
    return bulls, cows


# 1-й вызов функции проверки ввденного игроком числа
player_number = player_number_check()
# 1-й вызов функции подсчета быков и коров
bulls, cows = bulls_cows_counter(computer_number, player_number)
print("Yuu guessed", bulls, "bulls and", cows, "cows")

# Цикл повтора вышеуказанных функций пока количество быков не станет == 4
while bulls_cows_counter(computer_number, player_number) != (4, 0):
    print("    Try one more time!")
    player_number = player_number_check()
    bulls, cows = bulls_cows_counter(computer_number, player_number)
    print("Yuu guessed", bulls, "bulls and", cows, "cows.")
print("Congratulation!", player_number, "is correct answer")


# # # # Пирамида # # # #
# Мы можем визуализировать художественную пирамиду ASCII с N уровнями, напечатав N рядов звездочек,
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
# Необходимо написать программу, которая генерирует такую пирамиду со значением N, равным 10

pyramid = int(input("Enter pyramid level: "))
for level in range(pyramid):
    print(' ' * (pyramid-level-1) + '*' * (level*2+1))


# # # # Статуи # # # #
# Вы получили в подарок на день рождения статуи разных размеров,
# каждая статуя имеет неотрицательный целочисленный размер.
# Поскольку Вам нравится доводить вещи до совершенства, то необходимо расположить их от меньшего к большему,
# чтобы каждая статуя была больше предыдущей ровно на 1.
# Для этого Вам могут понадобиться дополнительные статуи. Определите количество отсутствующих статуй.
# Пример
# Для статуй = [6, 2, 3, 8] результат должен быть = 3. Иными словами, у Вас отсутствуют статуи размеров 4, 5 и 7.

gift = [6, 2, 3, 8]
new_gift = list(range(min(gift), max(gift)+1))
# print(new_gift)
missing_statues = 0
missed_elements = []
for i in new_gift:
    if i not in gift:
        missing_statues += 1
        missed_elements.append(i)
print(missing_statues, 'missing statues with numbers', missed_elements)
