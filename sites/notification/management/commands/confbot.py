from django.conf import settings

import telebot


bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)
