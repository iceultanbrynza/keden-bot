from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo
from config import DJANGO_URL as URL

# Инлайн кнопки для вызова страницы регистрации

registration_web_page_button = InlineKeyboardButton(
                                    text='Зарегистрироваться',
                                    web_app=WebAppInfo(url=f'{URL}/kedenbot/register')
                                )
registration_web_page_keyboard = InlineKeyboardMarkup(inline_keyboard=[[registration_web_page_button]])

### Опции

apply_button = KeyboardButton(
                    text='Подать заявку'
                )
already_applied_button = KeyboardButton(
                    text='Мои заявки'
                )

reg_data_button = KeyboardButton(
                    text='Регистрационные данные'
                )

options_keyboard = ReplyKeyboardMarkup(keyboard=[[apply_button],
                                                 [already_applied_button],
                                                 [reg_data_button]],
                                                 resize_keyboard=True)

### Обновление данный

renew_data = InlineKeyboardButton(
                    text='Обновить данные',
                    web_app=WebAppInfo(url=f'{URL}/kedenbot/register?mode=edit')
                )

renew_data_keyboard = InlineKeyboardMarkup(inline_keyboard=[[renew_data]])

### УДЛ/УВЭД

UVED_button = InlineKeyboardButton(
                        text='УВЭД',
                        callback_data='APPLY: UVED'
                    )

UDL_button = InlineKeyboardButton(
                        text='УДЛ',
                        callback_data='APPLY: UDL'
                    )

role_keyboard = InlineKeyboardMarkup(inline_keyboard=[[UVED_button],
                                                      [UDL_button]])

###УВЭД список
NAZAD_button = InlineKeyboardButton(text='Назад', callback_data='APPLY: NAZAD')

URLUVED = URL + '/kedenbot/uved'
UVED_PI_button = InlineKeyboardButton(text='1.Предварительное информирование (ПИ)', web_app=WebAppInfo(url=f'{URLUVED}?module=ПИ'))
UVED_TD_button = InlineKeyboardButton(text='2.Транзитная декларация (ТД)', web_app=WebAppInfo(url=f'{URLUVED}?module=ТД'))
UVED_IK_button = InlineKeyboardButton(text='3.Интегрированный контроль (ИК)', web_app=WebAppInfo(url=f'{URLUVED}?module=ИК'))
UVED_DT_button = InlineKeyboardButton(text='4.Декларация на товары (ДТ)', callback_data='APPLY: UVED: DT')
UVED_TR_button = InlineKeyboardButton(text='5.Таможенные реестры', callback_data='APPLY: UVED: TR')
UVED_MVH_button = InlineKeyboardButton(text='6.Место временного хранения (МВХ)', web_app=WebAppInfo(url=f'{URLUVED}?module=МВХ'))
UVED_O_button = InlineKeyboardButton(text='7.Обеспечение', web_app=WebAppInfo(url=f'{URLUVED}?module=О'))

UVED_keyboard = InlineKeyboardMarkup(inline_keyboard=[[UVED_PI_button],
                                                      [UVED_TD_button],
                                                      [UVED_IK_button],
                                                      [UVED_DT_button],
                                                      [UVED_TR_button],
                                                      [UVED_MVH_button],
                                                      [UVED_O_button],
                                                      [NAZAD_button]])

UVED_DT_1_button = InlineKeyboardButton(text='Платежи', web_app=WebAppInfo(url=f'{URLUVED}?module=ДТ&sect=Платежи'))
UVED_DT_2_button = InlineKeyboardButton(text='ДТС', web_app=WebAppInfo(url=f'{URLUVED}?module=ДТ&sect=ДТС'))
UVED_DT_3_button = InlineKeyboardButton(text='Запрос документов', web_app=WebAppInfo(url=f'{URLUVED}?module=ДТ&sect=ЗД'))
UVED_NAZAD_button = InlineKeyboardButton(text='Назад', callback_data='APPLY: UVED: NAZAD')
UVED_DT_keyboard = InlineKeyboardMarkup(inline_keyboard=[[UVED_DT_1_button],
                                                         [UVED_DT_2_button],
                                                         [UVED_DT_3_button],
                                                         [UVED_NAZAD_button]])

UVED_TR_1_button = InlineKeyboardButton(text='Информация о форме собственности', web_app=WebAppInfo(url=f'{URLUVED}?module=ТР&sect=ИФС'))
UVED_TR_2_button = InlineKeyboardButton(text='Сведения о наличии договора страхования', web_app=WebAppInfo(url=f'{URLUVED}?module=ТР&sect=СНДС'))
UVED_TR_3_button = InlineKeyboardButton(text='Отсутствие в реестре', web_app=WebAppInfo(url=f'{URLUVED}?module=ТР&sect=ОР'))
UVED_TR_keyboard = InlineKeyboardMarkup(inline_keyboard=[[UVED_TR_1_button],
                                                         [UVED_TR_2_button],
                                                         [UVED_TR_3_button],
                                                         [UVED_NAZAD_button]])

### УДЛ список

URLUDL = URL + '/kedenbot/udl'
UDL_PI_button = InlineKeyboardButton(text='1.Предварительное информирование (ПИ)', web_app=WebAppInfo(url=f'{URLUDL}?module=ПИ'))
UDL_TD_button = InlineKeyboardButton(text='2.Транзитная декларация (ТД)', web_app=WebAppInfo(url=f'{URLUDL}?module=ТД'))
UDL_IK_button = InlineKeyboardButton(text='3.Интегрированный контроль (ИК)', web_app=WebAppInfo(url=f'{URLUDL}?module=ИК'))
UDL_DTD_button = InlineKeyboardButton(text='4.Досмотр-ТД', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТД'))
UDL_DT_button = InlineKeyboardButton(text='5.Декларация на товары (ДТ)', callback_data='APPLY: UDL: DT')
UDL_PTD_button = InlineKeyboardButton(text='6.Пассажирская таможенная декларация (ПТД)', web_app=WebAppInfo(url=f'{URLUDL}?module=ПТД'))
UDL_TR_button = InlineKeyboardButton(text='7.Таможенные реестры', web_app=WebAppInfo(url=f'{URLUDL}?module=ТР'))
UDL_MVH_button = InlineKeyboardButton(text='8.Место временного хранения (МВХ)', web_app=WebAppInfo(url=f'{URLUDL}?module=МВХ'))
UDL_TDTS_button = InlineKeyboardButton(text='9.ТДТС', web_app=WebAppInfo(url=f'{URLUDL}?module=ТДТС'))
UDL_O_button = InlineKeyboardButton(text='10.Обеспечение', web_app=WebAppInfo(url=f'{URLUDL}?module=О'))
UDL_keyboard = InlineKeyboardMarkup(inline_keyboard=[[UDL_PI_button],
                                                     [UDL_TD_button],
                                                     [UDL_IK_button],
                                                     [UDL_DTD_button],
                                                     [UDL_DT_button],
                                                     [UDL_PTD_button],
                                                     [UDL_TR_button],
                                                     [UDL_MVH_button],
                                                     [UDL_TDTS_button],
                                                     [UDL_O_button],
                                                     [NAZAD_button]])

UVED_NAZAD_button = InlineKeyboardButton(text='Назад', callback_data='APPLY: UDL: NAZAD')
UDL_DT_1_button = InlineKeyboardButton(text='СУР', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=СУР'))
UDL_DT_2_button = InlineKeyboardButton(text='СИР', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=СИР'))
UDL_DT_3_button = InlineKeyboardButton(text='Запрос документов', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=ЗД'))
UDL_DT_4_button = InlineKeyboardButton(text='Требование о продлении срока выпуска товаров', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=ТПСВТ'))
UDL_DT_5_button = InlineKeyboardButton(text='Требование ТО о внесении изменений в ДТ до выпуска', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=ТТОВИТДВ'))
UDL_DT_6_button = InlineKeyboardButton(text='ФРРО', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=ФРРО'))
UDL_DT_7_button = InlineKeyboardButton(text='Завершение контроля', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=ЗК'))
UDL_DT_8_button = InlineKeyboardButton(text='Решение о выпуске', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=РВ'))
UDL_DT_9_button = InlineKeyboardButton(text='Факт вывоза', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=ФВ'))
UDL_DT_10_button = InlineKeyboardButton(text='ПДФ Файл', web_app=WebAppInfo(url=f'{URLUDL}?module=ДТ&sect=ПДФ'))
UDL_DT_keyboard = InlineKeyboardMarkup(inline_keyboard=[[UDL_DT_1_button],
                                                        [UDL_DT_2_button],
                                                        [UDL_DT_3_button],
                                                        [UDL_DT_4_button],
                                                        [UDL_DT_5_button],
                                                        [UDL_DT_6_button],
                                                        [UDL_DT_7_button],
                                                        [UDL_DT_8_button],
                                                        [UDL_DT_9_button],
                                                        [UDL_DT_10_button],
                                                        [UVED_NAZAD_button]])

### Обработка ошибки, финал: человек выбирает отработана заявка или нет
