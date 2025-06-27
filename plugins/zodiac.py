from pyrogram import filters
from pyrogram.types import Message
import datetime

zodiac_data = {
    "Capricorn": ((12, 22), (1, 19)),
    "Aquarius": ((1, 20), (2, 18)),
    "Pisces": ((2, 19), (3, 20)),
    "Aries": ((3, 21), (4, 19)),
    "Taurus": ((4, 20), (5, 20)),
    "Gemini": ((5, 21), (6, 20)),
    "Cancer": ((6, 21), (7, 22)),
    "Leo": ((7, 23), (8, 22)),
    "Virgo": ((8, 23), (9, 22)),
    "Libra": ((9, 23), (10, 22)),
    "Scorpio": ((10, 23), (11, 21)),
    "Sagittarius": ((11, 22), (12, 21)),
}

def get_zodiac(month, day):
    for sign, ((start_month, start_day), (end_month, end_day)) in zodiac_data.items():
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign
    return "Tidak diketahui"

def register(app):
    @app.on_message(filters.command("zodiak") & (filters.group | filters.private))
    async def zodiac_cmd(client, message: Message):
        args = message.text.split()
        if len(args) < 2:
            return await message.reply("Contoh: /zodiak 12-08")
        
        try:
            day, month = map(int, args[1].split("-"))
            sign = get_zodiac(month, day)
            await message.reply(f"Zodiak kamu: ♈ {sign}")
        except:
            await message.reply("Format salah. Gunakan: /zodiak 12-08")
