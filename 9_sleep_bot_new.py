import telebot
from datetime import datetime
from telebot import types
import os
from dotenv import load_dotenv
import json

load_dotenv()

key_tg = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(key_tg)

HELLO_MESSAGE = 'Доброго дня! Я бот, который будет помогать отслеживать параметры  сна! Используйте команды /sleep, чтобы отметить начало сна, /wake, для отметки окончания сна, /quality, чтобы поставить оценку и /notes, чтобы оставить заметку! Для сохранения введенных данных /save!'
HELLO_REPEAT = 'И снова здравствуйте! Команды всё те же ;)'
SLEEP_MESSAGE = 'Добрых снов! Не забудьте написать, когда проснётесь! Вам поможет команда /wake!'
WAKE_MESSAGE = 'Доброго утра и прекрасного настроения! Оцените свой сон командой /quality и оставьте заметку командой /notes! '
NOTES_MESSAGE = 'Оставьте заметку о качестве сна!'
QUALITY_MESSAGE = 'Поставьте оценку своему сну! (Цифра!)'
SLEEP_ERROR = 'Вы уже сообщили о начале сна!'
WAKE_ERROR = 'Нет записи о начале сна!'
QUALITY_ERROR = 'Неверный формат, введите цифру!'
NOTES_QUALITY_ERROR = 'Для оценки сна необходимо сделать запись о его начале и конце кнопками /sleep и /wake!'
SORRY_TEXT = 'Извините, я пока не могу обработать эту команду!'
SAVE_MESSAGE = 'Выполняю сохранение!'
FINISHED_SAVE_MESSAGE = 'Сохранение выполнено!'
SAVE_ERROR_FORMAT =  'Нет информации {}! Добавьте её и повторите сохранение!'
s_w = {'sleep':0, 'wake':0}
FORMAT = '%Y-%m-%d %H:%M:%S.%f'
FORMAT_ROUND = '%Y-%m-%d %H:%M:%S'
delta_sleep_wake_format = 'Вы спали: {}'
notes_format = 'Заметка "{}" сохранена!'
quality_format = 'Оценка "{}" сохранена!'


users = {}
all_notes = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('/start')
    button2 = types.KeyboardButton('/sleep')
    button3 = types.KeyboardButton('/wake')
    button4 = types.KeyboardButton('/quality')
    button5 = types.KeyboardButton('/notes')
    button6 = types.KeyboardButton('/save')
    markup.add(button1, button2, button3, button4, button5, button6)

    chat_id = message.chat.id
    if chat_id not in users:
        bot.send_message(chat_id, HELLO_MESSAGE, reply_markup=markup)
        users[chat_id] = all_notes
    else:
        bot.send_message(message.chat.id, HELLO_REPEAT, reply_markup=markup)


@bot.message_handler(commands=['sleep'])
def handle_sleep(message):
    chat_id = message.chat.id
    if s_w['sleep'] - s_w['wake'] == 0:
        sleep_time_now = (datetime.now()).strftime(FORMAT)
        sleep_time_round = sleep_time_now[:-7]
        users[chat_id]['time_sleep'] = (str(sleep_time_round))
        bot.send_message(message.chat.id, SLEEP_MESSAGE)
        s_w['sleep'] += 1
    else:
        bot.send_message(message.chat.id, SLEEP_ERROR)


@bot.message_handler(commands=['wake'])
def handle_wake(message):
    chat_id = message.chat.id
    if s_w['sleep'] - s_w['wake'] == 1:
        wake_time_now = (datetime.now()).strftime(FORMAT)
        wake_time_round = wake_time_now[:-7]
        users[chat_id]['time_wake'] = (str(wake_time_round))
        bot.send_message(message.chat.id, WAKE_MESSAGE)
        s_w['wake'] += 1
        delta_sleep_wake = datetime.strptime(users[chat_id]['time_wake'], FORMAT_ROUND) - datetime.strptime(users[chat_id]['time_sleep'], FORMAT_ROUND)
        users[chat_id]['delta_time'] = str(delta_sleep_wake)
        bot.send_message(message.chat.id, delta_sleep_wake_format.format(delta_sleep_wake))
    else:
        bot.send_message(message.chat.id, WAKE_ERROR)


@bot.message_handler(commands=['quality'])
def handle_quality(message):
    chat_id = message.chat.id
    if not 'time_wake' in users[chat_id]:
        bot.send_message(message.chat.id, NOTES_QUALITY_ERROR)
    else:
        mess_qual_next = bot.send_message(message.chat.id, QUALITY_MESSAGE)
        bot.register_next_step_handler(mess_qual_next, save_quality_handler)
def save_quality_handler(message):
    chat_id = message.chat.id
    try:
        quality_now = message.text
        users[chat_id]['qualities'] = (int(quality_now))
        bot.send_message(message.chat.id, quality_format.format(quality_now))
    except:
        mess_qual_next = bot.send_message(message.chat.id, QUALITY_ERROR)
        bot.register_next_step_handler(mess_qual_next, save_quality_handler)



@bot.message_handler(commands=['notes'])
def handle_notes(message):
    chat_id = message.chat.id
    if not 'time_wake' in users[chat_id]:
        bot.send_message(message.chat.id, NOTES_QUALITY_ERROR)
    else:
        mess_note_next = bot.send_message(message.chat.id, NOTES_MESSAGE)
        bot.register_next_step_handler(mess_note_next, save_notes_handler)
def save_notes_handler(message):
    chat_id = message.chat.id
    note_now = message.text
    users[chat_id]['notes'] = (note_now)
    bot.send_message(message.chat.id, notes_format.format(note_now))


@bot.message_handler(commands=['save'])
def check(message):
    chat_id = message.chat.id
    if not 'time_sleep' in users[chat_id]:
        bot.send_message(message.chat.id, SAVE_ERROR_FORMAT.format('/time_sleep'))
    elif not 'time_wake' in users[chat_id]:
        bot.send_message(message.chat.id, SAVE_ERROR_FORMAT.format('/time_wake'))
    elif not 'qualities' in users[chat_id]:
        bot.send_message(message.chat.id, SAVE_ERROR_FORMAT.format('/quality'))
    elif not 'notes' in users[chat_id]:
        bot.send_message(message.chat.id, SAVE_ERROR_FORMAT.format('/notes'))
    else:
        bot.send_message(message.chat.id, SAVE_MESSAGE)
        handle_save()
        bot.send_message(message.chat.id, FINISHED_SAVE_MESSAGE)
def handle_save():
    filename = '9_sleep_bot_info.json'
    
    date_now = str(datetime.now())[:-7]
    all_notes['time_save'] = date_now
    new_data = users
    try:
        with open (filename, encoding='utf-8') as tj_read:
            try:
                list_json = json.load(tj_read)
                if isinstance(list_json, list):
                    list_json.append(new_data)
                else:
                    list_json = [list_json, new_data]
            except json.JSONDecodeError:
                list_json = [new_data]
    except FileNotFoundError:
        list_json = [new_data]

    with open (filename, 'w') as tj_w:
        json.dump(list_json, tj_w, indent=4)
    
    clean_all_notes()
def clean_all_notes():
    all_notes.clear()
    



@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, SORRY_TEXT)
    
    
bot.polling(none_stop=True, interval=0)

