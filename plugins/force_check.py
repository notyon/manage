
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from utils.database import db
from config import LOG_GROUP_ID
from utils.log import send_log

async def check_force(client, user_id, chat_id):
    data = await db.force.find_one({"chat_id": chat_id})
    if not data:
        return True, None

    try:
        member = await client.get_chat_member(data["channel_id"], user_id)
        return member.status in ["member", "administrator", "creator"], data
    except:
        return False, data

def register(app):
    @app.on_message(filters.group & filters.text)
    async def enforce_force_sub(client, message: Message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        ok, data = await check_force(client, user_id, chat_id)
        if not ok and data:
            await client.restrict_chat_member(chat_id, user_id, permissions={"can_send_messages": False})
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{data['channel_username']}")],
                [InlineKeyboardButton("✅ Sudah Join, Unmute", callback_data=f"unmute_{chat_id}")]
            ])
            await message.reply("❌ Anda harus join channel terlebih dahulu untuk bisa mengirim pesan.", reply_markup=buttons)

    @app.on_callback_query(filters.regex("unmute_"))
    async def unmute_callback(client, callback_query: CallbackQuery):
        chat_id = int(callback_query.data.split("_")[1])
        user_id = callback_query.from_user.id
        ok, data = await check_force(client, user_id, chat_id)
        if ok:
            await client.restrict_chat_member(chat_id, user_id, permissions={"can_send_messages": True})
            await callback_query.message.edit("✅ Anda telah diunmute, silakan kirim pesan.")
            await send_log(client, f"✅ {callback_query.from_user.mention} berhasil unmute di {chat_id}")
        else:
            await callback_query.answer("🚫 Gagal, pastikan kamu sudah join channel.", show_alert=True)
