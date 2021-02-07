# Deep Linking для Telegram Ботов

Всем привет! Сегодня поговорим о Deep Linking(Реферальных ссылок) для Telegram Бота.

Я расскажу вам самый простой способ сделать такую систему, без БД и прочего.

# Приступим!

Deep Linking - это вот такие ссылки - https://t.me/usernamebot?=123, когда по ним переходят и нажимают старт происходит отдельное действие которое отличается от обычного старта без таких ссылок.

123 - это уникальный код, по которым бот активирует другое действие, то есть боту приходит команда "/start 123", а не "/start".

Так вот я придумал как это сделать намного легче, как на самом деле это нужно сделать.

# Делаем стандартое действие

  import telebot

  TOKEN = "ваш токен"

  bot = telebot.TeleBot(TOKEN)

Теперь нам нужно сделать чтобы бот реагировал на команду "/start test"

    @bot.message_handler(content_types=['text'])

    def lalala(message):

        if message.chat.type == 'private':

          if message.text == '/start ban':

            bot.send_message(message.chat.id, 'бан')

          elif message.text == '/start test':

            bot.send_message(message.chat.id, 'Привет, ты перешёл по реф. ссылки')

          else:

            bot.send_message(message.chat.id, 'Привет')

            

Вот как сделал это я!

# Ну и заключение

  bot.polling()

Полный код есть на GitHub
