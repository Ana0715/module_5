import json
import csv


# Задание 0. Работа с json
# Считайте данные из файла student_list.json и преобразуйте в словарь students.


with open('16_student_list.json') as json_file:
    students = json.load(json_file)


# Задание 1: Средний балл по всем предметам
# Напишите функцию get_average_score(), которая вычисляет средний балл по всем предметам для каждого студента в словаре students.


def make_grades_list(students_list):
    list_average = []
    for key, value in students_list.items():
        age = value["age"]
        grades_dict = (value["grades"])
        summa = 0
        for value in grades_dict.values():
            summa += value
        average = (summa/len(grades_dict))
        list_average.append((key, age, average))
    return (list_average)


def get_average_score(students_list):
    list_of_grades = make_grades_list(students_list)
    for (x, _, z) in list_of_grades:
        print(f"Средний балл для студента {x}: {z}")


# Задание 2: Наилучший и худший студент
# Напишите функции get_best_student() и get_worst_student(), которые находят студента с наилучшим и худшим средним баллом соответственно.


def get_best_student(students_list):
    list_of_grades = make_grades_list(students_list)
    max_grade = max(list_of_grades, key= lambda x: x[2])
    print(f"Наилучший студент: {max_grade[0]} (Средний балл: {max_grade[2]})")


def get_worst_student(students_list):
    list_of_grades = make_grades_list(students_list)
    max_grade = min(list_of_grades, key= lambda x: x[2])
    print(f"Худший студент: {max_grade[0]} (Средний балл: {max_grade[2]})")


# Задание 3: Поиск по имени
# Напишите функцию find_student(name), которая принимает имя студента в качестве аргумента и выводит информацию о нем, 
# если такой студент есть в словаре students. В противном случае, выведите сообщение "Студент с таким именем не найден".


def find_student(name, students_list):
    name = name.capitalize()
    if not name in students_list:
        print("Студент с таким именем не найден")
    for key, value in students_list.items():
        if key == name:
            print(
                f"Имя: {key}\n"
                f"Возраст: {value["age"]}\n"
                f"Предметы: {value["subjects"]}\n"
                f"Оценки: {value["grades"]}"
            )


# Задание 4: Сортировка студентов
# Отсортируйте студентов по их среднему баллу в порядке убывания. Выведите имена студентов и их средние баллы в следующем формате:


def students_sort(students_list):
    average_grades_list = make_grades_list(students_list)
    sort_list = sorted(average_grades_list, key= lambda x: x[2], reverse=True)
    print("Сортировка студентов по среднему баллу:")
    for (x, _, z) in sort_list:
        print(f"{x}: {z}")


# Задание 5. Преобразуйте словарь в список словарей данного формата
# students = [
#     {
#         'name': 'John',
#         'age': 20,
#         'subjects': ['Math', 'Physics', 'History', 'Chemistry', 'English'],
#         'grades': {'Math': 95, 'Physics': 88, 'History': 72, 'Chemistry': 84, 'English': 90}
#     }
# ]


def make_new_list_for_dict(students_list):
    list_for_dict = []
    for key, value in students_list.items():
        student_dict = {
            "name": key,
            "age": value["age"],
            "subjects": value["subjects"],
            "grades": value["grades"]
        }
        list_for_dict.append(student_dict)
    return list_for_dict


# Задание 6. Сформируйте csv


def make_new_dict_for_csv(students_list):
    list_with_info = make_grades_list(students_list)
    list_for_dict= []
    for i in list_with_info:
        new_dict = {
            "name": i[0],
            "age": i[1],
            "grade": i[2]
        }
        list_for_dict.append(new_dict)
    return list_for_dict


def make_csv(students_list, csv_file):
    list_for_csv = make_new_dict_for_csv(students_list)
    with open(csv_file, "w", encoding="utf-8") as f_csv:
        fieldnames = ["name", "age", "grade"]
        writer = csv.DictWriter(f_csv, fieldnames)
        writer.writeheader()
        writer.writerows(list_for_csv)




get_average_score(students)
get_best_student(students)
get_worst_student(students)
find_student("john", students)
students_sort(students)
make_new_list_for_dict(students)
make_csv(students, "16_students_list.csv")

