import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os
from snake import Snake
#from is_text import IsText
from config import FIELD_WIDTH, FIELD_HEIGHT
from game import Game
from render import render
from keyboard import control_keyboard
from db import init_db, get_max_score, update_max_score

init_db()

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token = TOKEN)

dp = Dispatcher()
games = {}

async def game_loop(chat_id, message_id):
    game = games[chat_id]

    while game.running:
        await asyncio.sleep(0.8)
        if game.game_over is False:
            game.tick()
            if game.snake.alive is False:
                game.game_over = True
                current =game.score
                best = get_max_score(game.user_id)
                #print(current,best)
                is_record = False
                if current > best:
                    update_max_score(game.user_id, current)
                    best = current
                    is_record = True
                text = ('GAME OVER\n\n' f'Рекорд: {current}\n' f'Лучший: {best}')
                if is_record:
                    text += '\n\n НОВЫЙ РЕКОРД!!!'
                #print('я здесь 1')
                #text = 'finish'
                await bot.edit_message_text(text,
                                            chat_id = chat_id, message_id = message_id)
                del games[chat_id]
                return
            else:
                await bot.edit_message_text(render(game),chat_id=chat_id,
                                            message_id=message_id,reply_markup= control_keyboard())

@dp.callback_query(F.data.in_({'UP','DOWN','LEFT','RIGHT'}))
async def on_move(callback):

    game = games.get(callback.message.chat.id)
    if not game:
        await callback.answer('Игра не запущена')
        return
    game.snake.set_direction(callback.data)
    await callback.answer()



@dp.message(Command("start"))
async def start(message:Message):
    await message.answer("Привет!")


@dp.message(Command("game"))
async def start_game(message : Message):
    user_id = message.from_user.id
    game = Game(user_id, FIELD_WIDTH, FIELD_HEIGHT)
    games[message.chat.id] = game

    msg = await message.answer(render(game), reply_markup=control_keyboard())
    game.task = asyncio.create_task(game_loop(message.chat.id, msg.message_id))



async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())