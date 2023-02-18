import html2text
from loguru import logger

from notification.management.commands.confbot import bot


def notice(message):
    bot.send_message(message.from_user.id,message.chat.id, message.text)


def send_message_to_telegram_chat(telegram_id, title, text):
    bot.send_message(telegram_id, html2text.html2text(f"{title}<br>{text}"), parse_mode='HTML')
