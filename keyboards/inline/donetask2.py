from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

donetask2 = InlineKeyboardMarkup(row_wight=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="✅ ЗАДАНИЕ 2. ВЫПОЛНЕНО",
                                          callback_data="donetask2"
                                      )
                                  ]
                              ])