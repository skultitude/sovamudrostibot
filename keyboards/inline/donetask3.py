from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

donetask3 = InlineKeyboardMarkup(row_wight=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="✅ ЗАДАНИЕ 3. ВЫПОЛНЕНО",
                                          callback_data="donetask3"
                                      )
                                  ]
                              ])