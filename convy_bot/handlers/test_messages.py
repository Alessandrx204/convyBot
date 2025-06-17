#executed in webm_handlers

from aiogram import Router, F, Bot
from aiogram.types import Message, InputFile

test_router: Router = Router()
@test_router.message(F.text.startswith('@'))
async def test_msg(message,bot):
    user= message.from_user
    usr_id = user.id
    usr_username = user.username
    me = await bot.get_me()
    if message.text == '@'+me.username:
        await message.reply(f'{usr_username}[{usr_id}] was so gentle to check if i was all good. thanks for asking <3, yes I am')