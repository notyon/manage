
from pyrogram import filters
from pyrogram.types import Message
import datetime

ZODIAK = {
    (1, 20): "Aquarius", (2, 19): "Pisces", (3, 21): "Aries", (4, 20): "Taurus",
    (5, 21): "Gemini", (6, 21): "Cancer", (7, 23): "Leo", (8, 23): "Virgo",
    (9, 23): "Libra", (10, 23): "Scorpio", (11, 23): "Sagittarius", (12, 22): "Capricorn"
}

def cari_zodiak(tgl, bln):
    for (batas_bln, batas_tgl), nama in reversed(ZODIAK.items()):
        if (bln, tgl) >= (batas_bln, batas_tgl):
            return nama
    return "Capricorn"

def register(app):
    @app.on_message(filters.command("zodiak") & (filters.group | filters.private))
    async def zodiak_handler(client, message: Message):
        if len(message.command) < 2:
            return await message.reply("🔮 Gunakan format: /zodiak <dd-mm>")
        tanggal = message.text.split(None, 1)[1].replace("/", "-").replace(".", "-")
        try:
            tgl, bln = map(int, tanggal.split("-"))
            datetime.date(2000, bln, tgl)  # validasi
            hasil = cari_zodiak(tgl, bln)
            await message.reply(f"🔮 Zodiak kamu: {hasil}")
        except:
            await message.reply("❌ Format salah. Contoh: /zodiak 21-03")
