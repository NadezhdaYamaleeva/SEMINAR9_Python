from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler
from random import randint

bot_token = "5915727952:AAFBrPXln0tXaKtOob_jvRQk58BwtAWL5ms"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context = True)
dispatcher = updater.dispatcher

def start (update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет! Выбери необходимое действие:"
        "/display - Показать все записи,"
        "/find - Найти номер по фамилии,"
        "/add - Добавить новую запись,"
        "/delete - Удалить запись,")
    open.init_data_base('people.csv')


def display (update, context):
    context.bot.send_message(update.effective_chat.id, "Показать все записи")


def find (update, context):
    context.bot.send_message(update.effective_chat.id, "Найти номер по фамилии")


def add (update, context):
    context.bot.send_message(update.effective_chat.id, "Добавить новую запись")


def delete (update, context):
    context.bot.send_message(update.effective_chat.id, "Удалить запись")


start_handler = CommandHandler('start', start)
display_handler = CommandHandler('display', display)
find_handler = CommandHandler('find', find)
add_handler = CommandHandler('add', add)
delete_handler = CommandHandler('delete', delete)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(display_handler)
dispatcher.add_handler(find_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(delete_handler)
updater.start_polling()
updater.idle()