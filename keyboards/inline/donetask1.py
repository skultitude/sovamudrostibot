from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

donetask1 = InlineKeyboardMarkup(row_wight=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="✅ ЗАДАНИЕ 1. ВЫПОЛНЕНО",
                                          callback_data="donetask1"
                                      )
                                  ]
                              ])