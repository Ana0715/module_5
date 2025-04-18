import csv
import json
from datetime import datetime

# Задание 1: Работа с JSON файлом

def students_info(filename):
    with open(filename, 'r', encoding='utf-8') as json_file:
        student_list = json.load(json_file)

        if not student_list:
            return 'Список студентов пуст'
        
        max_age = 0
        count_python = 0
        for student in student_list:
            if student['возраст'] > max_age:
                max_age = student['возраст']
                old_age_student = student
            if 'Python' in student['предметы']:
                count_python += 1
        
    return (
        f'Общее количество студентов: {len(student_list)}\n'
        f'Студент с самым высоким возрастом: {old_age_student}\n'
        f'Количество студентов, изучающих Python: {count_python}\n'
    )

print(students_info('4_students.json'))


# Задание 2: Работа с CSV файлом

def sales_info(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = list(csv.DictReader(csv_file))

        if not reader:
            return 'Данные отсутствуют'
        
        all_summ_for_year = sum([(int(row['Сумма'])) for row in reader])
        max_volume = [(row['Продукт']) for row in reader]
        count = 0
        for row in max_volume:
            if max_volume.count(row) > count:
                count = max_volume.count(row)
                count_info = row
        data = {}
        month = {
            1:'Январь',
            2:'Февраль',
            3:'Март',
            4:'Апрель',
            5:'Май',
            6:'Июнь',
            7:'Июль',
            8:'Август',
            9:'Сентябрь',
            10:'Октябрь',
            11:'Ноябрь',
            12:'Декабрь'
        }
        for row in reader:
            datetime_row = month[datetime.strptime(row['Дата'], '%Y-%m-%d').date().month]
            if datetime_row in data:
                data[datetime_row] += int(row['Сумма'])
            else:
                data[datetime_row] = int(row['Сумма'])
        

    return (
        f'Общая сумма продаж за период: {all_summ_for_year}\n'
        f'Продукт с самым высоким объемом продаж: {count_info} = {count}\n'
        f'Cуммы продаж для каждого месяца: {data}\n'
    )

print(sales_info('4_sales.csv'))


# Задание 3: Комбинированная работа с JSON и CSV

def employees_info(filename_employees_json, filename_performance_csv):
    with open(filename_employees_json, 'r', encoding='utf-8') as json_file_employ:
        with open (filename_performance_csv, 'r', encoding='utf-8') as csv_file_perf:
            data_json = json.load(json_file_employ)
            data_csv = list(csv.DictReader(csv_file_perf))

            if not data_json or not data_csv:
                return 'Данные не обнаружены'
            
            all_info_dict = []
            for row_csv in data_csv:
                for row_json in data_json:
                    if int(row_csv['employee_id']) == row_json['id']:
                        all_info_dict.append(
                            {
                                'id' : row_json['id'],
                                'имя' : row_json['имя'],
                                'должность' : row_json['должность'],
                                'производительность' : int(row_csv['performance'])
                            }
                        )

            def print_info(dictionary):
                return [row for row in dictionary]

            perf_list = [row['производительность'] for row in all_info_dict]
            middle_perf = sum(perf_list) / len(perf_list)
            max_performance = all_info_dict[0]['производительность']
            for perf in all_info_dict:
                if perf['производительность'] > max_performance:
                    max_performance = perf['производительность']
                    max_performance_employee = perf



    return (f'Сотрудники и их производительность: {print_info(all_info_dict)}\n'
        f'Средняя производительность среди сотрудников: {middle_perf}\n'
        f'Сотрудник с наивысшей производительностью: {max_performance_employee}\n')


print(employees_info('4_employees.json', '4_performance.csv'))


