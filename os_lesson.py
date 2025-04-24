import os
import shutil

# Часть 1: Работа с файлами и директориями

path_1 = r'C:\Users\MSI\.vscode\VC\модуль 5\Управление_файлами'
file1_path = os.path.join(path_1, 'file1.txt')
file2_path = os.path.join(path_1, 'file2.txt')

text_1 = 'Калининград — один из крупнейших городов России, расположенный на берегу Балтийского моря в устье реки Преголи.' \
'Он является центром одноимённой области, уместившейся между Польшей и Литвой.'

text_2 = 'Климат Калининграда переходный от морского к континентальному. ' \
'Он отличается сравнительно высокой влажностью и непредсказуемой погодой, характерной для большинства городов Балтики. ' \
'Лето в Калининграде обычно прохладное, а зима мягкая с небольшими морозами и нестабильным снежным покровом.'


def make_dir(path_directory):
    if not os.path.exists(path_directory):
        os.mkdir(path_directory)

    with open(file1_path, 'w', encoding='utf-8') as file_1_write:
        file_1_write.write(text_1)

    with open(file2_path, 'w', encoding='utf-8') as file_2_write:
        file_2_write.write(text_2)

    print('Директория Управление_файлами:', os.listdir(path_directory))

    with open(file1_path, 'r', encoding='utf-8') as file_1_read:
        data_1 = file_1_read.readlines()
        print(data_1)

    with open(file2_path, 'r', encoding='utf-8') as file_2_read:
        data_2 = file_2_read.readlines()
        print(data_2)


make_dir(path_directory=path_1)


# Часть 2: Удаление файлов и директории
# Удалите исходную директорию "Управление_файлами" вместе с ее содержимым.

del_file = 'file1.txt'
move_file = 'file2.txt'
new_path_directory = r'C:\Users\MSI\.vscode\VC\модуль 5\Управление_файлами\NEW'

def del_dir(path_directory):
    file_path = os.path.join(path_directory, del_file)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'Файл {del_file} удалён')
    else:
        print(f'Файл {del_file} не найден')

    print('Директория Управление_файлами:', os.listdir(path_directory))

    if not os.path.exists(new_path_directory):
        os.makedirs(new_path_directory)
    
    old_path = os.path.join(path_directory, move_file)
    new_path = os.path.join(new_path_directory, move_file)

    if os.path.exists(old_path) and not os.path.exists(new_path):
        os.rename(old_path, new_path)
        print(f'Файл {move_file} перемещён')
    else:
        print(f'Файл {move_file} не перемещён')

    print('Директория Управление_файлами:', os.listdir(path_directory))
    print('Директория NEW:', os.listdir(new_path_directory))

    shutil.rmtree(path_directory)
    print('Полное удаление выполнено')


del_dir(path_1)