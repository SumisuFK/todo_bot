from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import app.database.requests as rq

async def tasks(tg_id):
    keyboard = InlineKeyboardBuilder()
    tasks = await rq.get_tasks(tg_id)
    for task in tasks:
        keyboard.add(InlineKeyboardButton(text=task.task, callback_data=f'task_{task.id}'))
    return keyboard.adjust(1).as_markup()