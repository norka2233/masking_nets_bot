import telebot
from secret_keys import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, 'Вітаю, чим можу допомогти?')


bot.infinity_polling()
