
from pyrogram import filters
from pyrogram.types import Message
from utils.database import db
from config import OWNER_USERNAME

def register(app):
    @app.on_message(filters.private & filters.command("setwelcome"))
    async def set_welcome(client, message: Message):
        if message.from_user.username != OWNER_USERNAME:
            return await message.reply("❌ Hanya pemilik bot yang dapat mengatur pesan welcome.")
        if len(message.command) < 2:
            return await message.reply("📝 Gunakan: /setwelcome Selamat datang di grup kami!")
        text = message.text.split(None, 1)[1]
        await db.config.update_one({"_id": "welcome"}, {"$set": {"text": text}}, upsert=True)
        await message.reply("✅ Pesan welcome berhasil disimpan.")

    @app.on_message(filters.new_chat_members)
    async def welcome_new_member(client, message: Message):
        new_members = message.new_chat_members
        config = await db.config.find_one({"_id": "welcome"})
        text = config["text"] if config and "text" in config else "👋 Selamat datang {mention}!"
        for member in new_members:
            if member.is_bot:
                continue
            mention = member.mention
            await message.reply(text.replace("{mention}", mention))
