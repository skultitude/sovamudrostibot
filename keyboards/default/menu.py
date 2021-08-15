from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔥РАССКАЖИ ПРО КУРС")
        ],
        [
            KeyboardButton(text="📚КАКИЕ КНИГИ В БИБЛИОТЕКЕ?")
        ],
        [
            KeyboardButton(text="🎁ЗАБРАТЬ ПОДАРОК")
        ],
        [
            KeyboardButton(text="🤔КАК НАЧАТЬ?")
        ],
    ],
    resize_keyboard=True
)