import datetime

# Часть 1: Работа с текущей датой и временем

now = datetime.datetime.now()
year_for_check = datetime.datetime.strptime('2020-04-24 13:24:59', "%Y-%m-%d %H:%M:%S")

week_days_dict = {
    0:'Понедельник',
    1:'Вторник',
    2:'Среда',
    3:'Четверг',
    4:'Пятница',
    5:'Суббота',
    6:'Воскресенье'
}

now_week_num = now.weekday()
now_week_letter = week_days_dict[now_week_num]

def check_leap_year(check_year):
    if (check_year.year % 4 == 0 or check_year.year % 400 == 0) and check_year.year % 100 != 0:
        return 'Високосный'
    return 'Невисокосный'

print(f'Текущая дата и время: {now}\n'
      f'День недели: {now_week_letter}\n'
      f'Високосный ли сейчас год: {check_leap_year(now)}\n'
      f'Високосный ли 2020 год: {check_leap_year(year_for_check)}')



# Часть 2: Работа с пользовательской датой

year = input('Введите текущую дату в формате "yyyy-mm-dd"("год-месяц-день"): ')

def date_check(date):
    try:
        date_format = datetime.datetime.strptime(date, "%Y-%m-%d")
        return date_format
    except:
        return None

user_data = (date_check(year))

def day_min_sec_check(data):
    if user_data is None:
        return 'Неверная дата'
    now = datetime.datetime.now()
    delta_data = data - now
    if delta_data.total_seconds() < 0:
        return 'Данная дата уже прошла'
    days = delta_data.days
    seconds = delta_data.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'До данной даты: {days} дней, {hours} часов, {minutes} минут'


print(
    day_min_sec_check(user_data)
)