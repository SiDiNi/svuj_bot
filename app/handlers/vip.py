from datetime import datetime

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select

from app.database.database import get_db
from app.keyboards.inline import InlineKeyboard as IK
from app.models.models import User


vip_router = Router()


@vip_router.message(Command("start"))
async def start_command(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    async with get_db() as session:
        stmt = select(User).where(User.tg_id == user_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            new_user = User(
                tg_id=user_id,
                full_name=full_name,
                username=username,
                created_at=datetime.now(),
            )
            session.add(new_user)

    await message.answer("МЕНЮ", reply_markup=IK.inline_menu())


@vip_router.callback_query(F.data == "services")
async def show_services(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Наши услуги:", reply_markup=IK.our_services())
    await callback.message.answer(
        text="Прочие услуги:", reply_markup=IK.other_services()
    )


@vip_router.callback_query(F.data == "back_other")
async def back_from_other(callback: CallbackQuery):
    await callback.message.delete()
    prev_msg_id = callback.message.message_id - 1
    await callback.message.chat.delete_message(prev_msg_id)
    await callback.message.answer(text="МЕНЮ", reply_markup=IK.inline_menu())
    await callback.answer()


@vip_router.callback_query(F.data == "about_me")
async def show_about_me(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text="Салют! Занимаюсь сведосом 4 года, работаю в любых жанрах. Работал с такими артистами как: T-fest, eshkatitko, Fkey, W1lton и т.д.\n\nТак же пишу свою музыку под ником SVUJYK, кому интересно, ищите меня на всех площадках. Всех обнял! 🙏♥️",
        reply_markup=IK.back(),
    )
    await callback.answer()


@vip_router.callback_query(F.data == "back")
async def back_to_main(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="МЕНЮ", reply_markup=IK.inline_menu())
    await callback.answer()


@vip_router.message()
async def unknown_message_handler(message: Message):
    await message.answer(
        "🤖 Я понимаю только определенные команды и кнопки.\n"
        "Используйте /start для начала работы."
    )
