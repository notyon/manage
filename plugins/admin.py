
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

def register(app):
    async def is_admin(client, message):
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]

    @app.on_message(filters.command("mute") & filters.group)
    async def mute(client, message: Message):
        if not await is_admin(client, message):
            return await message.reply("❌ Kamu bukan admin.")
        if not message.reply_to_message:
            return await message.reply("❌ Balas pesan yang ingin di-mute.")
        await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions={"can_send_messages": False})
        await message.reply("✅ Pengguna telah di-mute.")

    @app.on_message(filters.command("unmute") & filters.group)
    async def unmute(client, message: Message):
        if not await is_admin(client, message):
            return await message.reply("❌ Kamu bukan admin.")
        if not message.reply_to_message:
            return await message.reply("❌ Balas pesan yang ingin di-unmute.")
        await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions={"can_send_messages": True})
        await message.reply("✅ Pengguna telah di-unmute.")

    @app.on_message(filters.command("kick") & filters.group)
    async def kick(client, message: Message):
        if not await is_admin(client, message):
            return await message.reply("❌ Kamu bukan admin.")
        if not message.reply_to_message:
            return await message.reply("❌ Balas pesan yang ingin di-kick.")
        user_id = message.reply_to_message.from_user.id
        await client.ban_chat_member(message.chat.id, user_id)
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply("✅ Pengguna telah di-kick.")

    @app.on_message(filters.command("ban") & filters.group)
    async def ban(client, message: Message):
        if not await is_admin(client, message):
            return await message.reply("❌ Kamu bukan admin.")
        if not message.reply_to_message:
            return await message.reply("❌ Balas pesan yang ingin di-ban.")
        await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("✅ Pengguna telah di-ban.")

    @app.on_message(filters.command("unban") & filters.group)
    async def unban(client, message: Message):
        if not await is_admin(client, message):
            return await message.reply("❌ Kamu bukan admin.")
        if len(message.command) < 2:
            return await message.reply("❌ Gunakan /unban <user_id>")
        user_id = int(message.command[1])
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply("✅ Pengguna telah di-unban.")
