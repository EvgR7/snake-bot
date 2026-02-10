from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def control_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text='⬆', callback_data='UP')],
                                [InlineKeyboardButton(text='⬇', callback_data='DOWN')],
                                [InlineKeyboardButton(text='⬅', callback_data='LEFT')],
                                [InlineKeyboardButton(text='➡', callback_data='RIGHT')]])
