
from pyrogram import filters
from pyrogram.types import Message
from utils.database import db

def register(app):
    @app.on_message(filters.command("filter") & (filters.group | filters.private))
    async def add_filter(client, message: Message):
        if not message.reply_to_message or len(message.command) < 2:
            return await message.reply("❌ Balas pesan yang ingin dijadikan trigger dengan: /filter <balasan>")
        trigger = message.reply_to_message.text.lower().strip()
        response = message.text.split(None, 1)[1]
        chat_id = str(message.chat.id if message.chat else message.from_user.id)
        await db.filters.update_one(
            {"chat_id": chat_id},
            {"$set": {f"rules.{trigger}": response}},
            upsert=True
        )
        await message.reply(f"✅ Filter ditambahkan untuk kata: `{trigger}`")

    @app.on_message(filters.text & (filters.group | filters.private))
    async def filter_reply(client, message: Message):
        chat_id = str(message.chat.id if message.chat else message.from_user.id)
        filters_data = await db.filters.find_one({"chat_id": chat_id})
        if not filters_data or "rules" not in filters_data:
            return
        text = message.text.lower().strip()
        for trigger, reply_text in filters_data["rules"].items():
            if text == trigger:
                return await message.reply(reply_text)
