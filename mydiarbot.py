import telebot

bot = telebot.TeleBot('YOUR TOKEN')


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, "HELLO!!!!")


bot.polling()
