from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from utils.log import send_log

def register(app):

    async def is_admin(client, chat_id, user_id):
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

    @app.on_message(filters.command("mute") & filters.reply & filters.group)
    async def mute_user(client, message: Message):
        if not await is_admin(client, message.chat.id, message.from_user.id):
            return await message.reply("❌ Hanya admin yang bisa mute.")
        
        user_id = message.reply_to_message.from_user.id
        await client.restrict_chat_member(message.chat.id, user_id, permissions={"can_send_messages": False})
        await message.reply("🔇 User berhasil dimute.")
        await send_log("🔒 User dimute karena belum join channel.", client)

    @app.on_message(filters.command("unmute") & filters.reply & filters.group)
    async def unmute_user(client, message: Message):
        if not await is_admin(client, message.chat.id, message.from_user.id):
            return await message.reply("❌ Hanya admin yang bisa unmute.")

        user_id = message.reply_to_message.from_user.id
        await client.unrestrict_chat_member(message.chat.id, user_id)
        await message.reply("🔊 User berhasil di-unmute.")

    @app.on_message(filters.command("ban") & filters.reply & filters.group)
    async def ban_user(client, message: Message):
        if not await is_admin(client, message.chat.id, message.from_user.id):
            return await message.reply("❌ Hanya admin yang bisa ban.")

        user_id = message.reply_to_message.from_user.id
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply("🚫 User berhasil diban.")

    @app.on_message(filters.command("unban") & filters.reply & filters.group)
    async def unban_user(client, message: Message):
        if not await is_admin(client, message.chat.id, message.from_user.id):
            return await message.reply("❌ Hanya admin yang bisa unban.")

        user_id = message.reply_to_message.from_user.id
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply("✅ User berhasil di-unban.")

    @app.on_message(filters.command("kick") & filters.reply & filters.group)
    async def kick_user(client, message: Message):
        if not await is_admin(client, message.chat.id, message.from_user.id):
            return await message.reply("❌ Hanya admin yang bisa kick.")

        user_id = message.reply_to_message.from_user.id
        await client.ban_chat_member(message.chat.id, user_id)
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply("👢 User berhasil di-kick.")
