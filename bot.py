from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

from config import API_ID, API_HASH, BOT_TOKEN, SUPPORT_GROUP, OWNER_USERNAME
from plugins import (
    welcome, force_check, auto_reply, zodiac,
    admin, config_force, cekanomali
)
from utils.log import send_log

app = Client("manage_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# === REGISTER PLUGIN ===
welcome.register(app)
force_check.register(app)
auto_reply.register(app)
zodiac.register(app)
admin.register(app)
config_force.register(app)
cekanomali.register(app)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    text = (
        "👋 Selamat datang, saya adalah bot manage!\n\n"
        "Gunakan saya untuk membantu mengatur grup, cek zodiak, auto-reply, dan lainnya."
    )
    buttons = [
        [{"text": "Group Support", "url": f"https://t.me/{SUPPORT_GROUP}"}],
        [{"text": "Owner", "url": f"https://t.me/{OWNER_USERNAME}"}],
    ]
    await message.reply(text, reply_markup=InlineKeyboardMarkup(buttons))

print("🤖 Bot is running...")
app.run()
