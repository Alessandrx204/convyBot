import asyncio

from  aiogram import Bot, Dispatcher
from handlers.webm_handlers import conv_router
from configs import BOT_TOKEN
from handlers.test_messages import test_router


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



async  def main():
    dp.include_router(conv_router)
    dp.include_router(test_router)
    me = await bot.get_me()
    print(f"🤖 Bot is running: @{me.username}")
    await dp.start_polling(bot)


if __name__ == '__main__':

    asyncio.run(main())
