from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choise = InlineKeyboardMarkup(row_wight=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="🔥 РАССКАЖИ ПРО КУРС",
                                          callback_data="about"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="📚 КАКИЕ КНИГИ В БИБЛИОТЕКЕ?",
                                          callback_data="book"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="🎁 ЗАБРАТЬ ПОДАРОК",
                                          callback_data="gift"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="🤔 КАК НАЧАТЬ?",
                                          callback_data="howtostart"
                                      )
                                  ]
                              ])