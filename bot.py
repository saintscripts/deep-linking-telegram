import telebot

TOKEN = "ваш токен"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])

def lalala(message):

    if message.chat.type == 'private':

        if message.text == '/start ban':

            bot.send_message(message.chat.id, 'бан')

        elif message.text == '/start test':

            bot.send_message(message.chat.id, 'Привет, ты перешёл по реф. ссылки')

        else:

            bot.send_message(message.chat.id, 'Привет')

            

bot.polling()

#by @saintfukk2
