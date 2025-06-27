from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

from config import FORCE_JOIN_CHANNEL
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
            await client.get_chat_member(FORCE_JOIN_CHANNEL, user_id)
            # Jika user sebelumnya dimute, unmute otomatis
            if await is_user_muted(chat_id, user_id):
                await client.unrestrict_chat_member(chat_id, user_id)
                await unmute_user(chat_id, user_id
