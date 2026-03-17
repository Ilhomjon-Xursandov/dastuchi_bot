#User ma'lumotlarini olish
from aiogram import Bot
from aiogram.types import Message

async def get_user_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()

    text = (
        f"{message.from_user.mention_html('USER INFO: ')}\n\n" 
        f"User full name: { message.from_user.full_name }\n" #userning to'liq ismim familyasini oladi
        f"User ID: {message.from_user.id}\n" #userning idsini olish
    )
    if user.bio: text += f"Bio: {user.bio}" #agar mavjud bo'lsa userning biosnini olish
    if message.from_user.username: text += f"Username: @{message.from_user.username}" #username olish
    if user_photos.photos:
        await message.answer_photo(
            user_photos.photos[0][-1].file_id,
            caption=text,
            parse_mode="HTML"
        )
    else:
        await message.answer(text)