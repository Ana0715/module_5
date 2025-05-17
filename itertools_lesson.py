import itertools

# Задача 1: Комбинации чисел из списка
# Дан список чисел [1, 2, 3, 4]. Используя модуль itertools, создайте все возможные комбинации чисел длиной 2 и выведите их.

numbers_1 = [1, 2, 3, 4]
iter_numbers_1 = [i for i in itertools.combinations(numbers_1, 2)]
print(iter_numbers_1)


# Задача 2: Перебор перестановок букв в слове
# Для слова 'Python' найдите все возможные перестановки букв. Выведите каждую перестановку на отдельной строке.

stroka_2 = 'Python'
iter_stroka_2 = [''.join(i) for i in itertools.permutations(stroka_2)]
print(iter_stroka_2)


# Задача 3: Объединение списков в цикле
# Даны три списка: ['a', 'b'], [1, 2, 3], ['x', 'y']. 
# Используя itertools.cycle, объедините их в один список в цикле, повторяя этот цикл 5 раз.

list_3_1 = ['a', 'b']
list_3_2 = [1, 2, 3]
list_3_3 = ['x', 'y']
result_list = []

cycle_list_1 = itertools.cycle(list_3_1)
cycle_list_2 = itertools.cycle(list_3_2)
cycle_list_3 = itertools.cycle(list_3_3)

for _ in range(5):
    result_list.append(next(cycle_list_1))
    result_list.append(next(cycle_list_2))
    result_list.append(next(cycle_list_3))

print(result_list)


# Задача 4: Генерация бесконечной последовательности чисел
# Создайте бесконечный генератор, который будет возвращать последовательность чисел Фибоначчи. Выведите первые 10 чисел Фибоначчи.

def fib(a=0, b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b

nums_4 = list(itertools.islice(fib(), 10))
print(nums_4)


# Задача 5: Составление всех возможных комбинаций слов
# Используя itertools.product, создайте все возможные комбинации слов из двух списков: ['red', 'blue'] и ['shirt', 'shoes']. 
# Выведите каждую комбинацию на отдельной строке.

list_5_1 = ['red', 'blue']
list_5_2 = ['shirt', 'shoes']

def product_func(*args):
    for i in itertools.product(*args):
        print(i)

product_func(list_5_1, list_5_2)