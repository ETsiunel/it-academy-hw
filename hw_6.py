"""Homework 6"""


# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
A = "Robin Singh"
print(type(A))
print(A.split())
print(type(A.split()))

# "I love arrays they are my favorite"
#   => ["I", "love", "arrays", "they", "are", "my", "favorite"]
B = "I love arrays they are my favorite"
print(B.split())
print(type(B.split()))

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
#   Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
C = ["Ivan", "Ivanou"]
D = "Minsk"
E = "Belarus"
print("Привет, "+C[0]+" "+C[1]+"! Добро пожаловать в "+D+" "+E)
print(type("Привет, "+C[0]+" "+C[1]+"! Добро пожаловать в "+D+" "+E))

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
#   сделайте из него строку => "I love arrays they are my favorite"
F = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(F[0]+" "+F[1]+" "+F[2]+" "+F[3]+" "+F[4]+" "+F[5]+" "+F[6])
print(type(F[0]+" "+F[1]+" "+F[2]+" "+F[3]+" "+F[4]+" "+F[5]+" "+F[6]))

# Создайте список из 10 элементов,
#   вставьте на 3-ю позицию новое значение,
#   удалите элемент из списка под индексом 6
J = [0, 1, 2, 3, 4, 5, 6, 7, 8, "девять"]
print(type(J))
print(J)

J.insert(2, "new")
del J[6]
print(J)
