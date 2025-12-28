import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8337161401:AAFM2TacDfashzev5SZ0EZabBpsUfn1Eto8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Salom, Ahlidin! 😎\n"
        "Bot ishlayapti.\n"
        "Yozing — javob beraman."
    )

@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())