import itertools


card_suits = ['Червы', 'Бубны', 'Трефы', 'Пики']


def check_cards():
    number_cards = input('Введите число карт каждой масти в колоде (от 1 до 13): ')
    try:
        number_cards = int(number_cards)
        if 1 <= number_cards <= 13:
            return number_cards
        return None
    except:
        return None


def check_combination(all_cards_num):
    combination_num = input('По сколько карт должны быть комбинации? ')
    try:
        combination_num = int(combination_num)
        if 0 < combination_num <= all_cards_num:
            return combination_num
        else:
            return None
    except:
        return None


def cards_generation():
    num_cards = check_cards()
    if not num_cards:
        return None

    num_list = []
    deck_card_list = []

    for i in itertools.count(1):
        if i > num_cards:
            break
        num_list.append(i)

    for i in itertools.product(num_list, card_suits):
        deck_card_list.append(i)
    return deck_card_list


def write_combination(filename, item):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(str(item))
        f.write('\n')


def clear_file(filename):
    with open(filename, 'w'):
        pass


def combination_card(filename):
    items = cards_generation()
    if not items:
        return 'Неверное значение!'

    combination_len = check_combination(len(items))
    if not combination_len:
        return 'Неверное значение!'

    if filename:
        clear_file(filename)
    for i in itertools.combinations(items, combination_len):
        write_combination(filename, i)
    return 'Выполнено!'


print(combination_card('11_hello.txt'))