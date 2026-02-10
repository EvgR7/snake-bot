import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os
from snake import Snake
from is_text import IsText
from config import FIELD_WIDTH, FIELD_HEIGHT
from game import Game
from render import render
from keyboard import control_keyboard

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)

dp = Dispatcher()
games = {}


@dp.callback_query(F.data.in_({'UP', 'DOWN', 'LEFT', 'RIGHT'}))
async def on_move(callback):
    user_id = callback.from_user.id
    direction = callback.data
    game = games.get(user_id)
    if not game:
        await callback.answer('Игра не запущена')
        return
    game.snake.set_direction(direction)

    if game.game_over is False:
        game.tick()

        if game.snake.alive is False:
            game.game_over = True
            text = str(game.score)

            print('я здесь 1')
            await callback.message.edit_text(f'Ваш рекорд {text} \n Game Over')
            del games[user_id]
        else:
            await callback.message.edit_text(render(game), reply_markup=control_keyboard())
        await callback.answer()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет!")


@dp.message(Command("game"))
async def start_game(message: Message):
    user_id = message.from_user.id
    game = Game(user_id, FIELD_WIDTH, FIELD_HEIGHT)
    games[user_id] = game

    text = render(game)

    await message.answer(text, reply_markup=control_keyboard())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())