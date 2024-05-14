from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('7166099528:AAEZ--6lRWUIezdRAVelCT5n6U7AyZEwU1w')
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    b1 = types.InlineKeyboardButton(text='Открыть веб страницу', web_app=WebAppInfo(url='https://danbzg.github.io/Shop/'))
    markup = types.InlineKeyboardMarkup(inline_keyboard=[[b1]]) 
    await message.answer('Привет, мой друг!', reply_markup=markup)






async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())