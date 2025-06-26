from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from keyboard import (role_keyboard,
                            UVED_keyboard,
                            UVED_TR_keyboard,
                            UVED_DT_keyboard,
                            UDL_keyboard,
                            UDL_DT_keyboard)
from redis_async import isRegistered
from config import URL
router = Router()
# запрос на Django который возвращает фронт, отсюда получаем текст
# запрос на Django, где делаются все нужные запросы на Битрикс (contactId, Module, ) + текст

@router.message(F.text == 'Подать заявку')
async def choose_role(message:Message):
    exists = await isRegistered(str(message.chat.id), URL)
    if exists:
        await message.answer('Выберите вашу роль в системе:',
                            reply_markup=role_keyboard)
    else:
        await message.answer('Вы не зарегистрированы. Пройдите регистрацию с помощью команды /start')

@router.callback_query(F.data == 'APPLY: NAZAD')
async def UVED_modules(callback:CallbackQuery):
    await callback.message.edit_text('Выберите вашу роль в системе:',
                                    reply_markup=role_keyboard)

@router.callback_query(F.data == 'APPLY: UVED: NAZAD')
async def UVED_modules(callback:CallbackQuery):
    await callback.message.edit_text('Список доступных модулей:',
                                    reply_markup=UVED_keyboard)

@router.callback_query(F.data == 'APPLY: UDL: NAZAD')
async def UVED_modules(callback:CallbackQuery):
    await callback.message.edit_text('Список доступных модулей:',
                                    reply_markup=UDL_keyboard)

@router.callback_query(F.data == 'APPLY: UVED')
async def UVED_modules(callback:CallbackQuery):
    await callback.message.edit_text('Список доступных модулей:',
                                    reply_markup=UVED_keyboard)

@router.callback_query(F.data == 'APPLY: UVED: DT')
async def UVED_DT_modules(callback:CallbackQuery):
    await callback.message.edit_text('Выберите нужный раздел из модуля "Декларации на товары"',
                                    reply_markup=UVED_DT_keyboard)


@router.callback_query(F.data == 'APPLY: UVED: TR')
async def UVED_TR_modules(callback:CallbackQuery):
    await callback.message.edit_text('Выберите нужный раздел из модуля "Таможенный реестр"',
                                    reply_markup=UVED_TR_keyboard)

@router.callback_query(F.data == 'APPLY: UDL')
async def UDL_modules(callback:CallbackQuery):
    await callback.message.edit_text('Список доступных модулей:',
                                      reply_markup=UDL_keyboard)

@router.callback_query(F.data == 'APPLY: UDL: DT')
async def UDL_DT_modules(callback:CallbackQuery):
    await callback.message.edit_text('Выберите нужный раздел из модуля "Декларации на товары"',
                                      reply_markup=UDL_DT_keyboard)