from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"В этом боте нельзя отправлять сообщения. По всем вопросам пиши [мне в личные сообщения](http://t.me/sova_mudrosti)", parse_mode='Markdown')
