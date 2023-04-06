from aiogram.types import ReplyKeyboardMarkup,  \
                          KeyboardButton

bthInfo = KeyboardButton('/Send')


greed_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(bthInfo)
