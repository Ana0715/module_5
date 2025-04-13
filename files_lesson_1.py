BAD_SYMBOLS = '.,|/*:;!@#$%^&()-_=+}{[]"<>?`'

def get_words(filename):
	data1 = [line.strip().lower().split() for line in filename.readlines()]
	data2, data3 = [], []
	for i in data1:
		data2.extend(i)
	for word in data2:
		check_list(word, data3)
	return data3


def check_list(stroka, new_list:list=None):
	if stroka and stroka[-1] in BAD_SYMBOLS:
		check_list(stroka[:-1], new_list)
	else:
		new_list.append(stroka)


def get_words_dict(filename):
	list_for_words = get_words(filename)
	dictionary = {}
	for word in list_for_words:
		dictionary[word] = dictionary.get(word, 0) + 1
	return dictionary


def print_one_by_one(dictionary:dict):
	for key, value in dictionary.items():
		print (key, value)


def all_process(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		final_dict = get_words_dict(f)
		print(
		f'Название файла: {f.name}\n'
		f'Количество слов: {sum(final_dict.values())}\n'
		f'Количество уникальных слов: {len(final_dict.keys())}\n'
		f'Процент уникальных слов: {round((len(final_dict.keys())/sum(final_dict.values()))*100)}%\n'
		'Все использованные слова:')
	print_one_by_one(final_dict)


all_process('test_file.txt')
all_process('test_file_2.txt')
