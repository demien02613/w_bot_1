from aiogram import Bot
from aiogram.types import Message
from typing import Dict


async def get_start(message: Message, bot: Bot):
    pass
    # await bot.send_message(1392284754,f"####Hello! <b>BOT SToP</b> !")
    # await message.answer("Hello!")
    await message.reply("Hello!")

# функция для конвертации json в словарь, key - value


async def get_da_mess(data_message: Dict, prefix: str = '', sep: str = '.'):
    correct_dict = {}
    for key, value in data_message.items():
        if value != None:
            if isinstance(value, Dict):
                correct_dict.update(await get_da_mess(data_message=value, prefix=f'{prefix}{key}{sep}'))
            else:
                correct_dict[f'{prefix}{key}'] = value
    return correct_dict
