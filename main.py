from aiogram import Bot, Dispatcher, types, executor
from os import getenv

TOKEN = getenv('token')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}')


@dp.message_handler(commands='about')
async def cmd_about(msg: types.Message):
    await msg.answer('Я бот который создан по консультации "Иннополис"')


if __name__ == '__main__':
    executor.start_polling(dp)
