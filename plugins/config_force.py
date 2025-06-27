
from pyrogram import filters
from pyrogram.types import Message
from utils.database import db
from config import OWNER_USERNAME

def register(app):
    @app.on_message(filters.private & filters.command("setforce"))
    async def set_force(client, message: Message):
        if message.from_user.username != OWNER_USERNAME:
            return await message.reply("❌ Hanya pemilik bot yang dapat mengatur force subscribe.")
        if len(message.command) < 3:
            return await message.reply("📝 Gunakan: /setforce <chat_id> <channel_username>")
        try:
            chat_id = int(message.command[1])
            channel_username = message.command[2].lstrip("@").strip()
            await db.force.update_one(
                {"chat_id": chat_id},
                {"$set": {"channel_id": f"@{channel_username}", "channel_username": channel_username}},
                upsert=True
            )
            await message.reply(f"✅ Force subscribe berhasil diset:
Chat ID: `{chat_id}`
Channel: `{channel_username}`")
        except Exception as e:
            await message.reply(f"❌ Gagal menyimpan: {e}")
