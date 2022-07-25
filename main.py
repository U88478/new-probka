import os
# from aiogram import Bot, Dispatcher, executor
import telebot
import logging
from config import *
from flask import Flask, request

# bot = Bot(token, parse_mode="HTML")
# dp = Dispatcher(bot)
bot = telebot.TeleBot(token)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(commands='start', commands_prefix='/')
def start(message):
    await message.reply("Доброго пожалувать, виход там 👉")

@server.route(f'/{token}', methods='POST')
def redirect_message():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

if __name__ == '__main__':
    bot.remove_webhool()
    bot.set_webhook(url=app_url)
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    # executor.start_polling(dp)
