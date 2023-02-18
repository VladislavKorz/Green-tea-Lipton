from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from telebot import types

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)

@bot.message_handler(commands=['start'])
def welcome(message):
    
    bot.send_message(message.chat.id, "Здравствуйте , {0.first_name}!\nЯ - {1.first_name}, бот для уведомлений организации РоссМолодеж ".format(message.from_user,bot.get_me()),)

def notice(message):
    bot.send_message(message.from_user.id,message.chat.id, message.text)


bot.polling(non_stop=True)
