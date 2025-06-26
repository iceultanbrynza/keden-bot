from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart

from redis_async import isRegistered
from config import URL
from keyboard import (registration_web_page_keyboard,
                            options_keyboard,
                            renew_data_keyboard)

router = Router()



@router.message(CommandStart())
async def start_and_send_webpage(message: Message):
    await message.answer(text='Вас приветствует Keden Bot. Здесь Вы можете сообщить о проблемах, возникших при пользовании нашим сервисом. Чтобы начать, зарегистрируйтесь ⬇️',
                         reply_markup=registration_web_page_keyboard)
    await message.answer(text='Если уже зарегистрированы, рассмотрите следующие опции...',
                         reply_markup=options_keyboard)

@router.message(F.text == 'Регистрационные данные')
async def renew_and_send_webpage(message: Message):
    if await isRegistered(message.chat.id, URL):
        await message.answer(text='Если нет необходимости обновлять данные, то выберете другую опцию ниже',
                            reply_markup=renew_data_keyboard)
    else:
        await message.answer(text='Вы не зарегистрированы. Пройдите регистрацию с помощью команды /start')
