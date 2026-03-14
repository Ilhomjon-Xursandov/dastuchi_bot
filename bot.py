
import asyncio                    # Asinxron ishlash uchun
import logging
from aiogram import Bot, Dispatcher  # Bot va Dispatcher klasslari
from aiogram.types import Message    # Xabar tipi
from aiogram.filters import Command  # Komanda filtri

TOKEN = "8635271477:AAHE0AokBJdgvMplyxbsKAb_vv0sx4MDoMw"                     # Bot tokeni

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)                                  # Bot obyekti yaratish
dp = Dispatcher()                                       # Dispatcher obyekti

@dp.message(Command("start"))                           # Agar /start kelsa
async def start(message: Message):                      # Bu funksiya ishlasin
    await message.answer("Salom! Bot ishga tushdi!")    # Javob qaytarsin

@dp.message(Command("help"))
async def start(message: Message):
    await message.answer("Bot hozircha ishlab chiqilmoqda kamchiliklar uchun usur so'raymiz!")    

async def main():                     # Asosiy funksiya
    print("Bot ishga tushdi...")      # Konsolga chiqarish
    await dp.start_polling(bot)       # Botni ishga tushirish

if __name__ == "__main__":            # Agar fayl to'g'ridan-to'g'ri ishga tushirilsa
    asyncio.run(main())                # main() funksiyasini ishga tushir
