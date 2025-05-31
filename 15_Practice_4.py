# Задача 1
# Дан словарь учеников. Отсортировать учеников по возрасту.

students_dict_1 = {
    "Саша": 27,
    "Кирилл": 52, 
    "Маша": 14, 
    "Петя": 36, 
    "Оля": 43, 
}

sorted_students_dict_1 = sorted(students_dict_1.items(), key= lambda x: x[1])
print(sorted_students_dict_1)


# Задача 2
# Дан список с данными о росте и весе людей. Отсортировать их по индексу массы тела. Он вычисляется по формуле: 
# Вес тела в килограммах/(Рост в метрах∗Рост в метрах)

data_2 = [
    (82, 191),
    (68, 174),
    (90, 189), 
    (73, 179), 
    (76, 184)
]

sorted_data_2 = sorted(data_2, key= lambda x: x[0]/((x[1]/100)**2))
print(sorted_data_2)


# Задача 3
# Дан словарь учеников. Найти самого минимального ученика по возрасту.

students_list_3 = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

min_student_age_3 = min(students_list_3, key= lambda student: student["age"])
print(min_student_age_3)