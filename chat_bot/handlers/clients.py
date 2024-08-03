import aiohttp
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
import bot_initializer


client_router = Router()


@client_router.message(CommandStart())
async def send_welcome(message: types.Message):
    """ Start page handler """
    try:
        await bot_initializer.bot_instance.send_message(
            message.from_user.id,
            text="Hi!\n"
                 "I'm your chat_bot for saving text from messages!\n"
                 "Use command: /new + text to add a new one\n"
                 "/messages to see all saved messages "
        )
    except Exception as e:
        print(f" Error {e}")


@client_router.message(Command('messages'))
async def get_messages(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{bot_initializer.WEB_API_URL}/messages/") as response:
            messages = await response.json()
            text = "\n".join([f"{msg['author']}: {msg['text']}" for msg in messages['items']])
            await message.answer(text if text else "No messages yet.")


@client_router.message(Command('new'))
async def new_message(message: types.Message):
    msg_text = message.text

    print(msg_text)
    if not msg_text:
        await message.answer("Please provide a message text.")
        return
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{bot_initializer.WEB_API_URL}/message/",
                                json={"text": msg_text, "author": message.from_user.username}) as response:
            if response.status == 200:
                await message.answer("Message added successfully!")
            else:
                await message.answer("Failed to add message.")
