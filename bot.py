import telebot

# Создаем экземпляр бота (замените 'YOUR_BOT_TOKEN' на токен от BotFather)
bot = telebot.TeleBot('TELEGRAM_BOT_TOKEN')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот. Напиши мне 'привет' или 'как дела'!")


# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Приводим текст сообщения к нижнему регистру для удобства сравнения
    text = message.text.lower()

    if text == 'привет':
        bot.reply_to(message, 'Привет-привет! Чем могу помочь?')
    elif text == 'как дела':
        bot.reply_to(message, 'У меня всё отлично, спасибо! А у тебя?')
    else:
        bot.reply_to(message, 'Я понимаю только "привет" и "как дела". Попробуй ещё раз!')


# Запуск бота
if __name__ == '__main__':
    print('Бот запущен...')
    bot.polling(none_stop=True)
