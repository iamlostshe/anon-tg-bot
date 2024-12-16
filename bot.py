# Встроенные модули
import asyncio
from os import getenv

# Не встроенные модули
from dotenv import load_dotenv
from loguru import logger

# Aiogram
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

# Мои модули (локальные)
import messages

# TODO дописать синхронизацию с бд
# для сохранения в памяти анонимных сообщений

# import db

# Получам токен из .env
load_dotenv()
TOKEN = getenv("TOKEN")
ADMINS_ID = getenv("ADMINS_ID").split(', ')

# Инициализируем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Отвечаем на приветственное сообщение (/start)
@dp.message(CommandStart())
async def command_start_handler(msg: Message) -> None:
    # Отвечаем пользователю
    await msg.answer(messages.start_msg(msg.from_user.first_name))
    # TODO Записываем пользователя в базу данных
    #db.add_user(msg.from_user.id)
    # Выводим информацию в консоль (лог)
    logger.info('/start id={}, username={}, url={}', msg.from_user.id, msg.from_user.username, msg.from_user.username)

# Отвечаем на любое другое сообщение
@dp.message()
async def echo_handler(msg: Message) -> None:
    # Отвечаем пользователю
    await msg.answer(messages.success(msg.from_user.first_name))
    # Пройдемся по всем админам
    for id in ADMINS_ID:
        # Отправляем сообщение об отправителе админу канала
        #await bot.send_message(id, messages.info(msg.from_user.id, msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.language_code))
        # Отправляем текст сообщения админу
        await bot.send_message(id, msg.text)
    # Выводим информацию в консоль (лог)
    logger.info('[m] id={}, username={}, text={}, url=https://t.me/{}', msg.from_user.id, msg.from_user.username, msg.text, msg.from_user.username)


# Запускаем бота
async def main() -> None:
    logger.info('Bot start polling...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
