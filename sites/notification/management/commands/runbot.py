from loguru import logger
from django.urls import reverse
from django.conf import settings 
import telebot

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте , {0.first_name}!\nЯ - {1.first_name}, бот для уведомлений организации РоссМолодеж ".format(message.from_user, bot.get_me())+f"{message.from_user.id}",)
    bot.send_message(
        message.chat.id, f"Для синхронизации с сайтом перейдите по ссылке:\n {settings.ABSOLUTE_URL + reverse('sync',kwargs={'user_id':message.from_user.id})}")


def notice(message):
    bot.send_message(message.from_user.id,message.chat.id, message.text)


def send_message_to_telegram_chat(telegram_id, title, text):
    bot.send_message(telegram_id, html2text.html2text(f"{title}<br>{text}"), parse_mode='HTML')




bot.polling(non_stop=True)

# bot.infinity_polling()
