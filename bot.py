from pyrogram import Client, filters

from config import API_ID, API_HASH, BOT_TOKEN

app = Client("test_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private)
async def handle_private(client, message):
    await message.reply("✅ Bot aktif dan merespon kamu!")

@app.on_message(filters.command("test") & filters.group)
async def handle_test(client, message):
    await message.reply("✅ Bot juga aktif di grup ini!")

print("🤖 Bot minimal test aktif...")
app.run()
