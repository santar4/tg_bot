import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, types

from app import handlers

# from aiogram.dispatcher import router




# Створимо об'єкт Bot


bot = Bot(os.getenv("Token"))

dp = Dispatcher()
dp.include_routers(handlers.router)


# Головна функція пакету
async def main() -> None:
    # Додаемо "меню" з власнимим командами
    await bot.set_my_commands(commands=[
        types.BotCommand(command="/start", description="Старт бот"),
        types.BotCommand(command="/random_quotes", description="Рандомна цитата"),
        types.BotCommand(command="/new_quote", description="Нова цитата"),
        types.BotCommand(command="/cancel", description="Відміна додавання цитати")
    ]
    )
    s = await bot.get_session()

    # Почнемо обробляти події для бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
   