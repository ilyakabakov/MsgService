import asyncio

from bot_initializer import bot_instance, dp
from handlers import clients


async def main():
    try:
        print("Bot started")
        dp.include_router(clients.client_router)
        await bot_instance.delete_webhook(
            drop_pending_updates=True
        )
        await dp.start_polling(bot_instance)

    except Exception as ex:
        print(f" Error: {ex}")


if __name__ == '__main__':
    asyncio.run(main())
