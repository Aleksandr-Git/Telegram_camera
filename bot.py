import config
import logging
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import sendPhoto as sp

API_TOKEN = config.API_TOKEN
MY_ID = config.MY_ID

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет!', reply_markup=kb.greed_kb)

@dp.message_handler(commands=['Send'])
async def send_photo(message: types.Message):
    p = sp.photo()
#    await bot.send_photo(MY_ID, photo=open("https://img5.goodfon.ru/original/1920x1080/8/57/kotionok-malysh-vzeroshennyi-vzgliad-luzha.jpg"), disable_notification=True)
#    await bot.send_photo(MY_ID, photo=open("./12_56_48_07-05-2021/photo.1.jpg", 'rb'), disable_notification=True)
    await bot.send_photo(MY_ID, photo=p, disable_notification=True)
#    sp.photo()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True)

print('ok')
