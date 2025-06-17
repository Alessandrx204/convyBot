import os
from aiogram.exceptions import TelegramBadRequest
from converter import Converter
from aiogram import Router, F, Bot
from aiogram.types import Message, InputFile, FSInputFile, ReactionTypePaid, ReactionTypeEmoji

import configs

conv_router: Router = Router()

bot = Bot(configs.BOT_TOKEN)

@conv_router.message(F.document)
async def WEBM_Handling(message: Message):
    our_file = message.document
    #The first check (file.file_name) verifies that the value exists and is not a non-empty string. Only if it is true, then evaluate the second (endswith).
    if our_file.file_name and our_file.file_name.endswith(".webm"):
        #dwld file
        if message.document.file_size > 20_000_000:  # 20 MB
            await message.reply("File is way to big to be processed thru Telegram API (max 20MB).😭️️️️️️")
            return #giveup
        file_info = await message.bot.get_file(our_file.file_id)

        file_path = file_info.file_path
        webm_video = os.path.join(os.path.dirname(__file__), 'downloaded_WEBM_video.webm')
        #await message.answer('ok') #those are mjust meant to be used in debug
        mp4_video = os.path.join(os.path.dirname(__file__), 'converted_MP4_video.mp4')
        #await message.answer('ok1')#those are mjust meant to be used in debug
        file_bytes_dwld = await message.bot.download_file(file_path)
        #await message.answer('ok2')#those are mjust meant to be used in debug
        with open(webm_video, 'wb') as fi:
            fi.write(file_bytes_dwld.read())
        await message.reply("messaggio salvato")
        returncode = await Converter.webm2mp4(webm_video, mp4_video)
        #await message.answer('ok3')#those are mjust meant to be used in debug
        if returncode == 0:
            # those are mjust meant to be used in debug
            file2b_sent = FSInputFile(path=mp4_video)
            #await message.answer('ok5')#those are mjust meant to be used in debug
            await message.reply_video(video=file2b_sent, caption="here's thy file")
            os.remove(webm_video)
            os.remove(mp4_video)

            await message.react([configs.goodOutcomeEmoji])  # message.react()
        else:
            print('something went wrong')
            await message.reply('something went wrong, im unable to convert the video 🙈️️️️️️ ')

            await message.react([configs.badOutcomeEmoji])  # message.react()



