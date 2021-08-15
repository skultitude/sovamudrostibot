from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from handlers.users.messages import MESSAGES
from keyboards.inline import choise
from loader import dp

PhotoGift = 'AgACAgIAAxkDAAMIYRjHha5U9tjxYCH2sktemLVv5rEAAlK0MRsP-clI3qERyxOpaYoBAAMCAAN3AAMgBA'


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'''Приветствую, {message.from_user.first_name} 👋🏻
Меня зовут Ольга.

Вместе со мной ты пройдёшь мини-курс эффективного чтения, после которого твоя жизнь точно изменится в лучшую сторону.'''
                         , reply_markup=choise)


@dp.callback_query_handler(text_contains="about")
async def process_callback(call: CallbackQuery):
    await call.answer(cache_time=2)
    await call.message.edit_text(MESSAGES['about'], reply_markup=choise, parse_mode='Markdown')


@dp.callback_query_handler(text_contains="book")
async def process_callback(call: CallbackQuery):
    await call.answer(cache_time=2)
    await call.message.edit_text(MESSAGES['book'],
                                 reply_markup=choise, parse_mode='Markdown')


@dp.callback_query_handler(text_contains="gift")
async def process_callback(call: CallbackQuery):
    await call.answer(cache_time=2)
    await call.message.answer_photo(PhotoGift)
    await call.message.answer(MESSAGES['gift'], reply_markup=choise)
