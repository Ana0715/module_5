from functools import reduce

# 1. Используйте map(), чтобы преобразовать список чисел в список их кубов, используя обычную функцию.

def cube(x):
    return x ** 3

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubes_numbers = list(map(cube, numbers1))
print(cubes_numbers)


# 2. Используйте filter(), чтобы отобрать из списка чисел только те, которые делятся на 5, используя обычную функцию.

def filter_five(x):
    return x % 5 == 0

numbers2 = [2, 5, 9, 15, 19, 23, 45, 49, 65]
filter_numbers = list(filter(filter_five, numbers2))
print(filter_numbers)


# 3. Используйте  filter() и  reduce(), чтобы найти произведение всех нечетных чисел в списке, используя обычную функцию.

def is_odd(x):
    return x % 2 != 0

def multiply(x, y):
    return x * y

numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(is_odd, numbers3))
product = reduce(multiply, odd_numbers)
print(product)