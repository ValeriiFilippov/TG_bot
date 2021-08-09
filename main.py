import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from handlers.handler import send_welcome, echo


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(send_welcome, commands=['start', 'help'])
dp.register_message_handler(echo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)