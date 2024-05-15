from aiogram.fsm.state import StatesGroup, State
from pydantic import BaseModel, ValidationError


class QuoteCreateForm(StatesGroup):
    quote = State()
    author = State()
