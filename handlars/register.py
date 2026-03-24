from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.register_state import RegisterState
from services.register_service import RegisterService

router = Router()
service = RegisterService()

@router.message(Command("start"))
async def start_handle(message: Message, state: FSMContext):
    await message.answer("Ismingizni kiriting: ")
    await state.set_state(RegisterState.name)

@router.message(RegisterState.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Yoshingizni kiriting: ")
    await state.set_state(RegisterState.age)

@router.message(RegisterState.age)
async def get_age(message: Message, state: FSMContext):
    data = await state.get_data()

    user = await service.save_user(
        message.from_user.id,
        data["name"],
        int(message.text)
    )

    await message.answer(
        f"Saqlandi: {user['name']} - {user['age']}"
    )

    await state.clear()