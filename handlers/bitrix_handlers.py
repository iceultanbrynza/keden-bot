from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from redis_async import redis_client
from redis_async import isRegistered

from config import URL

import httpx
router = Router()

# Заявка отработана
@router.callback_query(F.data.startswith("applicationDataCompleted/"))
async def ApplIsCompleted(callback:CallbackQuery):
    id = callback.data.split('/')[1]
    kb = callback.message.reply_markup

    body = {
        "entityTypeId": 1444,
        "id": id,
        "fields": {
            "stageId": "DT1444_180:SUCCESS"
        }
    }

    headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
    }
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{URL}/crm.item.update",
                json=body,
                headers=headers
            )
            data = response.json()
        await callback.message.edit_text("Ваша проблема отработана.\n" \
                                        "Если обнаружите новые проблемы, обращайтесь в Keden Bot.\n" \
                                        "Наша тех.поддержка оперативно решит проблему.")

    except httpx.RequestError:
        await callback.message.edit_text("Ошибка. Ответьте еще раз, пожалуйста", reply_markup=kb)

# Заявка НЕ отработана
@router.callback_query(F.data.startswith("applicationDataNotCompleted/"))
async def ApplIsNotCompleted(callback:CallbackQuery):
    id = callback.data.split('/')[1]
    kb = callback.message.reply_markup

    body = {
        "entityTypeId": 1444,
        "id": id,
        "fields": {
            "stageId": "DT1444_180:2"
        }
    }

    headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{URL}/crm.item.update",
                json=body,
                headers=headers
            )
            data = response.json()
        await callback.message.edit_text("Ваша проблема будет рассмотрена повторно")

    except httpx.RequestError:
        await callback.message.edit_text("Ошибка. Ответьте еще раз, пожалуйста", reply_markup=kb)
