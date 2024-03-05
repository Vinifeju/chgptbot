from asyncio import run
from aiogram import Bot, Dispatcher

from command_handler import chgptrouter

from config import Config


bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(*[chgptrouter])
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    run(main())
