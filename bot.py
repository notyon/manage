from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from plugins import (
    welcome, force_check, auto_reply, zodiac,
    admin, config_force, cekanomali
)

from utils.log import send_log

app = Client("manage_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register all plugins
welcome.register(app)
force_check.register(app)
auto_reply.register(app)
zodiac.register(app)
admin.register(app)
config_force.register(app)
cekanomali.register(app)

@app.on_message()
async def handler(_, message):
    if message.text == "/start":
        text = (
            "👋 Selamat datang, saya adalah bot manage! Gunakan saya untuk membantu mengatur grup, cek zodiak, auto-reply, dan lainnya."
        )
        buttons = [
            [{"text": "Group Support", "url": f"https://t.me/{SUPPORT_GROUP}"}],
            [{"text": "Owner", "url": f"https://t.me/{OWNER_USERNAME}"}],
        ]
        await message.reply(text)

print("🤖 Bot is running...")
app.run()
