from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

final = InlineKeyboardMarkup(row_wight=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="🎁 ЗАБРАТЬ ПОДАРОК 🎁",
                                          callback_data="final"
                                      )
                                  ]
                              ])