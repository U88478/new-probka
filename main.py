import os
from aiogram import Bot, Dispatcher, executor
import logging
from config import *

bot = Bot(token, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.DEBUG)

@dp.message_handler(commands='start', commands_prefix='/')
async def start(message):
    ans = await message.reply("Доброго пожалувать, виход там 👉")
    message.delete()
    ans.delete()

if __name__ == '__main__':
    executor.start_polling(dp)
