from aiogram.dispatcher.filters import Text
from aiogram import types

from handlers.users.messages import MESSAGES
from keyboards.inline import donetask1
from loader import bot

from data.config import PROVIDER_TOKEN
from loader import dp

from aiogram.types.message import ContentType

@dp.callback_query_handler(text_contains="howtostart")
async def process_buy_command(message: types.Message):

    await bot.send_invoice(message.from_user.id,
                           title=MESSAGES['title'],
                           description=MESSAGES['description'],
                           provider_token=PROVIDER_TOKEN,
                           currency='rub',
                           is_flexible=False,  # True если конечная цена зависит от способа доставки
                           prices=[types.LabeledPrice(label='Стоимость', amount=30000)],
                           start_parameter='course',
                           payload='some-invoice-payload-for-our-internal-use',
                           need_name='true'
                           )

    @dp.pre_checkout_query_handler()
    async def process_pre_checkout_query(query: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)

        @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
        async def process_successful_payment(message: types.Message):
            await bot.send_message(
                message.chat.id, MESSAGES['task1'], parse_mode='Markdown', disable_web_page_preview='true', reply_markup=donetask1)