
import asyncio                       # Asinxron ishlash uchun
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types              # Bot va Dispatcher klasslari
from aiogram.types import Message                       # Xabar tipi
from aiogram.filters import Command                     # Komanda filtri

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")                 # Bot tokeni

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)                                  # Bot obyekti yaratish
dp = Dispatcher()                                       # Dispatcher obyekti

@dp.message(Command("start"))                          
async def start(message: Message):                      
    await message.answer(f"Salom {message.from_user.full_name}!")   

@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Bot hozircha ishlab chiqilmoqda kamchiliklar uchun usur so'raymiz!")    

async def main():                     # Asosiy funksiya
    print("Bot ishga tushdi...")      # Konsolga chiqarish
    await dp.start_polling(bot)       # Botni ishga tushirish

if __name__ == "__main__":            # Agar fayl to'g'ridan-to'g'ri ishga tushirilsa
    asyncio.run(main())               # main() funksiyasini ishga tushir
