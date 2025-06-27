from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from utils.database import add_filter, get_filter_reply, remove_filter

def register(app):

    @app.on_message(filters.command("filter") & filters.reply & filters.group)
    async def set_filter(client, message: Message):
        user = message.from_user
        chat_id = message.chat.id

        # Hanya admin yang bisa
        member = await client.get_chat_member(chat_id, user.id)
        if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("❌ Hanya admin yang bisa set filter.")

        args = message.text.split(None, 1)
        if len(args) < 2:
            return await message.reply("❌ Format: /filter <balasan> (dengan reply pesan target)")

        keyword = message.reply_to_message.text.lower()
        response = args[1]
        add_filter(chat_id, keyword, response)

        await message.reply(f"✅ Filter untuk kata: `{keyword}` berhasil ditambahkan.")

    @app.on_message(filters.command("stopfilter") & filters.reply & filters.group)
    async def remove_filter_cmd(client, message: Message):
        user = message.from_user
        chat_id = message.chat.id

        # Hanya admin
        member = await client.get_chat_member(chat_id, user.id)
        if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("❌ Hanya admin yang bisa hapus filter.")

        keyword = message.reply_to_message.text.lower()
        success = remove_filter(chat_id, keyword)
        if success:
            await message.reply(f"✅ Filter untuk `{keyword}` dihapus.")
        else:
            await message.reply("⚠️ Filter tidak ditemukan.")

    @app.on_message(filters.text & filters.group & ~filters.command(["filter", "stopfilter"]))
    async def auto_reply_filter(client, message: Message):
        chat_id = message.chat.id
        text = message.text.lower()

        response = get_filter_reply(chat_id, text)
        if response:
            await message.reply(response)
