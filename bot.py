import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat_id, 'Вітаю, чим можу допомогти?')



