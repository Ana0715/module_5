import random
from collections import Counter, namedtuple, deque, defaultdict

# Задание 1: Анализ списка чисел с помощью Counter
# Сгенерируйте случайный список чисел.
# Используйте Counter, чтобы подсчитать количество уникальных элементов в списке.
# Найдите три наиболее часто встречающихся элемента в списке и выведите их с количеством вхождений.
def num_counter(num_list):
    counter_list = Counter(num_list)
    most_common_elements = counter_list.most_common(3)
    tuple_format_list = [f'Число: {i}, количество вхождений: {j}' for (i, j) in most_common_elements]
    return(
        f'Случайный список чисел: {num_list}\n'
        f'Количество уникальных элементов: {len(counter_list)}\n'
        f'Три наиболее часто встречающихся элемента: {tuple_format_list}'
    )


random_list = [random.randint(0, 15) for _ in range(20)]
print(num_counter(random_list))


# Задание 2: Работа с именованными кортежами
# Создайте именованный кортеж Book с полями title, author, genre.
# Создайте несколько экземпляров Book.
# Выведите информацию о книгах, используя атрибуты именованных кортежей.

Book = namedtuple('Book', ['title', 'author', 'genre'])
book_1 = Book('Война и мир', 'Лев Николаевич Толстой', 'исторический роман')
book_2 = Book('Преступление и наказание', 'Фёдор Михайлович Достоевский', 'психологический роман')
book_3 = Book('Гордость и предубеждение', 'Джейн Остин', 'роман о воспитании и любви')


print(book_1.title, book_1.author)
print(book_2.title, book_2.genre)
print(book_3.title)


# Задание 3: Работа с defaultdict
# Создайте defaultdict с типом данных list.
# Добавьте несколько элементов в словарь, используя ключи и значения.
# Выведите содержимое словаря, где значения - это списки элементов с одинаковыми ключами.

default_list = defaultdict(list)
def app_defaultdict(check_list, key, value):
    check_list[key].append(value)

app_defaultdict(default_list, 1, 'Война и мир')
app_defaultdict(default_list, 1, 'Лев Николаевич Толстой')
app_defaultdict(default_list, 1, 'исторический роман')

app_defaultdict(default_list, 2, 'Преступление и наказание')
app_defaultdict(default_list, 2, 'Фёдор Михайлович Достоевский')
app_defaultdict(default_list, 2, 'психологический роман')

app_defaultdict(default_list, 3, 'Гордость и предубеждение')
app_defaultdict(default_list, 3, 'Джейн Остин')
app_defaultdict(default_list, 3, 'роман о воспитании и любви')

print(default_list)


# Задание 4: Использование deque для обработки данных
# Создайте deque и добавьте в него элементы.
# Используйте методы append, appendleft, pop и popleft для добавления и удаления элементов из deque.
# Проверьте, как изменяется deque после каждой операции.

deque_list_1 = deque([random.randint(0, 10) for _ in range(5)])
print(deque_list_1)
deque_list_1.append(7)
print(deque_list_1)
deque_list_1.appendleft(0)
print(deque_list_1)
deque_list_1.pop()
print(deque_list_1)
deque_list_1.popleft()
print(deque_list_1)


# Задание 5: Реализация простой очереди с помощью deque
# Напишите функции для добавления и извлечения элементов из deque.
# Создайте пустой deque.
# Используйте написанные функции для добавления и извлечения элементов из очереди.

def app_right(deq_list, value):
    deq_list.append(value)

def app_left(deq_list, value):
    deq_list.appendleft(value)

def pop_right(deq_list):
    return deq_list.pop() if deq_list else None

def pop_left(deq_list):
    return deq_list.popleft()if deq_list else None

deque_list_2 = deque()

pop_right(deque_list_2)

app_right(deque_list_2, 9)
app_right(deque_list_2, 7)
app_right(deque_list_2, 4)
app_right(deque_list_2, 1)
print(deque_list_2)

app_left(deque_list_2, 3)
app_left(deque_list_2, 9)
app_left(deque_list_2, 6)
app_left(deque_list_2, 0)
app_left(deque_list_2, 2)
print(deque_list_2)

pop_right(deque_list_2)
print(deque_list_2)

pop_left(deque_list_2)
print(deque_list_2)
