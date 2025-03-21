"""Модуль взаимодействия с ботом."""  # noqa: RUF002

import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from loguru import logger

import messages

# Получам токен из .env
load_dotenv()

TOKEN = getenv("TOKEN")
ADMINS_ID = getenv("ADMINS_ID").replace(" ", "").split(",")

# Инициализируем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(msg: Message) -> None:
    """Отвечаем на приветственное сообщение (/start)."""
    # Отвечаем пользователю
    await msg.answer(messages.start_msg(msg.from_user.first_name))

    # Выводим информацию в консоль (лог)
    logger.info(
        "/start id={}, username={}, url={}",
        msg.from_user.id,
        msg.from_user.username,
        msg.from_user.username,
    )

@dp.message()
async def any_message(msg: Message) -> None:
    """Отвечаем на любое другое сообщение."""
    # Отвечаем пользователю
    await msg.answer(messages.success(msg.from_user.first_name))

    # Пройдемся по всем админам
    for admin_id in ADMINS_ID:
        # Отправляем текст сообщения админу
        await bot.send_message(admin_id, msg.text)

    # Выводим информацию в консоль (лог)
    logger.info("[m] id={}, username={}, text={}, url=https://t.me/{}",
        msg.from_user.id,
        msg.from_user.username,
        msg.text, msg.from_user.username,
    )


# Запускаем бота
async def main() -> None:
    """Скрипт инициализации и запуска бота."""
    # Устанавливаем файл для сбора логов  # noqa: RUF003
    logger.add("anon-tg-bot.log")

    # Выводим лог
    logger.info("Bot start polling...")

    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
