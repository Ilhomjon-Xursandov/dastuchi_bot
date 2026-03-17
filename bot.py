
import asyncio, logging, os                    # Asinxron ishlash uchun
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types              # Bot va Dispatcher klasslari
from aiogram.types import Message                       # Xabar tipi
from aiogram.filters import Command
from user_info import get_user_info

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")                 # Bot tokeni

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)                                  # Bot obyekti yaratish
dp = Dispatcher()                                       # Dispatcher obyekti

@dp.message(Command("start"))                          
async def start(message: Message):                      
    await message.answer(f"Salom {message.from_user.full_name}!😍")

@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Bot hozircha ishlab chiqilmoqda kamchiliklar uchun usur so'raymiz!")    

#jaob sifatida javob qaytarish
@dp.message(Command('info'))
async def cmd_reply(message: types.Message, bot: Bot):
    await get_user_info(message, bot)

async def main():                     # Asosiy funksiya
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)       # Botni ishga tushirish

if __name__ == "__main__":            # Agar fayl to'g'ridan-to'g'ri ishga tushirilsa
    asyncio.run(main())               # main() funksiyasini ishga tushir
