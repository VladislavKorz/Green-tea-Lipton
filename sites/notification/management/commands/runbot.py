from loguru import logger

from notification.management.commands.confbot 
import bot



@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте , {0.first_name}!\nЯ - {1.first_name}, бот для уведомлений организации РоссМолодеж ".format(message.from_user, bot.get_me())+f"{message.from_user.id}",)




bot.polling(non_stop=True)

# bot.infinity_polling()
