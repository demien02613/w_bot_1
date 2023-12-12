
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, Update
import sys
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart
from aiogram import F
from aiogram.methods import DeleteWebhook
from datetime import datetime
from core.handlers.basic import get_da_mess
from core.settings import BOT_TOKEN, BOT_ADMIN_ID, envF
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

if (BOT_ADMIN_ID == '') | (BOT_TOKEN == '12345678:AaBbCcDdEeFf'):
    print(f'отредактируйте файл {envF} с настройками TOKEN и ADMIN_ID')
    sys.exit(11)

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")


@dp.message(F.document)
async def get_doc(message: Message, bot: Bot):
    await message.answer(f"####Save document <b>{ message.document.mime_type} OK</b>!")
    print("document: =", message.document)
    file = await bot.get_file(message.document.file_id)
    try:
        await bot.download_file(file.file_path, message.document.file_name)
    except:
        print(BaseException)


@dp.message(Command(commands=['start']))
async def get_strt(message: Message, bot: Bot):
    await message.answer(f"#### PRESS start <b>{ message} OK</b>!")
    print("pres start : =", message)


@dp.message(Command(commands=['info']))
async def get_info(message: Message, started_at: str):
    await message.answer(f"#bot_started_at: <b>{ started_at} </b>!")
    print("started at : ", started_at)


@dp.message(F.photo)
async def get_photo(message: Message, bot: Bot):
    pass
    await message.answer(f"####Have foto <b>OK</b>!")
    # file = await bot.download_media(message=message, file_name="photo.jpg")
    print("1id: =", message.photo)
    i = 0
    for ph in message.photo:
        print("id: =", message.photo[i].file_id)
        i += 1
    file = await bot.get_file(message.photo[-1].file_id)
    try:

        await bot.download_file(file.file_path, "photo.jpg")
    except:
        print(BaseException)


async def main3():

    print("asincio - асинхрон - wait 5sec")
    await asyncio.sleep(5)
    print("5 sec done")


@dp.message()
async def cmd_start(message: Message, bot: Bot):
    # print("update: =", update.update_id)
    # print(str(await bot.me().update_id))
    print(message.model_dump_json())
    if message.from_user.id == BOT_ADMIN_ID:
        await message.answer("<tg-spoiler>HI BOSS!</tg-spoiler>")
        print("123", str(F.text))
        # return
    if message.text == 'ex':
        await main3()
        await message.answer("<tg-spoiler>Hello!</tg-spoiler>"+" "+str((await bot.me()).username))
        return
    if message.text == 'exit':
        print("exit - ", str(message.chat.username))
        await message.answer("exiting...")
        await dp.stop_polling()
        await bot.session.close()

    await bot.send_message(message.from_user.id, f"Hello! {message.from_user.first_name} {message.from_user.id}!")
    await message.answer("<tg-spoiler>Hello!</tg-spoiler>")
    await message.reply("Hello!")


# Запуск процесса поллинга новых апдейтов


async def main2():
    while True:
        print("wait 5sec")
        await asyncio.sleep(5)
        # await bot.send_message(1392284754,f"####Hello! <b>BOT SToP</b> !")
        print("heartBeat 5 sec done")


async def main():
    # loop = asyncio.get_event_loop()
    # loop.create_task(main2())
    # dp.startup.register(get_start)
    await bot(DeleteWebhook(drop_pending_updates=True))  # отключаем обновления
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":

    asyncio.run(main())
