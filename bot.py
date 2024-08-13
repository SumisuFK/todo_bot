import asyncio
import os
#import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import user
from app.database.models import async_main


bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    load_dotenv()
    dp.include_router(user)
    await async_main()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')