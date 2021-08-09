from weather_api import get_weather
from aiogram import types


async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm weather bot!\n Enter your citi, please")


async def echo(message: types.Message):
    info = get_weather(message.text)
    await message.answer(info)
