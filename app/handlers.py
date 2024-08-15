import json
from pprint import pprint
import random
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import app.settings
from app import settings
from app.settings import DB
from app.Keyboards import main_menu_keyboard, build_quotes_keyboard, cancel_states_keyboard
from app.data.db import get_quotes, create_quote
from app.fsm import QuoteCreateForm



router = Router()



@router.message(Command("start"))
@router.message(Command("menu"))
async def command_start_handler(message: Message) -> None:
    if message.text == "/start":
        await message.answer(f"Hello, {message.from_user.full_name}!",
                             reply_markup=main_menu_keyboard())
    else:
        await message.answer(f"Menu:",
                             reply_markup=main_menu_keyboard())


@router.message(Command("random_quotes"))
async def send_json_data2(message: Message):
    with open(settings.DB, encoding='utf8') as file:
        data2 = json.load(file)
        quote: dict = random.choice(data2)
        await message.answer(text=f"{quote['quote']} - {quote['author']}",
                             reply_markup=main_menu_keyboard())


def quotes2(update, context):
    send_json_data2(context.bot, update.message.chat_id)


@router.callback_query(F.data == "back")
async def back_handler(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.answer()
    await send_json_data2(callback.message)

@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "відміна")
@router.message(F.text == "Відмінна додавання цитати")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Створення цитати відмінено",
        reply_markup=main_menu_keyboard()
    )

@router.message(Command("new_quote"))
@router.message(F.text == "Додати нову цитату")
async def create_quote_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(QuoteCreateForm.quote)
    await message.answer(text="Напишіть свою цитату",
                         reply_markup=cancel_states_keyboard())


@router.message(QuoteCreateForm.quote)
async def proces_quote(message: Message, state: FSMContext) -> None:
    data = await state.update_data(quote=message.text)
    print(data)
    await state.set_state(QuoteCreateForm.author)
    await message.answer("Хто автор цитати?",
                         reply_markup=cancel_states_keyboard())

@router.message(QuoteCreateForm.author)
async def process_author(message: Message, state: FSMContext):
    data = await state.update_data(author=message.text)
    print(data)
    await state.clear()  # stop FSM

    print(data)
    create_quote(data)
    await message.answer(f"Цитата  {data.get('quote')} додано до бібліотеки",
                         reply_markup=main_menu_keyboard())






