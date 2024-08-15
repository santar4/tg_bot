
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
def main_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Додати нову цитату")
    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup



def build_quotes_keyboard(quotes: list):
    builder = InlineKeyboardBuilder()
    for index, quot in enumerate(quotes):
        builder.button(text=quot.get("tite"), callback_data=f"quot_{index}")

    return builder.as_markup()


def cancel_states_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Cancel creating quote")
    markup = builder.as_markup()
    markup.resize_keyboard = True
    return markup