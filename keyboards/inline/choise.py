from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choise = InlineKeyboardMarkup(row_wight=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="馃敟 袪袗小小袣袗袞袠 袩袪袨 袣校袪小",
                                          callback_data="about"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="馃摎 袣袗袣袠袝 袣袧袠袚袠 袙 袘袠袘袥袠袨孝袝袣袝?",
                                          callback_data="book"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="馃巵 袟袗袘袪袗孝鞋 袩袨袛袗袪袨袣",
                                          callback_data="gift"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="馃 袣袗袣 袧袗效袗孝鞋?",
                                          callback_data="howtostart"
                                      )
                                  ]
                              ])