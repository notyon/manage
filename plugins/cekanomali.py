
from pyrogram import filters
from pyrogram.types import Message, InputMediaPhoto
import random

ANOMALI_PICTS = [
    "https://telegra.ph/file/33a51b1cf395d5609b8f7.jpg",
    "https://telegra.ph/file/9de6c160bfe48be84277c.jpg",
    "https://telegra.ph/file/0cda8770a15e5309ddbb5.jpg"
]

def register(app):
    @app.on_message(filters.command("cekanomali") & (filters.group | filters.private))
    async def cek_anomali(client, message: Message):
        pict = random.choice(ANOMALI_PICTS)
        mention = message.from_user.mention
        await message.reply_photo(
            photo=pict,
            caption=f"⚠️ Anomali kamu, {mention}..."
        )
