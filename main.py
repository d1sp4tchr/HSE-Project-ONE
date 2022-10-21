import telebot

bot = telebot.TeleBot('5633930287:AAHSBuq70NZ-W5pqIBbc7-Vx76tyvT296ho')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И вам привет!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "Hello there":
        bot.send_message(message.chat.id, "General Kenobi", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "В твоих словах есть буквы", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'В твоих словах нет букв, только пикча')
bot.polling(none_stop=True)