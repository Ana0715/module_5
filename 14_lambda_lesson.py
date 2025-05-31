# 1. Дан список строк ["apple", "kiwi", "banana", "fig"]. 
# Оставьте в нем только строки, длина которых больше 4 символов, используя filter() и лямбда-функцию.

fruits_1 = ["apple", "kiwi", "banana", "fig"]
sort_fruits_1 = list(filter(lambda x: len(x) > 4, fruits_1))
print(sort_fruits_1)


# 2. Дан список словарей students = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]. 
# Найдите студента с максимальной оценкой, используя max() и лямбда-функцию для задания ключа сортировки.

students_2 = [
    {"name": "John", "grade": 90}, 
    {"name": "Jane", "grade": 85}, 
    {"name": "Dave", "grade": 92}
    ]
max_grade_student_2 = max(students_2, key= lambda x: x["grade"])
print(max_grade_student_2)


# 3.  Дан список кортежей [(1, 5), (3, 2), (2, 8), (4, 3)]. 
# Отсортируйте его по сумме элементов каждого кортежа с использованием sorted() и лямбда-функции.

numbers_3 = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_numbers_3 = sorted(numbers_3, key=lambda x: sum(x))
print(sorted_numbers_3)


# 4. Дан список чисел [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
# Оставьте в нем только четные числа с использованием filter() и лямбда-функции.

numbers_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_4 = list(filter(lambda x: x % 2 == 0, numbers_4))
print(even_numbers_4)


# 5. Сортировка объектов пользовательского класса:
# Создайте класс Person с атрибутами name и age. Дан список объектов этого класса. 
# Отсортируйте список объектов по возрасту с использованием sorted() и лямбда-функции.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name: {self.name}, age: {self.age})"
    
persons_5 = [
    Person("John", 25),
    Person("Jane", 30),
    Person("Dave", 19)
]
sorted_persons_5 = sorted(persons_5, key=lambda x: x.age)
print(sorted_persons_5)