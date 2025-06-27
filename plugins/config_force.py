from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_USERNAME
from utils.database import set_force_channel, get_force_channel
from pyrogram.enums import ChatMemberStatus

def register(app):

    @app.on_message(filters.private & filters.command("setforce"))
    async def set_force(client, message: Message):
        user = message.from_user
        args = message.text.split()

        if len(args) != 3:
            return await message.reply("❌ Format: /setforce <chat_id_grup> <channel_id>")

        try:
            chat_id = int(args[1])
            channel_id = int(args[2])
        except:
            return await message.reply("❌ Format ID salah. Harus angka.")

        # Cek apakah user adalah OWNER atau admin grup tsb
        is_owner = user.username == OWNER_USERNAME
        try:
            member = await client.get_chat_member(chat_id, user.id)
            is_admin = member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
        except:
            is_admin = False

        if not (is_owner or is_admin):
            return await message.reply("❌ Hanya admin grup atau owner bot yang bisa set force join.")

        set_force_channel(chat_id, channel_id)
        await message.reply(f"✅ Channel wajib untuk grup `{chat_id}` diset ke `{channel_id}`.")

    @app.on_message(filters.command("forceid") & filters.group)
    async def show_force_id(client, message: Message):
        chat_id = message.chat.id
        channel_id = get_force_channel(chat_id)

        if channel_id:
            await message.reply(f"📌 Channel wajib join ID: `{channel_id}`")
        else:
            await message.reply("ℹ️ Belum ada channel wajib yang diset.")
