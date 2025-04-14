import csv

with open('spisok.txt', 'r', encoding='utf-8') as txt_file:
    shopping_list = [str_txt.replace('\n', '').split('\t') for str_txt in txt_file.readlines()]


def dict_maker(spisok, list_for_dict:list):
    for i in spisok:
        new_dict = {'наименование':i[0], 'количество товара':i[1], 'цена за 1шт.':i[2]}
        list_for_dict.append(new_dict)
    

shop_dict = []
dict_maker(shopping_list, shop_dict)


with open('новые_данные.csv', 'w', encoding='utf-8') as csv_file:
    fieldnames = ['наименование', 'количество товара', 'цена за 1шт.']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    writer.writerows(shop_dict)
        
with open('новые_данные.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    summa = 0
    for row in reader:
        summa += int(row['количество товара']) * int(row['цена за 1шт.'])
    print(f'Общая стоимость заказа: {summa} руб.')