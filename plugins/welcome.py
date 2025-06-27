from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_USERNAME
from utils.database import set_welcome, get_welcome
from pyrogram.enums import ChatMemberStatus

def register(app):

    # Welcome saat user join grup
    @app.on_message(filters.new_chat_members)
    async def welcome_user(client, message: Message):
        chat_id = message.chat.id
        user = message.new_chat_members[0]

        welcome_text = get_welcome(chat_id)
        if not welcome_text:
            return

        mention = f"[{user.first_name}](tg://user?id={user.id})"
        text = welcome_text.replace("{mention}", mention)
        await message.reply(text, disable_web_page_preview=True)

    # Set welcome message via DM
    @app.on_message(filters.private & filters.command("setwelcome"))
    async def set_welcome_msg(client, message: Message):
        user = message.from_user

        if user.username != OWNER_USERNAME:
            return await message.reply("❌ Hanya owner yang bisa set welcome.")

        args = message.text.split(None, 2)
        if len(args) < 3:
            return await message.reply("❌ Format salah.\nGunakan: /setwelcome <chat_id> <pesan>")

        try:
            chat_id = int(args[1])
        except:
            return await message.reply("❌ Chat ID harus berupa angka.")

        welcome_text = args[2]
        set_welcome(chat_id, welcome_text)
        await message.reply("✅ Pesan welcome berhasil disimpan.")
