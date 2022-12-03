#########################################################
from config import bot
import config
from time import sleep
import re
#########################################################
# Aquí vendrá la implementación de la lógica del bot

@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "Hola, soy un \U0001F916, ¿cómo estás?",
        parse_mode="Markdown") 
    
@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
   
    bot.reply_to(
        message,
        "\U0001F63F Ups, no entendí lo que me dijiste.")

#########################################################
if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################