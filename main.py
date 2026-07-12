import asyncio

from aiogram import Bot, Dispatcher

from app.core.config import config
from app.handlers.vip import vip_router


async def main():
    token = config.bot.bot_token
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.include_router(vip_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Бот запущен!")
        asyncio.run(main())
    except BaseException as e:
        print("Бот отключен!", e)
