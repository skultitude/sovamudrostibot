from aiogram import types
from aiogram.types import CallbackQuery

from handlers.users.messages import MESSAGES
from keyboards.inline import donetask1, donetask2, donetask3, final
from loader import dp

PhotoGift2 = 'AgACAgIAAxkDAAMHYRjHhErFVB6DFDTEITPqDeCm1pYAAlG0MRsP-clIlAvHHz9kinQBAAMCAAN3AAMgBA'

@dp.message_handler(commands=['sudoaccess'])
async def sudo_access(message: types.Message):
    await message.answer(MESSAGES['task1'], parse_mode='Markdown', disable_web_page_preview='true', reply_markup=donetask1)


@dp.callback_query_handler(text_contains="donetask1")
async def process_callback(call: CallbackQuery):
    await call.answer(cache_time=2)
    await call.message.answer(MESSAGES['task2'], reply_markup=donetask2, parse_mode='Markdown')


@dp.callback_query_handler(text_contains="donetask2")
async def process_callback(call: CallbackQuery):
    await call.answer(cache_time=2)
    await call.message.answer(MESSAGES['task3'], reply_markup=donetask3, parse_mode='Markdown')


@dp.callback_query_handler(text_contains="donetask3")
async def process_callback(call: CallbackQuery):
    await call.answer(cache_time=2)
    await call.message.answer(MESSAGES['gift2'], reply_markup=final, parse_mode='Markdown')


@dp.callback_query_handler(text_contains="final")
async def process_callback(call: CallbackQuery):
    await call.answer(cache_time=2)
    await call.message.answer_photo(PhotoGift2, caption=MESSAGES['gift_caption'], parse_mode='Markdown')