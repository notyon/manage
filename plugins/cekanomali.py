from pyrogram import filters
from pyrogram.types import Message

# URL atau path gambar anomali
ANOMALI_IMAGE_URL = "https://i.ibb.co/XFv5Mxg/anomali.jpg"  # Ganti sesuai kebutuhan

def register(app):
    @app.on_message(filters.command("cekanomali") & (filters.group | filters.private))
    async def cekanomali_handler(client, message: Message):
        user = message.from_user
        mention = user.mention if user else "Pengguna"

        await message.reply_photo(
            photo=ANOMALI_IMAGE_URL,
            caption=f"👽 {mention}, anomali kamu terdeteksi..."
        )
