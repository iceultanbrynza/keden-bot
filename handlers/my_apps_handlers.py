from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import WebAppInfo

import httpx
from datetime import datetime

from config import URL, DJANGO_URL
from redis_async import isRegistered


# BITRIX USER DEFINED FIELDS
CRITICALLITY = {
    1988: "Низкая",
    1989: "Средняя",
    1990: "Высокая",
    2131: "Критичная"
}
MODULE = {
    1991:"ПИ",
    1992:"ТД",
    1993:"Таможенные реестры",
    2154:"ТДТС",
    2155:"МВХ",
    2156: "Обеспечение",
    2157: "ПТД"
}

router = Router()

@router.message(F.text == 'Мои заявки')
async def choose_role(message:Message):
    if await isRegistered(str(message.chat.id), URL):
        async with httpx.AsyncClient() as client:
            try:
                params = {
                    "entityTypeId": 1444,
                    "filter[ufCrm168UserChatId]": message.chat.id
                }
                response = await client.post(f'{URL}/crm.item.list', params=params)
            except httpx.RequestError as e:
                return await message.answer('Ошибка. Попробуйте еще раз.')
            else:
                result = response.json().get('result', {})
                items = result.get('items', [])
                if not items:
                    return await message.answer('Вы еще не создавали заявку. Но вы можете создать ее сейчас ⬇️')

        text=""
        buttons = []
        for item in items:
            id = item.get('id', '')
            date = item.get('createdTime', '')
            dt = datetime.fromisoformat(date)
            formatted_date = dt.strftime("%d.%m.%Y / %H:%M")
            criticallity = item.get('ufCrm168Criticality', '')
            criticallity_text = CRITICALLITY.get(criticallity, 'еще не определена') if criticallity else 'еще не определена'
            module = item.get('ufCrm168SelectModule', '')
            module_text = MODULE.get(module, 'еще не определена') if module else 'не определена'
            answer = item.get('ufCrm168DecisionText', '')
            button = InlineKeyboardButton(text=f'Заявка #{id}', web_app=WebAppInfo(url=f"{DJANGO_URL}/kedenbot/get_appl/{id}"))
            buttons.append([button])
            text += f"Заявка №{id} от {formatted_date}, критичность - {criticallity_text}, модуль - {module_text} - По вашей заявке поступил ответ: {answer}.\n\n"

        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

        await message.answer(text=text)
        await message.answer('Выберите какую заявку просмотреть:',
                            reply_markup=keyboard)

    else:
        await message.answer('Вы не зарегистрированы. Пройдите регистрацию с помощью команды /start')