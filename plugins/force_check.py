from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

from utils.database import get_force_channel
from utils.database import is_user_muted, mute_user, unmute_user
from utils.log import send_log

def register(app):
    @app.on_message(filters.group & ~filters.service)
    async def check_force_sub(client, message):
        user = message.from_user
        chat_id = message.chat.id
        user_id = user.id

        # Admin / Creator tetap boleh kirim
        member = await client.get_chat_member(chat_id, user_id)
        if member.status in ["administrator", "creator"]:
            return

        try:
            # Cek apakah user sudah join channel wajib
            channel_id = get_force_channel(chat_id)
    if not channel_id:
        return  # tidak wajib join jika belum diset

    await client.get_chat_member(channel_id, user_id)
            # Jika user sebelumnya dimute, unmute otomatis
            if await is_user_muted(chat_id, user_id):
                await client.unrestrict_chat_member(chat_id, user_id)
                await unmute_user(chat_id, user_id)
        except UserNotParticipant:
            # Mute user
            await client.restrict_chat_member(
                chat_id,
                user_id,
                permissions={"can_send_messages": False}
            )
            await mute_user(chat_id, user_id)

            # Hapus pesan mereka
            try:
                await message.delete()
            except:
                pass

            # Kirim pesan unmute dengan tombol
            buttons = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("🔗 Join Channel", url=f"https://t.me/c/{str(FORCE_JOIN_CHANNEL)[4:]}"),
                ],
                [
                    InlineKeyboardButton("✅ Saya Sudah Join - Unmute", callback_data=f"unmute:{chat_id}")
                ]
            ])

            await message.reply(
                "⚠️ Kamu harus bergabung ke channel terlebih dahulu untuk bisa mengirim pesan.",
                reply_markup=buttons
            )
            await send_log(f"🔒 User @{user.username or user_id} dimute karena belum join channel.")

    @app.on_callback_query(filters.regex(r"^unmute:(-?\d+)$"))
    async def handle_unmute_button(client, callback_query):
        chat_id = int(callback_query.data.split(":")[1])
        user_id = callback_query.from_user.id

        try:
            await client.get_chat_member(FORCE_JOIN_CHANNEL, user_id)

            await client.unrestrict_chat_member(chat_id, user_id)
            await unmute_user(chat_id, user_id)

            await callback_query.answer("✅ Kamu sudah di-unmute!", show_alert=True)
            await send_log(f"🔓 User @{callback_query.from_user.username or user_id} di-unmute (join channel).")
        except UserNotParticipant:
            await callback_query.answer("❌ Kamu belum join channel!", show_alert=True)
