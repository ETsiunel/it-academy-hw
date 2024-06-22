"""Homework_14"""
# # # Files # # #
# Напишите программу, которая создает текстовый файл(если его нет) "students.txt".
# Запишите в файл список студентов, номер группы, их оценки.
# Каждый студент на новой строке.
# Откройте файл и прочитайте всю информацию из него.
# Напечатайте общее количество студентов, количество студентов для каждой группы
# и среднюю оценку для каждой группы.
# Допишите эту информацию в конец файла.
# Предусмотрите возможные ошибки и обработайте их.

import os
file_name = "students.txt"


def create_file(file_name):
    """Функция создания файла"""
    students_list = [
        "Kate Tsiunel, 245, 98",
        "Anna Rabtsava, 245, 90",
        "Alex Tsurkan, 315, 66",
        "Denis Lomeyko, 315, 86",
        "Dmitriy Skvortsov, 245, 45"
    ]

    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            for student in students_list:
                file.write(student + "\n")
    except IOError as e:
        print(f"Error writing to file: {e}")


if not os.path.exists(file_name):
    create_file(file_name)


def read_file(filename):
    """Функция чтения файла"""
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            students = file.readlines()
        list_students = []
        for student in students:
            parts = [part.strip() for part in student.strip().split(',')]
            if len(parts) == 3:
                list_students.append(parts)
        return list_students
    except IOError as e:
        print(f"Error reading file: {e}")
        return []


def students_info(students):
    """Функция подсчета студентов в группе и среднего балла"""
    total_students = len(students)
    group_info = {}

    for student in students:
        group = student[1]
        grade = int(student[2])

        if group not in group_info:
            group_info[group] = {'count': 0, 'total_grade': 0}

        group_info[group]['count'] += 1
        group_info[group]['total_grade'] += grade

    return total_students, group_info


def append_file(file_name, total_students, group_info):
    """Функция дозаписи в файл"""
    try:
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f"\nTotal students: {total_students}\n")
            for group, info in group_info.items():
                avg_grade = info['total_grade'] / info['count']
                file.write(f"Group {group}: {info['count']} students, "
                           f"average grade {avg_grade:.2f}\n")
    except IOError as e:
        print(f"Error appending file: {e}")


students = read_file(file_name)
total_students, group_info = students_info(students)
append_file(file_name, total_students, group_info)
