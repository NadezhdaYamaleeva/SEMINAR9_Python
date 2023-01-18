from view import *
from model import *
import telebot
from telebot import types

bot = telebot.TeleBot('5915727952:AAFBrPXln0tXaKtOob_jvRQk58BwtAWL5ms')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    display = types.KeyboardButton('Показать все записи')
    find = types.KeyboardButton('Найти номер по фамилии')
    add = types.KeyboardButton('Добавить новую запись')
    delete = types.KeyboardButton('Удалить запись')
    markup.add(display, find, add, delete)
    mess = f'Привет, {message.from_user.first_name}. Выбери необходимое действие'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    message.text = message.text.lower()
    if message.text =='Показать все записи':
        all = get_all()
        bot.send_message(message.chat.id, show_all(all), parse_mode='Markdown')
    elif message.text == 'Найти номер по фамилии':
        bot.send_message(message.chat.id, 'Введите фамилию', parse_mode='html')
    elif message.text == 'Добавить новую запись':
        bot.send_message(message.chat.id, "Введите фамилию, имя и номер телефона через пробел", parse_mode='html')
    elif message.text == 'Удалить запись':
        bot.send_message(message.chat.id, 'Введите число', parse_mode='html')
    elif message.text == 'photo':
        photo = open('main_bot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        try:
            number = int(message.text)
            delete(number-1)
            bot.send_message(message.chat.id, 'Запись успешно удалена', parse_mode='html')
        except:
            if len(message.text.split(' '))==1:
                all = get_all()
                bot.send_message(message.chat.id, searching(all, message.text.strip()), parse_mode='html')
            elif len(message.text.split(' '))==3:
                add(message.text.title().split(' '))
                bot.send_message(message.chat.id, 'Запись добавлена', parse_mode='html')
            


bot.polling(none_stop=True)
