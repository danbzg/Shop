import telebot
import requests
import json

bot = telebot.TeleBot('7011544607:AAHt99JFMR8zCannItZFR6HyoNxxNEaR2as')
API = '1ab14e42e9d808e51676a4e6c9ed25c1'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'sun.jfif' if temp > 5.0 else 'sunny.jfif'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан неверно')


bot.polling(none_stop=True)